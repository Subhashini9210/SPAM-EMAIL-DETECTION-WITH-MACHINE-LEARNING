"""Train and evaluate a spam classifier from a labeled CSV."""
import argparse
from math import ceil
from email import policy
from email.parser import BytesParser
from pathlib import Path

import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

from detector.classification import normalize_label


def read_spamassassin_corpus(root):
    """Read extracted SpamAssassin ham/spam folders as labeled email text."""
    rows = []
    folder_labels = {
        "ham": "ham", "easy_ham": "ham", "easy_ham_2": "ham",
        "hard_ham": "ham", "spam": "spam", "spam_2": "spam",
    }
    for folder_name, label in folder_labels.items():
        folder = root / folder_name
        if not folder.is_dir():
            continue
        for path in folder.iterdir():
            if not path.is_file() or path.name == "cmds":
                continue
            try:
                message = BytesParser(policy=policy.default).parsebytes(path.read_bytes())
                subject = str(message.get("subject", ""))
                bodies = []
                parts = message.walk() if message.is_multipart() else [message]
                for part in parts:
                    if part.get_content_type() != "text/plain" or part.get_filename():
                        continue
                    try:
                        content = part.get_content()
                    except (LookupError, UnicodeError, ValueError):
                        continue
                    if isinstance(content, str) and content.strip():
                        bodies.append(content.strip())
                text = "\n".join(([f"Subject: {subject}"] if subject else []) + bodies).strip()
                if text:
                    rows.append({"label": label, "message": text})
            except (OSError, ValueError):
                continue
    if not rows:
        raise SystemExit(f"No readable email messages found in corpus directory: {root}")
    return pd.DataFrame(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("data", help="CSV, UCI tab-separated file, or extracted SpamAssassin corpus directory")
    parser.add_argument("--label-column", default="label")
    parser.add_argument("--text-column", default="message")
    args = parser.parse_args()
    source = Path(args.data)
    if source.is_dir():
        data = read_spamassassin_corpus(source)
        args.label_column, args.text_column = "label", "message"
    else:
        suffix = source.suffix.lower()
        if suffix == ".csv":
            data = pd.read_csv(source)
        else:
            sample = None
            try:
                sample = pd.read_csv(source, sep="\t", nrows=5, header=None)
            except Exception:
                pass
            if sample is not None and not sample.empty and sample.shape[1] >= 2:
                first_label = str(sample.iloc[0, 0]).strip().lower()
                if first_label in {"ham", "spam", "0", "1", "yes", "no"}:
                    data = pd.read_csv(source, sep="\t", header=None, names=[args.label_column, args.text_column])
                else:
                    data = pd.read_csv(source, sep="\t")
            else:
                try:
                    data = pd.read_csv(source)
                except Exception as exc:
                    raise SystemExit(
                        "Provide a CSV, tab-separated data file, or an extracted SpamAssassin email corpus directory."
                    ) from exc

    if args.label_column not in data.columns or args.text_column not in data.columns:
        if len(data.columns) >= 2:
            data = data.iloc[:, :2].copy()
            data.columns = [args.label_column, args.text_column]
        else:
            raise SystemExit(f"File is missing required column(s): {args.label_column}, {args.text_column}")
    missing = {args.label_column, args.text_column} - set(data.columns)
    if missing:
        raise SystemExit(f"File is missing required column(s): {', '.join(sorted(missing))}")
    data = data[[args.label_column, args.text_column]].dropna()
    data[args.text_column] = data[args.text_column].astype(str).str.strip()
    data = data[data[args.text_column] != ""]
    try:
        data[args.label_column] = data[args.label_column].map(normalize_label)
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc
    class_counts = data[args.label_column].value_counts()
    if set(class_counts.index) != {"ham", "spam"}:
        raise SystemExit("Training data must contain both ham and spam messages.")
    test_count = ceil(len(data) * 0.2)
    if test_count < 2 or len(data) - test_count < 2 or class_counts.min() < 2:
        raise SystemExit("Training data needs enough ham and spam messages for a stratified hold-out.")

    x_train, x_test, y_train, y_test = train_test_split(
        data[args.text_column], data[args.label_column], test_size=0.2,
        random_state=42, stratify=data[args.label_column],
    )
    model = Pipeline([
        ("tfidf", TfidfVectorizer(lowercase=True, strip_accents="unicode",
                                  ngram_range=(1, 2), min_df=1, sublinear_tf=True)),
        ("classifier", LogisticRegression(max_iter=1000, class_weight="balanced")),
    ])
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    print(f"Accuracy: {accuracy_score(y_test, predictions):.4f}")
    print("Confusion matrix (true rows, predicted columns):")
    print(confusion_matrix(y_test, predictions, labels=model.classes_))
    print(classification_report(y_test, predictions, zero_division=0))
    project_root = Path(__file__).resolve().parent
    output = project_root / "spam-detection" / "outputs" / "models" / "spam_classifier.joblib"
    legacy_output = project_root / "artifacts" / "spam_classifier.joblib"
    output.parent.mkdir(parents=True, exist_ok=True)
    legacy_output.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, output)
    joblib.dump(model, legacy_output)
    print(f"Saved model to {output}")
    print(f"Also saved compatibility copy to {legacy_output}")


if __name__ == "__main__":
    main()

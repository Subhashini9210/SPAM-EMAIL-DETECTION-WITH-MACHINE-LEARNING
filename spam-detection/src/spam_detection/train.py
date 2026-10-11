"""Train, evaluate, and use a text spam classifier."""

from argparse import ArgumentParser
from pathlib import Path

import joblib
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score
from sklearn.model_selection import StratifiedKFold, cross_val_score, train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline


PROJECT_DIR = Path(__file__).resolve().parents[2]
DEFAULT_DATA_PATH = PROJECT_DIR / "data" / "raw" / "train.csv"
DEFAULT_MODEL_PATH = PROJECT_DIR / "outputs" / "models" / "spam_classifier.joblib"
DEFAULT_FIGURE_PATH = PROJECT_DIR / "outputs" / "figures" / "confusion_matrix.png"


def _load_dataset(data_path: Path) -> tuple[pd.Series, pd.Series]:
    """Load and validate the text/label CSV used by this project."""
    data = pd.read_csv(data_path)
    required = {"text", "label"}
    if not required.issubset(data.columns):
        raise ValueError("Dataset must contain the required columns: label, text")

    data = data[["text", "label"]].dropna().copy()
    data["text"] = data["text"].astype(str).str.strip()
    data["label"] = data["label"].astype(str).str.strip().str.lower()
    data = data[(data["text"] != "") & (data["label"] != "")]
    if data["label"].nunique() < 2:
        raise ValueError("Dataset must contain at least two classes")
    counts = data["label"].value_counts()
    if counts.min() < 2:
        raise ValueError("Each class must have at least two examples")
    return data["text"], data["label"]


def _make_model() -> Pipeline:
    """Keep feature extraction inside the model to prevent leakage and mismatches."""
    return Pipeline([
        ("vectorizer", CountVectorizer(lowercase=True, ngram_range=(1, 2))),
        ("classifier", MultinomialNB()),
    ])


def train_and_evaluate(
    data_path: Path = DEFAULT_DATA_PATH,
    model_path: Path = DEFAULT_MODEL_PATH,
    figure_path: Path = DEFAULT_FIGURE_PATH,
) -> dict[str, float]:
    """Train a pipeline, report hold-out/CV metrics, and save its artifacts."""
    data_path, model_path, figure_path = map(Path, (data_path, model_path, figure_path))
    texts, labels = _load_dataset(data_path)

    try:
        x_train, x_test, y_train, y_test = train_test_split(
            texts,
            labels,
            test_size=0.2,
            random_state=42,
            stratify=labels,
        )
    except ValueError as exc:
        raise ValueError("Dataset is too small for a stratified train/test split") from exc

    model = _make_model()
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    accuracy = accuracy_score(y_test, predictions)
    weighted_f1 = f1_score(y_test, predictions, average="weighted", zero_division=0)

    class_count = int(labels.value_counts().min())
    folds = min(5, class_count)
    cv = StratifiedKFold(n_splits=folds, shuffle=True, random_state=42)
    cv_scores = cross_val_score(
        _make_model(), texts, labels, cv=cv, scoring="f1_weighted"
    )
    cv_weighted_f1 = float(cv_scores.mean())

    classes = model.named_steps["classifier"].classes_
    matrix = confusion_matrix(y_test, predictions, labels=classes)
    report = classification_report(
        y_test, predictions, labels=classes, target_names=classes, zero_division=0
    )
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Weighted F1: {weighted_f1:.4f}")
    print(f"cross-validation weighted F1: {cv_weighted_f1:.4f} ({folds} folds)")
    print("Confusion Matrix:")
    print(matrix)
    print("Classification Report:")
    print(report)

    model_path.parent.mkdir(parents=True, exist_ok=True)
    figure_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, model_path)

    figure, axis = plt.subplots(figsize=(6, 5))
    axis.imshow(matrix, cmap="Blues")
    axis.set(
        xticks=range(len(classes)),
        yticks=range(len(classes)),
        xticklabels=classes,
        yticklabels=classes,
        xlabel="Predicted label",
        ylabel="Actual label",
        title="Spam classification confusion matrix",
    )
    for row in range(matrix.shape[0]):
        for column in range(matrix.shape[1]):
            axis.text(column, row, str(matrix[row, column]), ha="center", va="center")
    figure.tight_layout()
    figure.savefig(figure_path, dpi=160)
    plt.close(figure)

    return {
        "accuracy": float(accuracy),
        "weighted_f1": float(weighted_f1),
        "cross_validation_weighted_f1": cv_weighted_f1,
    }


def predict_text(text: str, model_path: Path = DEFAULT_MODEL_PATH) -> str:
    """Predict the label for one message using a saved training pipeline."""
    model_path = Path(model_path)
    if not model_path.is_file():
        raise FileNotFoundError(f"Trained model not found: {model_path}")
    model = joblib.load(model_path)
    return str(model.predict([text])[0])


def main() -> None:
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA_PATH)
    parser.add_argument("--model", type=Path, default=DEFAULT_MODEL_PATH)
    parser.add_argument("--figure", type=Path, default=DEFAULT_FIGURE_PATH)
    parser.add_argument("--predict", help="Classify a message using the saved model")
    args = parser.parse_args()

    if args.predict is not None:
        print(predict_text(args.predict, args.model))
    else:
        train_and_evaluate(args.data, args.model, args.figure)


if __name__ == "__main__":
    main()

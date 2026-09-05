"""Train and evaluate a simple text spam classifier."""

from argparse import ArgumentParser
from math import ceil
from pathlib import Path

import joblib
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
)
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

DEFAULT_DATA_PATH = Path("data/raw/train.csv")
DEFAULT_MODEL_PATH = Path("outputs/models/spam_classifier.joblib")
DEFAULT_FIGURE_PATH = Path("outputs/figures/confusion_matrix.png")


def load_and_validate_data(data_path: Path) -> pd.DataFrame:
    """Load a labelled CSV dataset and validate it for stratified evaluation."""
    if not data_path.is_file():
        raise FileNotFoundError(f"Dataset not found: {data_path}")

    df = pd.read_csv(data_path)
    required_columns = {"text", "label"}
    missing_columns = required_columns - set(df.columns)
    if missing_columns:
        missing = ", ".join(sorted(missing_columns))
        raise ValueError(f"Dataset is missing required column(s): {missing}")

    df = df.dropna(subset=["text", "label"]).copy()
    df["text"] = df["text"].astype(str).str.strip()
    df = df[df["text"].ne("")]
    if df.empty:
        raise ValueError("The dataset contains no usable text and label rows.")

    class_counts = df["label"].value_counts()
    if len(class_counts) < 2:
        raise ValueError("The dataset must contain at least two label classes.")
    if (class_counts < 2).any():
        raise ValueError("Each label class must contain at least two examples.")

    test_size = 0.2
    test_rows = ceil(len(df) * test_size)
    class_count = len(class_counts)
    if test_rows < class_count or len(df) - test_rows < class_count:
        raise ValueError(
            "The dataset is too small for a stratified 80/20 train-test split."
        )

    return df


def build_pipeline() -> Pipeline:
    """Create the text-vectorization and Naive Bayes classification pipeline."""
    return Pipeline(
        [
            ("vectorizer", CountVectorizer(stop_words="english", ngram_range=(1, 2))),
            ("model", MultinomialNB(alpha=0.5)),
        ]
    )


def train_and_evaluate(
    data_path: Path,
    model_path: Path = DEFAULT_MODEL_PATH,
    figure_path: Path = DEFAULT_FIGURE_PATH,
) -> dict[str, float]:
    """Train, evaluate, save the model, and return key evaluation metrics."""
    df = load_and_validate_data(data_path)
    test_size = 0.2
    class_counts = df["label"].value_counts()
    X_train, X_test, y_train, y_test = train_test_split(
        df["text"], df["label"], test_size=test_size, random_state=42, stratify=df["label"]
    )

    pipeline = build_pipeline()
    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)
    folds = min(5, int(class_counts.min()))
    cross_validation_f1 = cross_val_score(
        build_pipeline(),
        df["text"],
        df["label"],
        cv=folds,
        scoring="f1_weighted",
    )

    model_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(pipeline, model_path)

    figure_path.parent.mkdir(parents=True, exist_ok=True)
    display = ConfusionMatrixDisplay.from_predictions(y_test, y_pred, labels=sorted(class_counts.index))
    display.ax_.set_title("Spam classifier confusion matrix")
    display.figure_.tight_layout()
    display.figure_.savefig(figure_path, dpi=150)
    plt.close(display.figure_)

    accuracy = accuracy_score(y_test, y_pred)
    weighted_f1 = f1_score(y_test, y_pred, average="weighted", zero_division=0)

    print("Accuracy:", accuracy)
    print("Weighted F1:", weighted_f1)
    print(f"{folds}-fold cross-validation weighted F1:", cross_validation_f1.mean())
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, zero_division=0))
    print(f"\nSaved model: {model_path}")
    print(f"Saved chart: {figure_path}")

    return {
        "accuracy": accuracy,
        "weighted_f1": weighted_f1,
        "cross_validation_weighted_f1": float(cross_validation_f1.mean()),
    }


def predict_text(text: str, model_path: Path = DEFAULT_MODEL_PATH) -> str:
    """Classify one message using a saved pipeline."""
    if not model_path.is_file():
        raise FileNotFoundError(f"Saved model not found: {model_path}")
    pipeline = joblib.load(model_path)
    return str(pipeline.predict([text])[0])


def main() -> None:
    parser = ArgumentParser(description="Train a spam-detection classifier.")
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA_PATH, help="CSV dataset path")
    parser.add_argument("--model-out", type=Path, default=DEFAULT_MODEL_PATH, help="Path for saved model")
    parser.add_argument("--figure-out", type=Path, default=DEFAULT_FIGURE_PATH, help="Path for confusion-matrix image")
    parser.add_argument("--predict", help="Classify one message using the saved model")
    parser.add_argument("--model", type=Path, default=DEFAULT_MODEL_PATH, help="Saved model used with --predict")
    args = parser.parse_args()
    if args.predict:
        print("Prediction:", predict_text(args.predict, args.model))
        return
    train_and_evaluate(args.data, args.model_out, args.figure_out)


if __name__ == "__main__":
    main()

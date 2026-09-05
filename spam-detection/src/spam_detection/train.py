"""Train and evaluate a simple text spam classifier."""

from argparse import ArgumentParser
from math import ceil
from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

DEFAULT_DATA_PATH = Path("data/raw/train.csv")


def train_and_evaluate(data_path: Path) -> None:
    """Load data, train the model, and print evaluation metrics."""
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

    X_train, X_test, y_train, y_test = train_test_split(
        df["text"], df["label"], test_size=test_size, random_state=42, stratify=df["label"]
    )

    vectorizer = CountVectorizer()
    model = MultinomialNB()
    model.fit(vectorizer.fit_transform(X_train), y_train)
    y_pred = model.predict(vectorizer.transform(X_test))

    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))


def main() -> None:
    parser = ArgumentParser(description="Train a spam-detection classifier.")
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA_PATH, help="CSV dataset path")
    args = parser.parse_args()
    train_and_evaluate(args.data)


if __name__ == "__main__":
    main()

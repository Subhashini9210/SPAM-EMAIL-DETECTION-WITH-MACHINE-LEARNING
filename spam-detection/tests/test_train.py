"""Tests for the training command's data validation and happy path."""

import pandas as pd
import pytest

from spam_detection.train import train_and_evaluate


def write_dataset(tmp_path, rows, columns=("text", "label")):
    """Create a CSV fixture and return its path."""
    path = tmp_path / "dataset.csv"
    pd.DataFrame(rows, columns=columns).to_csv(path, index=False)
    return path


def test_missing_required_columns_has_clear_error(tmp_path):
    path = write_dataset(tmp_path, [("Hello", "ham")], ("message", "category"))

    with pytest.raises(ValueError, match="label, text"):
        train_and_evaluate(path)


def test_each_class_needs_two_examples(tmp_path):
    path = write_dataset(
        tmp_path,
        [("Claim a prize", "spam"), ("Meeting tomorrow", "ham"), ("See you", "ham")],
    )

    with pytest.raises(ValueError, match="at least two examples"):
        train_and_evaluate(path)


def test_dataset_must_support_stratified_split(tmp_path):
    path = write_dataset(
        tmp_path,
        [("Prize offer", "spam"), ("Free reward", "spam"), ("Hello", "ham"), ("Thanks", "ham")],
    )

    with pytest.raises(ValueError, match="too small"):
        train_and_evaluate(path)


def test_train_and_evaluate_prints_metrics(tmp_path, capsys):
    rows = [(f"Claim reward number {index}", "spam") for index in range(5)]
    rows += [(f"Project meeting number {index}", "ham") for index in range(5)]
    path = write_dataset(tmp_path, rows)

    train_and_evaluate(path)

    output = capsys.readouterr().out
    assert "Accuracy:" in output
    assert "Confusion Matrix:" in output
    assert "Classification Report:" in output

# Spam Detection

Train and evaluate a multinomial Naive Bayes spam classifier from a CSV dataset.

## Project layout

```text
src/spam_detection/train.py  # training command
data/raw/train.csv           # local dataset (not committed)
outputs/figures/             # generated chart assets
tests/                       # automated tests
```

The dataset must contain `text` and `label` columns. Labels can be strings such as
`spam` and `ham`.

## Setup

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Train

```powershell
python src\spam_detection\train.py
```

To use a different dataset path:

```powershell
python src\spam_detection\train.py --data path\to\dataset.csv
```

The command prints accuracy, a confusion matrix, and a classification report.

# Spam Detection with Machine Learning

A reproducible SMS spam-classification project built with a bag-of-words
representation (unigrams and bigrams) and multinomial Naive Bayes. It trains a reusable
model, reports hold-out and cross-validation metrics, and saves a confusion-matrix chart.

## Project layout

```text
src/spam_detection/train.py  # training and prediction command
data/raw/train.csv           # local dataset (not committed)
outputs/models/              # generated model artifact (not committed)
outputs/figures/             # generated confusion-matrix chart
tests/                       # automated tests
```

The dataset must contain `text` and `label` columns. Labels can be strings such as `spam`
and `ham`. For portfolio-quality evaluation, download the [UCI SMS Spam Collection](https://archive.ics.uci.edu/dataset/228/sms+spam+collection), which contains 5,574 labelled SMS messages. The data remains local and is not committed.

## Setup

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Download the dataset

```powershell
python src\spam_detection\download_data.py
```

This downloads the UCI collection and converts it into `data/raw/train.csv` with the
required `text` and `label` columns.

## Train

```powershell
python src\spam_detection\train.py
```

To use a different dataset path:

```powershell
python src\spam_detection\train.py --data path\to\dataset.csv
```

The command saves `outputs/models/spam_classifier.joblib` and
`outputs/figures/confusion_matrix.png`, then prints hold-out accuracy, weighted F1,
five-fold cross-validation weighted F1, a confusion matrix, and a classification report.

## Predict a new message

After training, classify a message with the saved model:

```powershell
python src\spam_detection\train.py --predict "Congratulations! You won a free prize."
```

## Test

```powershell
python -m pytest -q
```

## Interview talking points

- **Why this model?** Multinomial Naive Bayes is a fast, interpretable baseline for sparse text features.
- **Why weighted F1?** It balances precision and recall while accounting for class imbalance.
- **Limitations:** A text-only model can miss novel spam patterns; production systems need monitoring, privacy controls, and periodic retraining.

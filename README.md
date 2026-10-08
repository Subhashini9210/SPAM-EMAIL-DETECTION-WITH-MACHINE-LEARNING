# 📧 Spam Email Detection Using Machine Learning

A machine learning-based text classification project that identifies whether a message is `Spam` or `Ham` (legitimate email/SMS). The project uses natural language processing, `CountVectorizer`, and a `Multinomial Naive Bayes` classifier to build a reliable baseline spam detector.

## Overview

Spam detection is a classic text classification problem. In this project, email and SMS text is converted into numerical features and passed to a supervised machine learning model that learns patterns associated with spam and non-spam messages.

This repository implements a complete training pipeline with:

- dataset validation
- text cleaning and preprocessing
- feature extraction using `CountVectorizer`
- model training using `MultinomialNB`
- evaluation using accuracy, F1-score, and confusion matrix
- model persistence using `joblib`
- automated tests with `pytest`
- CI using GitHub Actions

## Features

- Text preprocessing and cleaning
- Bag-of-words feature extraction using `CountVectorizer`
- Multinomial Naive Bayes classification
- Train/test split with stratification
- Cross-validation evaluation
- Confusion matrix generation
- Model persistence with `joblib`
- Automated testing with `pytest`
- CI workflow with GitHub Actions
- Command-line prediction support

## Project Structure

```text
SPAM-EMAIL-DETECTION-WITH-MACHINE-LEARNING/
├── AUTHORS.md
├── LICENSE
├── README.md
├── report.md
├── report.pdf
├── slides.md
├── slides.pdf
├── requirements.txt
├── .github/
│   └── workflows/
│       └── test.yml
├── spam-detection/
│   ├── README.md
│   ├── requirements.txt
│   ├── data/
│   │   └── raw/
│   │       └── train.csv
│   ├── outputs/
│   │   ├── models/
│   │   │   └── spam_classifier.joblib
│   │   └── figures/
│   │       └── confusion_matrix.png
│   ├── src/
│   │   └── spam_detection/
│   │       ├── __init__.py
│   │       ├── download_data.py
│   │       └── train.py
│   └── tests/
│       ├── conftest.py
│       └── test_train.py
```

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Joblib
- PyTest
- Git & GitHub
- GitHub Actions

## Dataset

The project is designed to work with a labeled text dataset containing:

- `text`: the message content
- `label`: the class label (`spam` or `ham`)

The reference dataset used for this project is the UCI SMS Spam Collection.

### Dataset Statistics

- Total messages: 5,574
- Spam messages: 747
- Ham messages: 4,827
- Split: 80/20 stratified train-test split

## Machine Learning Workflow

```text
Dataset
  ↓
Data validation
  ↓
Text cleaning
  ↓
Feature extraction
  ↓
CountVectorizer
  ↓
Train/test split
  ↓
Multinomial Naive Bayes
  ↓
Prediction
  ↓
Model evaluation
  ↓
Save model
  ↓
Spam/Ham classification
```

## Model Details

The project uses a pipeline combining:

- `CountVectorizer(stop_words="english", ngram_range=(1, 2))`
- `MultinomialNB(alpha=0.5)`

This is a strong baseline for text classification because it is fast, interpretable, and well-suited for sparse word-frequency features.

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/Subhashini9210/SPAM-EMAIL-DETECTION-WITH-MACHINE-LEARNING.git
cd SPAM-EMAIL-DETECTION-WITH-MACHINE-LEARNING
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

- macOS/Linux:

```bash
source .venv/bin/activate
```

- Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Download the Dataset

From the project folder:

```bash
python spam-detection/src/spam_detection/download_data.py
```

This downloads the UCI SMS Spam Collection and saves it as a CSV dataset in the expected raw data folder.

## Train the Model

```bash
cd spam-detection
python src/spam_detection/train.py
```

This script trains the spam classifier, saves the trained model, saves the confusion matrix plot, and prints evaluation metrics.

## Predict a New Message

```bash
cd spam-detection
python src/spam_detection/train.py --predict "Congratulations! You won a free prize."
```

## Run Tests

```bash
cd spam-detection
python -m pytest -q
```

## Model Evaluation

The trained model was evaluated on a stratified 80/20 train-test split.

## Results

### Model Performance

| Metric | Score |
|----------|---------|
| Accuracy | 97.86%|
| Precision | 98% |
| Recall | 98% |
| F1 Score | 98% |

### Confusion Matrix

Add an image of your confusion matrix here.

## Screenshots

### Home Page

screenshots/home.png

### Spam Detection Result

screenshots/result.png

## Live Demo

Coming Soon

## Future Enhancements

- Deep Learning based spam detection
- BERT Transformer model
- Real-time Gmail integration
- Multi-language spam detection
- Web application deployment
- Mobile application support

## Author

**Subhashini**

Machine Learning & Python Developer


### Confusion Matrix

| Actual \ Predicted | Ham | Spam |
|--------------------|-----|------|
| Ham                | 961 | 5    |
| Spam               | 9   | 140  |

These results indicate that the classifier performs very well and is suitable as a baseline solution for spam detection tasks.

## GitHub Actions CI

This repository includes a GitHub Actions workflow for automated validation.

The workflow runs tests on repository changes to ensure the project remains stable and reproducible.

## Usage Notes

This project is suitable for:

- learning spam classification with machine learning
- portfolio or academic projects
- baseline text classification experiments
- further extension to TF-IDF, Logistic Regression, SVM, or deep learning models

## Future Improvements

Potential enhancements for the project include:

- TF-IDF vectorization
- Hyperparameter tuning
- Improved preprocessing (stemming, lemmatization)
- Real email metadata analysis
- Deployment as a web app or API
- Advanced models such as Logistic Regression, SVM, or BERT

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgements

- UCI Machine Learning Repository for the SMS Spam Collection dataset
- Scikit-learn documentation and community examples

## Conclusion

This project demonstrates a robust machine learning workflow for spam detection using text classification, data validation, evaluation, and model persistence. It is a strong end-to-end example of a practical NLP classification solution and can serve as a solid foundation for further enhancement.

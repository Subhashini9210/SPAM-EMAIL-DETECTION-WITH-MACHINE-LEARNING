# 📧 Spam Email Detection Using Machine Learning

A machine learning-based text classification system that automatically classifies messages as **Spam** or **Ham (Legitimate)** using Natural Language Processing (NLP), CountVectorizer, and a Multinomial Naive Bayes classifier.

The project includes data validation, text feature extraction, model training, evaluation, model persistence, automated testing, and GitHub Actions CI.

---

## 📌 Project Overview

Spam messages are unwanted messages that may contain advertisements, scams, fraudulent offers, or other potentially harmful content.

This project uses **Machine Learning and Natural Language Processing (NLP)** to analyze the text of a message and classify it into one of two categories:

* 🚫 **Spam** — unwanted or suspicious message
* ✅ **Ham** — legitimate message

The system converts text into numerical features using **CountVectorizer** and uses a **Multinomial Naive Bayes** classifier to make the final prediction.

---

## 🎯 Project Objectives

The main objectives of this project are:

* Detect spam messages automatically.
* Apply Natural Language Processing techniques to text data.
* Convert text into numerical features using CountVectorizer.
* Train a machine learning classification model.
* Evaluate the model using standard classification metrics.
* Save the trained model for future predictions.
* Provide a command-line prediction interface.
* Implement automated testing using PyTest.
* Use GitHub Actions for Continuous Integration.

---

## ✨ Key Features

* 📧 Spam/Ham text classification
* 🧠 Natural Language Processing
* 🔤 Text preprocessing
* 📊 CountVectorizer feature extraction
* 🔢 Unigram and bigram features
* 🤖 Multinomial Naive Bayes classifier
* 📈 Accuracy and F1-score evaluation
* 🔍 Precision and recall through classification report
* 📉 Confusion matrix generation
* 🔄 5-fold cross-validation when supported by the dataset
* 💾 Model persistence using Joblib
* 🧪 Automated testing using PyTest
* ⚙️ GitHub Actions CI
* 💻 Command-line prediction

---

## 🛠️ Technologies Used

| Technology              | Purpose                     |
| ----------------------- | --------------------------- |
| Python                  | Main programming language   |
| Pandas                  | Data loading and processing |
| NumPy                   | Numerical operations        |
| Scikit-learn            | Machine learning and NLP    |
| CountVectorizer         | Text feature extraction     |
| Multinomial Naive Bayes | Classification              |
| Joblib                  | Model persistence           |
| Matplotlib              | Visualization               |
| Seaborn                 | Data visualization support  |
| PyTest                  | Automated testing           |
| Git & GitHub            | Version control             |
| GitHub Actions          | Continuous Integration      |

---

## 🧠 Machine Learning Workflow

The project follows this workflow:

```text
Dataset
   ↓
Data Validation
   ↓
Text Cleaning
   ↓
Feature Extraction
   ↓
CountVectorizer
   ↓
Train/Test Split
   ↓
Multinomial Naive Bayes
   ↓
Model Prediction
   ↓
Model Evaluation
   ↓
Save Trained Model
   ↓
Spam / Ham Prediction
```

---

## 📂 Dataset

The project is designed to work with a labelled text dataset containing:

* `text` — message content
* `label` — classification label

The original project documentation uses the **UCI SMS Spam Collection** as the reference dataset.

The dataset contains:

* **5,574 messages**
* **747 spam messages**
* **4,827 ham messages**

The training program validates that the required `text` and `label` columns are present before training.

---

## 🔤 Text Processing and Feature Extraction

Text data cannot be directly provided to a traditional machine learning classifier.

Therefore, the project converts the text into numerical features.

### CountVectorizer

The project uses:

```python
CountVectorizer(
    stop_words="english",
    ngram_range=(1, 2)
)
```

This extracts:

* **Unigrams** — individual words
* **Bigrams** — pairs of consecutive words

For example:

```text
free prize winner
```

can be represented using features such as:

```text
free
prize
winner
free prize
prize winner
```

These numerical features are then passed to the machine learning classifier.

---

## 🤖 Machine Learning Model

### Multinomial Naive Bayes

The project uses:

```python
MultinomialNB(alpha=0.5)
```

Multinomial Naive Bayes is well suited for text classification because it works effectively with discrete word-frequency features.

### Why Naive Bayes?

* Fast training
* Fast prediction
* Suitable for text classification
* Computationally efficient
* Works well with bag-of-words features

---

## 📊 Model Evaluation

The model is evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* Classification Report
* Confusion Matrix
* Cross-validation weighted F1 score

The project uses an **80/20 stratified train-test split** and performs cross-validation on the available labelled data.

### Performance

> ⚠️ Replace the values below with the actual values generated by your latest training run. Do not use example numbers.

| Metric   |           Result |
| -------- | ---------------: |
| Accuracy | **YOUR_VALUE%_** |

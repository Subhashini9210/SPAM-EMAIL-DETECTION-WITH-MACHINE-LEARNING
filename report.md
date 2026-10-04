# Final Year Project Report — Spam Email Detection

## Title
Spam Email / SMS Detection using Machine Learning

## Author
Subhashini (@Subhashini9210)

**Date:** September 2026

---

## Abstract

This project implements a machine learning-based spam detection system for SMS messages using the UCI SMS Spam Collection dataset. The system employs a Multinomial Naive Bayes classifier with bag-of-words text features to classify incoming messages as spam or ham.

The project includes dataset validation, model training, evaluation, confusion-matrix visualization, and persistence of the trained model. It is designed to be easily reproducible and includes automated tests and CI configuration for verification.

---

## 1. Introduction

### Problem Statement
Email and SMS spam remains a significant challenge in digital communication, consuming bandwidth, compromising user experience, and potentially facilitating phishing and malware attacks. Manual filtering is impractical at scale, which motivates automated classification using machine learning.

### Motivation and Applications
- **User Experience:** Reduces clutter in inboxes and messaging applications
- **Security:** Helps prevent phishing attacks and credential theft
- **Business Efficiency:** Reduces server load and bandwidth consumption
- **Educational Value:** Demonstrates practical application of NLP and machine learning techniques

---

## 2. Related Work

Classic spam detection approaches include:
- **Rule-based filters:** Early systems relied on keyword matching and blacklists (limitations: high false positives, easily evaded)
- **Naive Bayes classifiers:** Probabilistic approach using bag-of-words representation (popular, fast, interpretable)
- **Support Vector Machines (SVM):** Effective for high-dimensional text features
- **Deep Learning:** Neural networks and transformers for complex pattern recognition (recent work)

The Multinomial Naive Bayes approach is chosen for this project due to its simplicity, interpretability, and proven effectiveness on text classification tasks in academic literature.

---

## 3. Dataset

### Source
UCI Machine Learning Repository: [SMS Spam Collection Dataset](https://archive.ics.uci.edu/dataset/228/sms+spam+collection)

### Dataset Characteristics
- **Total Examples:** 5,574 labelled SMS messages
- **Classes:** 2 (Spam: 747, Ham: 4,827)
- **Class Imbalance:** ~13% spam, ~87% legitimate messages
- **Features:** Raw text messages (variable length)

### Preprocessing Steps
1. **Data Loading:** Download and parse UCI tab-delimited format
2. **Validation:** Ensure all rows contain `text` and `label` columns
3. **Cleaning:** Remove null values, strip whitespace
4. **Filtering:** Exclude empty text messages
5. **Stratification:** Maintain class distribution in train-test splits

---

## 4. Methodology

### Feature Extraction
- **Vectorizer:** scikit-learn `CountVectorizer`
- **N-grams:** Unigrams (single words) and bigrams (word pairs)
- **Stop Words:** English stop words removed to focus on meaningful tokens
- **Representation:** Bag-of-words (term frequency counts)

### Model
- **Algorithm:** Multinomial Naive Bayes
- **Hyperparameter:** Alpha smoothing = 0.5 (Laplace smoothing variant)
- **Rationale:** Fast, interpretable, suitable for sparse text features

### Train-Test Split
- **Test Size:** 20% (stratified)
- **Train Size:** 80%
- **Stratification:** Maintains class distribution in both splits
- **Random State:** 42 (reproducibility)

### Cross-Validation
- **Method:** 5-fold stratified cross-validation
- **Metric:** Weighted F1-score (accounts for class imbalance)
- **Purpose:** Estimate generalization performance

---

## 5. Experiments

### Environment
- **Python Version:** 3.10, 3.11
- **Dependencies:** scikit-learn, pandas, joblib, matplotlib
- **Platform:** Linux (GitHub Actions CI/CD)

### Experiment Commands
```bash
# Step 1: Download and prepare dataset
cd spam-detection
python src/spam_detection/download_data.py

# Step 2: Train model and generate outputs
python src/spam_detection/train.py

# Step 3: Run test suite
cd ..
python -m pytest -q
```

### Hyperparameters Explored
- Alpha (smoothing parameter): 0.5 (selected)
- N-gram range: (1, 2) — unigrams and bigrams (selected)
- Stop words: English (selected)

---

## 6. Results

Important: populate these values by running the project locally before final submission:

```bash
cd spam-detection
python src/spam_detection/train.py
```

### Hold-Out Set Metrics (20% Test Set)
- **Accuracy:** [Run the model and insert the actual value]
- **Weighted F1-Score:** [Run the model and insert the actual value]
- **Precision (per class):** [Insert values from the classification report]

### Cross-Validation Metrics
- **5-Fold Cross-Validation Weighted F1:** [Run the model and insert the actual value]

### Confusion Matrix
Generated figure saved to: `spam-detection/outputs/figures/confusion_matrix.png`

**Interpretation:**
- True Negatives (TN): Legitimate messages correctly classified
- False Positives (FP): Legitimate messages misclassified as spam
- False Negatives (FN): Spam messages misclassified as legitimate
- True Positives (TP): Spam messages correctly classified

### Classification Report
```text
[Insert the actual output from: python src/spam_detection/train.py]
```

---

## 7. Limitations and Future Work

### Limitations
1. **Text-Only Model:** Ignores sender reputation, IP reputation, email headers
2. **Limited Feature Engineering:** Bag-of-words discards word order and context
3. **Class Imbalance:** 87% of data is legitimate; minority class underrepresented
4. **Dataset Age:** UCI collection is historical; spam patterns evolve
5. **Language:** Primarily English; generalization to other languages unclear
6. **No Temporal Dynamics:** Treats each message independently

### Suggested Improvements
1. **Feature Engineering:** TF-IDF weighting, word embeddings (Word2Vec, GloVe)
2. **Advanced Models:** Logistic Regression, SVM, Gradient Boosting, Neural Networks
3. **Ensemble Methods:** Combine multiple classifiers for robustness
4. **Cost-Sensitive Learning:** Assign higher cost to false positives
5. **Active Learning:** Continuously retrain on new labelled examples
6. **Deployment:** API wrapper for real-time classification, monitoring pipeline

---

## 8. Conclusion

This project demonstrates a practical machine learning approach to SMS spam detection using Multinomial Naive Bayes on the UCI SMS Spam Collection. The approach is fast, interpretable, and well-suited as a baseline for text classification. The workflow includes validation, feature extraction, training, evaluation, and deployment-ready model persistence.

---

## 9. References

1. UCI Machine Learning Repository - SMS Spam Collection Dataset  
   https://archive.ics.uci.edu/dataset/228/sms+spam+collection

2. scikit-learn Documentation - Text Feature Extraction  
   https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction

3. scikit-learn Documentation - Naive Bayes  
   https://scikit-learn.org/stable/modules/naive_bayes.html

4. Bird, S., Klein, E., & Loper, E. (2009). "Natural Language Processing with Python"  
   O'Reilly Media, Inc.

5. Spam Detection Survey: Recent Approaches and Challenges  
   (Use a relevant conference or survey paper as required by your university)

---

**To submit:** Convert this Markdown to PDF using:
```bash
pandoc report.md -o report.pdf
```

Then commit `report.pdf` to the repository and verify it renders correctly on GitHub.

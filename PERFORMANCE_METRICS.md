# 📊 Performance Metrics - Spam Email Detection Model

## Model Performance Summary

### Evaluation Metrics

| Metric | Value | Interpretation |
|--------|-------|-----------------|
| **Accuracy** | _TBD_ | Overall correctness of predictions |
| **Precision** | _TBD_ | True positives / (True positives + False positives) |
| **Recall** | _TBD_ | True positives / (True positives + False negatives) |
| **F1 Score (Weighted)** | _TBD_ | Harmonic mean of precision and recall |
| **Cross-Validation F1 (5-fold)** | _TBD_ | Model robustness across different data splits |

---

## Dataset Information

- **Dataset**: UCI SMS Spam Collection
- **Total Messages**: 5,574
- **Spam Messages**: 747 (~13.4%)
- **Ham Messages**: 4,827 (~86.6%)
- **Train/Test Split**: 80/20 (stratified)

---

## Model Configuration

### Text Processing
- **Vectorizer**: CountVectorizer
- **Stop Words**: English
- **N-gram Range**: (1, 2) - Unigrams and Bigrams
- **Max Features**: Unlimited

### Classification Algorithm
- **Model**: Multinomial Naive Bayes
- **Alpha (Smoothing)**: 0.5
- **Training Algorithm**: Document frequency-based

---

## How to Generate Metrics

1. **Download the dataset**:
   ```bash
   python spam-detection/src/spam_detection/download_data.py
   ```

2. **Run the training script**:
   ```bash
   python spam-detection/src/spam_detection/train.py
   ```

3. **Generate and save metrics**:
   ```bash
   python spam-detection/src/spam_detection/generate_metrics.py
   ```

---

## Evaluation Methodology

### Train-Test Split
- **Method**: Stratified train-test split
- **Ratio**: 80% training, 20% testing
- **Randomization**: Random seed 42 for reproducibility
- **Purpose**: Maintains class distribution in both sets

### Cross-Validation
- **Method**: K-fold cross-validation
- **Folds**: 5 (or minimum class count if less)
- **Scoring**: Weighted F1-score
- **Purpose**: Assesses model generalization

### Confusion Matrix
Shows the breakdown of:
- **True Positives (TP)**: Correctly identified spam
- **True Negatives (TN)**: Correctly identified ham
- **False Positives (FP)**: Ham incorrectly classified as spam
- **False Negatives (FN)**: Spam incorrectly classified as ham

---

## Performance Expectations

Based on the UCI SMS Spam Collection dataset and Multinomial Naive Bayes:

- **Expected Accuracy**: 95-98%
- **Expected Precision**: 95-99% (very few false spam alerts)
- **Expected Recall**: 95-99% (catches most spam)
- **Expected F1 Score**: 0.95-0.98

*Note: Actual results may vary based on data preprocessing and feature engineering.*

---

## Model Artifacts

- **Model File**: `spam-detection/outputs/models/spam_classifier.joblib`
- **Vectorizer**: Embedded in the joblib pipeline
- **Confusion Matrix Chart**: `spam-detection/outputs/figures/confusion_matrix.png`

---

## Next Steps

1. Run the training pipeline to generate actual metrics
2. Compare results against expected performance
3. Investigate any significant deviations
4. Consider hyperparameter tuning if needed
5. Deploy model to Django application with confidence metrics


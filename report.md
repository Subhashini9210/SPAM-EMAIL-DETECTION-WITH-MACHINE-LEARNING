# Final Year Project Report — Spam Email Detection

## Title
Spam Email / SMS Detection using Machine Learning

## Author
Subhashini (@Subhashini9210)

## Abstract
(Brief summary of the problem, approach, and results — 150–300 words.)

## 1. Introduction
- Problem statement
- Motivation and applications

## 2. Related Work
- Brief review of classic spam detection approaches and recent work

## 3. Dataset
- Describe the UCI SMS Spam Collection (source link)
- Number of examples, classes (spam/ham)
- Any preprocessing steps

## 4. Methodology
- Feature extraction (CountVectorizer with unigrams+bigrams)
- Model: Multinomial Naive Bayes (alpha=0.5)
- Train/test split, stratification details
- Cross-validation strategy

## 5. Experiments
- Exact code/commands used to run experiments (include the command to run train.py)
- Hyperparameters tried (if any)
- Any hardware or environment details

## 6. Results
- Hold-out accuracy, weighted F1, cross-validation F1
- Confusion matrix (include the figure path: outputs/figures/confusion_matrix.png)
- Discussion of false positives/false negatives

## 7. Limitations and Future Work
- Data limitations, model limitations
- Suggestions: try TF-IDF, more complex models, deployment considerations

## 8. Conclusion
- Summary of findings

## 9. References
- UCI SMS Spam Collection: https://archive.ics.uci.edu/dataset/228/sms+spam+collection
- Scikit-learn docs


---

Instructions: convert this markdown to PDF for submission (e.g., using pandoc or GitHub rendering). Add your student details in the Author section and include supervisor details.

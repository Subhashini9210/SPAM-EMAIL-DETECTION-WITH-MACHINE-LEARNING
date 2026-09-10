# Spam Email / SMS Detection with Machine Learning

A machine learning-based spam detection system using Multinomial Naive Bayes and bag-of-words text features on the UCI SMS Spam Collection dataset.

## 📊 Quick Overview

- **Model:** Multinomial Naive Bayes with unigrams + bigrams
- **Dataset:** UCI SMS Spam Collection (5,574 messages)
- **Accuracy:** [Run train.py to see results]
- **Status:** ✅ Fully tested with CI/CD pipeline

## 🚀 Quick Start

```bash
# Clone and setup
git clone https://github.com/Subhashini9210/SPAM-EMAIL-DETECTION-WITH-MACHINE-LEARNING.git
cd SPAM-EMAIL-DETECTION-WITH-MACHINE-LEARNING

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
pip install -r spam-detection/requirements.txt

# Download data and train model
cd spam-detection
python src/spam_detection/download_data.py
python src/spam_detection/train.py

# Run tests
cd ..
python -m pytest -q

# Make a prediction
cd spam-detection
python src/spam_detection/train.py --predict "Congratulations! You won a free prize."
```

## 📁 Project Structure

```
.
├── spam-detection/              # Main ML project
│   ├── src/spam_detection/
│   │   ├── train.py            # Train and predict CLI
│   │   └── download_data.py    # Download UCI dataset
│   ├── tests/
│   │   ├── test_train.py       # Unit tests
│   │   └── conftest.py         # Pytest config
│   ├── data/raw/               # Downloaded dataset (git-ignored)
│   ├── outputs/                # Generated models & figures (git-ignored)
│   └── requirements.txt        # ML dependencies
├── AUTHORS.md                   # Student submission metadata
├── report.md                    # Full project report (convert to PDF)
├── slides.md                    # Presentation outline (convert to PDF)
├── SUBMISSION_CHECKLIST.md     # Pre-submission verification
├── LICENSE                      # MIT License
├── README.md                    # This file
└── requirements.txt             # Root dependencies
```

## 🔧 How It Works

### 1. Data Download
Downloads 5,574 labelled SMS messages from UCI:
- **Spam:** 747 messages (13%)
- **Ham (Legitimate):** 4,827 messages (87%)

### 2. Preprocessing
- Stop word removal (English)
- Tokenization and normalization
- Stratified train-test split (80/20)

### 3. Model Training
- **Vectorization:** CountVectorizer with unigrams & bigrams
- **Classifier:** Multinomial Naive Bayes (alpha=0.5)
- **Evaluation:** Weighted F1-score with 5-fold cross-validation

### 4. Outputs Generated
- `outputs/models/spam_classifier.joblib` — Trained model
- `outputs/figures/confusion_matrix.png` — Confusion matrix plot

## 📊 Results

Run the training to see:
- Hold-out accuracy
- Weighted F1-score
- 5-fold cross-validation metrics
- Confusion matrix visualization
- Classification report (precision, recall, F1 per class)

## 🧪 Testing

All tests are automated via GitHub Actions CI/CD:

```bash
python -m pytest -q spam-detection/tests/
```

Tests cover:
- Data validation and error handling
- Model training and evaluation
- Prediction on new messages
- UCI dataset parsing

## 📖 Submission Files

- **`report.md`** — Full project report (convert to `report.pdf`)
- **`slides.md`** — 10-slide presentation outline (convert to `slides.pdf`)
- **`AUTHORS.md`** — Student metadata (fill in your details)
- **`SUBMISSION_CHECKLIST.md`** — Pre-submission verification checklist

## 📝 For Final Submission

1. **Fill in AUTHORS.md** with your:
   - Full name
   - Student/Roll number
   - Supervisor name
   - Institution/Department
   - Contact email

2. **Generate PDFs:**
   ```bash
   # Report
   pandoc report.md -o report.pdf
   
   # Slides (use your preferred tool: Marp, Reveal.js, PowerPoint, etc.)
   ```

3. **Run experiments** to populate metrics in report.md

4. **Verify submission checklist** before submitting to your university

## 🔗 References

- [UCI SMS Spam Collection](https://archive.ics.uci.edu/dataset/228/sms+spam+collection)
- [scikit-learn Text Feature Extraction](https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction)
- [scikit-learn Naive Bayes](https://scikit-learn.org/stable/modules/naive_bayes.html)

## 📄 License

MIT License — See [LICENSE](LICENSE) file for details

## ✅ CI/CD Status

GitHub Actions automatically runs tests on every push. View workflow status: [Actions](https://github.com/Subhashini9210/SPAM-EMAIL-DETECTION-WITH-MACHINE-LEARNING/actions)

# Spam Email / SMS Detection with Machine Learning

 
A robust machine learning system for detecting spam SMS and email messages using Natural Language Processing (NLP), CountVectorizer feature extraction, and a Multinomial Naive Bayes classifier.
 
## 🚀 Key Features


✅ SMS Spam Detection
 
✅ NLP-Based Text Preprocessing

✅ Bag-of-Words Feature Engineering

✅ Multinomial Naive Bayes Classification

✅ Cross Validation and Model Evaluation

✅ Automated Testing with PyTest

✅ GitHub Actions CI/CD Pipeline

✅ Command-Line Prediction Interface

✅ Model Persistence Using Joblib

---
## 📊 Quick Overview

| Attribute | Details |
|------------|------------|
| Model | Multinomial Naive Bayes |
| Feature Extraction | CountVectorizer (Unigrams + Bigrams) |
| Dataset | UCI SMS Spam Collection |
| Dataset Size | 5,574 Messages |
| Spam Messages | 747 |
| Ham Messages | 4,827 |
| Testing | PyTest |
| CI/CD | GitHub Actions |
| Outputs | Trained Model, Metrics, Confusion Matrix |
---
## 🎯 Project Objective
The goal of this project is to build a machine learning model capable of automatically classifying SMS and email messages as:
- **Spam** 🚫
- **Ham (Legitimate Message)** ✅
The system applies NLP preprocessing and machine learning classification techniques to detect unwanted or fraudulent messages effectively.
---
## 🧠 Machine Learning Workflow
### Step 1: Data Collection
The project uses the UCI SMS Spam Collection dataset containing 5,574 labelled messages.
| Class | Count |
|---------|---------|
| Spam | 747 |
| Ham | 4,827 |
---
### Step 2: Text Preprocessing
The raw text undergoes preprocessing before training.

Tasks performed:

- Convert text to lowercase
- Remove stop words
- Tokenisation
- Normalisation
- Text cleaning
Example:

**Original Message**

```text
Congratulations! You have won a FREE prize!
```

**Processed Text**
 
```text
congratulations won free prize
```
 
---
 
### Step 3: Feature Extraction
 
The cleaned text is converted into numerical features using:
 
```python
CountVectorizer()
```
 
Using:
 
- Unigrams
- Bigrams
  
Example:

 
```text
free prize winner

Becomes a numerical vector that machine learning algorithms can process.
 
### Step 4: Model Training
 
Classifier used:
 
```python
MultinomialNB(alpha=0.5)

Reasons for choosing Naive Bayes:
 
- Fast training
- Efficient prediction
- Excellent performance on text classification problems
- Low computational cost
 
### Step 5: Model Evaluation
 
Evaluation metrics include:
 
- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Cross Validation Score
 
The trained model is validated using:
 
```text
5-Fold Cross Validation
 
## 📁 Project Structure

```text
SPAM-EMAIL-DETECTION-WITH-MACHINE-LEARNING/
│
├── .github/
│ └── workflows/
│
├── spam-detection/
│ ├── src/spam_detection/
│ │ ├── train.py
│ │ └── download_data.py
│ │
│ ├── tests/
│ │ ├── test_train.py
│ │ └── conftest.py
│ │
│ ├── data/raw/
│ ├── outputs/
│ └── requirements.txt
│
├── AUTHORS.md
├── report.md
├── slides.md
├── SUBMISSION_CHECKLIST.md
├── LICENSE
├── README.md
└── requirements.txt
```
---

## ⚙️ Installation
 
### Clone Repository
 
```bash
git clone https://github.com/Subhashini9210/SPAM-EMAIL-DETECTION-WITH-MACHINE-LEARNING.git
 
cd SPAM-EMAIL-DETECTION-WITH-MACHINE-LEARNING
```
 
### Create Virtual Environment
 
Linux/macOS:
 
```bash
python3 -m venv .venv
 
source .venv/bin/activate
```

Windows PowerShell:
 
```powershell
python -m venv .venv
 
.\.venv\Scripts\Activate.ps1
```
 
### Install Dependencies
 
```bash
pip install -r requirements.txt
 
pip install -r spam-detection/requirements.txt
```

---
 
## ▶️ Running the Project
 
### Download Dataset
 
```bash
cd spam-detection
 
python src/spam_detection/download_data.py
 
### Train Model
 
```bash
python src/spam_detection/train.py
 
 
## 🔮 Make Predictions
 
Example:
 
```bash
python src/spam_detection/train.py --predict "Congratulations! You won a free prize."
```
 
Expected Output:
 
```text
Prediction: Spam

Another Example:
 
Input:
 
```text
Hi, are we meeting at 5 PM today?
 
Output:
 
```text
Prediction: Ham
```
---
## 📈 Results
After training, the system generates:

- Hold-Out Accuracy
- Precision Score
- Recall Score
- F1 Score
- Classification Report
- Cross Validation Results
- Confusion Matrix
 
### Performance Metrics

| Metric | Score |
|----------|----------|
| Accuracy | Generated After Training |
| Precision | Generated After Training |
| Recall | Generated After Training |
| F1 Score | Generated After Training |
 
Replace the above values with the actual results from your training run.
 
---
 
## 📸 Screenshots
 
### Confusion Matrix
 
Add:
```text
Figure_1.png
```
 
### Model Performance
 
Add:

```text
Figure_2.png
```

---
 
## 🧪 Testing
 
All tests are automated using PyTest and GitHub Actions.
 
Run tests:
 
```bash
python -m pytest -q spam-detection/tests/
```
 
Tests cover:
 
- Data Validation
- Dataset Parsing
- Error Handling
- Model Training
- Model Evaluation
- Prediction Functionality
 336
  ---
## 💼 Skills Demonstrated
 
This project demonstrates:
 
- Python Programming
- Machine Learning
- Natural Language Processing (NLP)
- Text Classification
- Feature Engineering
- Data Cleaning and Preprocessing
- Model Evaluation
- Cross Validation
- Software Testing
- GitHub Actions CI/CD
- Version Control with Git and GitHub
 
---

## 📖 Submission Files
 
| File | Description |
|--------|--------|
| report.md | Complete project report |
| slides.md | Presentation slides outline |
| AUTHORS.md | Author information |
| SUBMISSION_CHECKLIST.md | Submission verification checklist |
 
---
 
## 📝 Author

### Subhashini Vippala
 
Bachelor of Technology (B.Tech)
 
Artificial Intelligence and Machine Learning
 
J. Ramu NRI Institute of Technology
 
GitHub:
 
https://github.com/Subhashini9210
 
Project:

Spam Email / SMS Detection Using Machine Learning
 
## 🔮 Future Enhancements

Future versions may include:
 
- Logistic Regression Classifier
- Support Vector Machine (SVM)
- Random Forest Classifier
- Streamlit Web Application
- FastAPI Deployment
- Deep Learning with LSTM Networks
- Transformer-Based Models (BERT)
- Real-Time Spam Detection API
- Email Integration Support
 
---
 
## 🔗 References
 
1. UCI SMS Spam Collection Dataset

https://archive.ics.uci.edu/dataset/228/sms+spam+collection
 
2. Scikit-Learn Text Feature Extraction
 
https://scikit-learn.org/stable/modules/feature_extraction.html
 
3. Scikit-Learn Naive Bayes

https://scikit-learn.org/stable/modules/naive_bayes.html
---
 
## 📄 License

 
This project is licensed under the MIT License.


See the LICENSE file for details.
 ---
 
## ✅ CI/CD Status
 
GitHub Actions automatically runs tests on every push and pull request. 

The workflow ensures:
 
 - Automated Testing
- Dependency Validation
- Continuous Integration
- Project Stability
 
View workflow status from the Actions tab of the repository.


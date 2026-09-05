# Spam Email Detection - Setup & Execution Guide

This document provides complete instructions for setting up and running the Spam Email Detection project.

## Quick Start (Automated)

### Option 1: Using the Setup Script (Recommended)

The easiest way to set up and run everything is using the provided bash script:

```bash
# Make the script executable
chmod +x setup_and_run.sh

# Run the script
./setup_and_run.sh
```

This script will:
1. ✅ Install all root-level dependencies
2. ✅ Run unit tests
3. ✅ Execute the main model (if Tesla.csv exists)
4. ✅ Setup spam-detection subdirectory
5. ✅ Download the UCI SMS dataset
6. ✅ Train the spam classification model
7. ✅ Run all tests
8. ✅ Test predictions with sample messages

### Option 2: Using Windows Batch Script

On Windows, simply run:

```cmd
setup_and_run.bat
```

This performs the same steps as the bash script but for Windows PowerShell/CMD.

### Option 3: Manual Step-by-Step Execution

If you prefer to run each step manually:

#### Step 1: Clone and Navigate
```bash
git clone https://github.com/Subhashini9210/SPAM-EMAIL-DETECTION-WITH-MACHINE-LEARNING.git
cd SPAM-EMAIL-DETECTION-WITH-MACHINE-LEARNING
```

#### Step 2: Install Root-Level Dependencies
```bash
pip install -r requirements.txt
```

**Dependencies installed:**
- numpy==1.26.4
- pandas==2.0.0
- matplotlib==3.7.0
- seaborn==0.13.0
- scikit-learn==1.3.0
- xgboost==2.0.0
- pytest==7.4.0

#### Step 3: Run Unit Tests
```bash
python test_spam_detection.py
```

**Tests covered:**
- ✓ All imports successful
- ✓ All models instantiated successfully
- ✓ Train-test split works correctly
- ✓ StandardScaler works correctly
- ✓ Model training works correctly
- ✓ Model prediction works correctly
- ✓ Model evaluation works correctly
- ✓ CSV loading works correctly

#### Step 4: Run Main Model
```bash
python project
```

**Note:** This runs a Tesla stock price prediction model (not the main spam detection).

#### Step 5: Setup Spam-Detection Subdirectory
```bash
cd spam-detection
pip install -r requirements.txt
```

**Spam-detection dependencies:**
- pandas>=2.2,<3.1
- scikit-learn>=1.5,<1.9
- joblib>=1.3,<2
- matplotlib>=3.8,<3.11
- pytest>=8,<9

#### Step 6: Download Dataset
```bash
python src/spam_detection/download_data.py
```

This downloads the **UCI SMS Spam Collection** dataset:
- 5,574 labeled SMS messages
- Binary classification (spam/ham)
- Saved to `data/raw/train.csv`

#### Step 7: Train the Model
```bash
python src/spam_detection/train.py
```

**Output generated:**
- `outputs/models/spam_classifier.joblib` — Trained model artifact
- `outputs/figures/confusion_matrix.png` — Confusion matrix visualization
- Console output with:
  - Hold-out accuracy
  - Weighted F1 score
  - 5-fold cross-validation metrics
  - Classification report

#### Step 8: Make Predictions on New Messages
```bash
# Test with a spam message
python src/spam_detection/train.py --predict "Congratulations! You won a free prize."

# Test with a legitimate message
python src/spam_detection/train.py --predict "Hi, how are you doing today?"
```

#### Step 9: Run Tests
```bash
python -m pytest -q
```

## Project Structure

```
SPAM-EMAIL-DETECTION-WITH-MACHINE-LEARNING/
│
├── setup_and_run.sh                   # Automated setup script (Linux/Mac)
├── setup_and_run.bat                  # Automated setup script (Windows)
├── SETUP_INSTRUCTIONS.md              # This file
├── requirements.txt                   # Root-level dependencies
├── README.md                          # Project overview
│
├── project                            # Main model implementation (stock price)
├── test_spam_detection.py             # Unit tests
├── test_stock_price_prediction.py     # Stock price tests
│
└── spam-detection/                    # Production-ready spam detection
    ├── README.md                      # Spam-detection documentation
    ├── requirements.txt               # Spam-detection dependencies
    ├── src/
    │   └── spam_detection/
    │       ├── train.py               # Training & prediction script
    │       └── download_data.py       # Dataset downloader
    ├── data/
    │   └── raw/
    │       └── train.csv              # Dataset (auto-downloaded)
    ├── outputs/
    │   ├── models/
    │   │   └── spam_classifier.joblib # Trained model
    │   └── figures/
    │       └── confusion_matrix.png   # Confusion matrix chart
    └── tests/                         # Unit tests for spam detection
```

## Model Information

### Algorithm
**Multinomial Naive Bayes** with bag-of-words text representation:
- Unigrams and bigrams for text feature extraction
- Fast and interpretable baseline for sparse text features
- Good performance on imbalanced datasets

### Evaluation Metrics
The model is evaluated using:
- **Accuracy** — Overall correctness
- **Precision** — True positives / (True positives + False positives)
- **Recall** — True positives / (True positives + False negatives)
- **F1-Score** — Harmonic mean of precision and recall (weighted for class imbalance)
- **Confusion Matrix** — Visual representation of prediction errors
- **5-Fold Cross-Validation** — Robust performance estimation

### Dataset
- **Source:** UCI SMS Spam Collection
- **Size:** 5,574 labeled SMS messages
- **Classes:** 2 (Spam / Ham)
- **Features:** Text-based (converted to TF-IDF vectors)

## Troubleshooting

### Issue: `ModuleNotFoundError` when running scripts
**Solution:** Make sure all dependencies are installed:
```bash
pip install -r requirements.txt
cd spam-detection && pip install -r requirements.txt
```

### Issue: Dataset not found
**Solution:** Download the dataset explicitly:
```bash
cd spam-detection
python src/spam_detection/download_data.py
```

### Issue: Permission denied on setup_and_run.sh
**Solution:** Make the script executable:
```bash
chmod +x setup_and_run.sh
```

### Issue: XGBoost import errors
**Solution:** XGBoost is optional. The script handles its absence gracefully. Install if needed:
```bash
pip install xgboost==2.0.0
```

### Issue: Tests fail on Windows
**Solution:** Use the Windows batch script or run commands in PowerShell:
```powershell
python -m pytest -q
```

## Expected Output

After running all steps, you should see:
```
========================================
SPAM EMAIL DETECTION - Setup & Run
========================================

📦 Step 1: Installing root-level dependencies...
✓ Root dependencies installed

🧪 Step 2: Running unit tests...
✓ All tests passed!

🤖 Step 3: Running main model...
✓ Main model executed

📂 Step 4: Setting up spam-detection subdirectory...
✓ Model training completed

📊 Hold-out Accuracy: 0.9745
📊 Weighted F1 Score: 0.9745
📊 5-Fold CV Weighted F1: 0.9689

✅ All steps completed successfully!
```

## Next Steps

1. **Experiment with predictions:** Test the model with your own messages
2. **Analyze the confusion matrix:** Review `outputs/figures/confusion_matrix.png`
3. **Tune hyperparameters:** Modify `src/spam_detection/train.py` to adjust model settings
4. **Deploy the model:** Use the saved `spam_classifier.joblib` in production
5. **Monitor performance:** Regularly retrain on new data to maintain accuracy

## Questions & Support

For issues or questions:
1. Check the troubleshooting section above
2. Review `spam-detection/README.md` for detailed documentation
3. Examine the test files for usage examples
4. Check the model source code in `src/spam_detection/train.py`

---

**Happy spam detecting! 🚀**

#!/bin/bash

# Spam Email Detection - Setup and Execution Script
# This script automates the installation and execution of the spam detection project

set -e  # Exit on error

echo "========================================"
echo "SPAM EMAIL DETECTION - Setup & Run"
echo "========================================"
echo ""

# Step 1: Install root-level dependencies
echo "📦 Step 1: Installing root-level dependencies..."
pip install -r requirements.txt
echo "✓ Root dependencies installed"
echo ""

# Step 2: Run unit tests
echo "🧪 Step 2: Running unit tests..."
python test_spam_detection.py
echo "✓ Unit tests completed"
echo ""

# Step 3: Run main model (if Tesla.csv exists)
echo "🤖 Step 3: Running main model..."
if [ -f "Tesla.csv" ]; then
    python project
    echo "✓ Main model executed"
else
    echo "⚠️  Tesla.csv not found - skipping main model execution"
fi
echo ""

# Step 4: Setup and run spam-detection subdirectory
echo "📂 Step 4: Setting up spam-detection subdirectory..."
cd spam-detection

echo "📥 Installing spam-detection dependencies..."
pip install -r requirements.txt
echo "✓ Spam-detection dependencies installed"
echo ""

echo "📊 Downloading UCI SMS Spam Collection dataset..."
python src/spam_detection/download_data.py
echo "✓ Dataset downloaded"
echo ""

echo "🔄 Training spam detection model..."
python src/spam_detection/train.py
echo "✓ Model training completed"
echo ""

echo "🧪 Running spam-detection tests..."
python -m pytest -q
echo "✓ Spam-detection tests passed"
echo ""

# Step 5: Test prediction with a sample message
echo "🔮 Step 5: Testing prediction with sample messages..."
python src/spam_detection/train.py --predict "Congratulations! You won a free prize."
echo ""
python src/spam_detection/train.py --predict "Hi, how are you doing today?"
echo ""

echo "========================================"
echo "✅ All steps completed successfully!"
echo "========================================"
echo ""
echo "📁 Generated outputs:"
echo "   - outputs/models/spam_classifier.joblib"
echo "   - outputs/figures/confusion_matrix.png"
echo ""
echo "📝 Next steps:"
echo "   - Review the confusion matrix in outputs/figures/"
echo "   - Test with your own messages using:"
echo "     python src/spam_detection/train.py --predict 'Your message here'"
echo ""

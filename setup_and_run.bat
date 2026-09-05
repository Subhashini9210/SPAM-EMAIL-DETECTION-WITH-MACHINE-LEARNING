@echo off
REM Spam Email Detection - Setup and Execution Script (Windows)
REM This script automates the installation and execution of the spam detection project

setlocal enabledelayedexpansion

echo.
echo ========================================
echo SPAM EMAIL DETECTION - Setup ^& Run
echo ========================================
echo.

REM Step 1: Install root-level dependencies
echo ^[1/5^] Installing root-level dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo Error installing root dependencies
    exit /b 1
)
echo ^[OK^] Root dependencies installed
echo.

REM Step 2: Run unit tests
echo ^[2/5^] Running unit tests...
python test_spam_detection.py
if errorlevel 1 (
    echo Error running unit tests
    exit /b 1
)
echo ^[OK^] Unit tests completed
echo.

REM Step 3: Run main model (if Tesla.csv exists)
echo ^[3/5^] Running main model...
if exist Tesla.csv (
    python project
    if errorlevel 1 (
        echo Error running main model
        exit /b 1
    )
    echo ^[OK^] Main model executed
) else (
    echo ^[SKIP^] Tesla.csv not found - skipping main model execution
)
echo.

REM Step 4: Setup and run spam-detection subdirectory
echo ^[4/5^] Setting up spam-detection subdirectory...
cd spam-detection

echo Installing spam-detection dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo Error installing spam-detection dependencies
    exit /b 1
)
echo ^[OK^] Spam-detection dependencies installed
echo.

echo Downloading UCI SMS Spam Collection dataset...
python src\spam_detection\download_data.py
if errorlevel 1 (
    echo Error downloading dataset
    exit /b 1
)
echo ^[OK^] Dataset downloaded
echo.

echo Training spam detection model...
python src\spam_detection\train.py
if errorlevel 1 (
    echo Error training model
    exit /b 1
)
echo ^[OK^] Model training completed
echo.

echo Running spam-detection tests...
python -m pytest -q
if errorlevel 1 (
    echo Error running tests
    exit /b 1
)
echo ^[OK^] Spam-detection tests passed
echo.

REM Step 5: Test prediction with sample messages
echo ^[5/5^] Testing prediction with sample messages...
echo.
echo Test 1: Spam message detection
python src\spam_detection\train.py --predict "Congratulations! You won a free prize."
echo.
echo Test 2: Legitimate message detection
python src\spam_detection\train.py --predict "Hi, how are you doing today?"
echo.

cd ..

echo ========================================
echo All steps completed successfully!
echo ========================================
echo.
echo Generated outputs:
echo    - outputs\models\spam_classifier.joblib
echo    - outputs\figures\confusion_matrix.png
echo.
echo Next steps:
echo    - Review the confusion matrix in outputs\figures\
echo    - Test with your own messages using:
echo      python src\spam_detection\train.py --predict "Your message here"
echo.
pause

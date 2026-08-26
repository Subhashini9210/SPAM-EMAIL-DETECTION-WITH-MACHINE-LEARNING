import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
try:
    from xgboost import XGBClassifier
    XGBOOST_AVAILABLE = True
except ImportError:
    XGBOOST_AVAILABLE = False
from sklearn import metrics

import warnings
warnings.filterwarnings('ignore')
print("program is running")

# Test cases for the stock price prediction model

def test_imports():
    """Test that all required libraries can be imported."""
    assert np is not None
    assert pd is not None
    assert LogisticRegression is not None
    assert SVC is not None
    print("✓ All imports successful")


def test_sklearn_models():
    """Test that sklearn models can be instantiated."""
    lr = LogisticRegression(max_iter=1000)
    svc = SVC(kernel='poly', probability=True)
    
    assert lr is not None
    assert svc is not None
    print("✓ All models instantiated successfully")
    
    # Only test XGBoost if available
    if XGBOOST_AVAILABLE:
        xgb = XGBClassifier(eval_metric='logloss', verbosity=0)
        assert xgb is not None
        print("✓ XGBoost instantiated successfully")


def test_sample_data_preprocessing():
    """Test data preprocessing pipeline."""
    # Create sample data
    np.random.seed(42)
    X = np.random.randn(100, 3)
    y = np.random.randint(0, 2, 100)
    
    # Test train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    assert X_train.shape[0] == 80
    assert X_test.shape[0] == 20
    assert X_train.shape[1] == 3
    print("✓ Train-test split works correctly")


def test_scaler():
    """Test StandardScaler functionality."""
    np.random.seed(42)
    data = np.random.randn(50, 3)
    
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    
    # Check that data is scaled (mean ~0, std ~1)
    assert np.abs(scaled_data.mean()) < 0.1
    assert np.abs(scaled_data.std() - 1.0) < 0.1
    print("✓ StandardScaler works correctly")


def test_model_training():
    """Test that models can be trained on sample data."""
    np.random.seed(42)
    X = np.random.randn(100, 3)
    y = np.random.randint(0, 2, 100)
    
    models = [
        LogisticRegression(max_iter=1000),
        SVC(kernel='poly', probability=True),
    ]
    
    # Only add XGBoost if available
    if XGBOOST_AVAILABLE:
        models.append(XGBClassifier(eval_metric='logloss', verbosity=0))
    
    for model in models:
        model.fit(X, y)
        predictions = model.predict(X)
        assert len(predictions) == len(y)
    
    print("✓ Model training works correctly")


def test_model_prediction():
    """Test model predictions and probability outputs."""
    np.random.seed(42)
    X = np.random.randn(100, 3)
    y = np.random.randint(0, 2, 100)
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    
    # Test predictions
    predictions = model.predict(X_test)
    assert len(predictions) == len(y_test)
    assert all(pred in [0, 1] for pred in predictions)
    
    # Test probability predictions
    probabilities = model.predict_proba(X_test)
    assert probabilities.shape == (len(y_test), 2)
    assert all(0 <= prob <= 1 for probs in probabilities for prob in probs)
    
    print("✓ Model prediction works correctly")


def test_model_evaluation():
    """Test model evaluation metrics."""
    np.random.seed(42)
    X = np.random.randn(100, 3)
    y = np.random.randint(0, 2, 100)
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    
    predictions = model.predict(X_test)
    
    # Test various metrics
    accuracy = metrics.accuracy_score(y_test, predictions)
    assert 0 <= accuracy <= 1
    
    cm = metrics.confusion_matrix(y_test, predictions)
    assert cm.shape == (2, 2)
    
    probabilities = model.predict_proba(X_test)[:, 1]
    auc_score = metrics.roc_auc_score(y_test, probabilities)
    assert 0 <= auc_score <= 1
    
    print("✓ Model evaluation works correctly")


def test_csv_loading():
    """Test CSV loading capability."""
    np.random.seed(42)
    test_data = {
        'Date': ['1/1/2020', '2/1/2020', '3/1/2020'],
        'Open': [100, 101, 102],
        'High': [105, 106, 107],
        'Low': [95, 96, 97],
        'Close': [102, 103, 104],
        'Volume': [1000000, 1100000, 1200000]
    }
    
    # Create temporary test CSV
    import tempfile
    import os
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        df = pd.DataFrame(test_data)
        df.to_csv(f.name, index=False)
        temp_file = f.name
    
    try:
        # Test loading
        loaded_df = pd.read_csv(temp_file)
        assert loaded_df.shape[0] == 3
        assert 'Close' in loaded_df.columns
        print("✓ CSV loading works correctly")
    finally:
        os.remove(temp_file)


if __name__ == "__main__":
    print("=" * 60)
    print("Running Stock Price Prediction Tests")
    print("=" * 60 + "\n")
    
    test_imports()
    test_sklearn_models()
    test_sample_data_preprocessing()
    test_scaler()
    test_model_training()
    test_model_prediction()
    test_model_evaluation()
    test_csv_loading()
    
    print("\n" + "=" * 60)
    print("✓ All tests passed!")
    print("=" * 60)
    

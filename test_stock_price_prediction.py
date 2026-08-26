import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn import metrics

import warnings
warnings.filterwarnings('ignore')


# Test cases for the stock price prediction model

def test_imports():
    """Test that all required libraries can be imported."""
    assert np is not None
    assert pd is not None
    assert LogisticRegression is not None
    assert SVC is not None
    assert XGBClassifier is not None
    print("✓ All imports successful")


def test_sklearn_models():
    """Test that sklearn models can be instantiated."""
    lr = LogisticRegression()
    svc = SVC(kernel='poly', probability=True)
    xgb = XGBClassifier()
    
    assert lr is not None
    assert svc is not None
    assert xgb is not None
    print("✓ All models instantiated successfully")


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
        XGBClassifier(use_label_encoder=False, eval_metric='logloss', verbosity=0)
    ]
    
    for model in models:
        model.fit(X, y)
        predictions = model.predict(X)
        assert len(predictions) == len(y)
    
    print("✓ Model training works correctly")


if __name__ == "__main__":
    test_imports()
    test_sklearn_models()
    test_sample_data_preprocessing()
    test_scaler()
    test_model_training()
    print("\n✓ All tests passed!")

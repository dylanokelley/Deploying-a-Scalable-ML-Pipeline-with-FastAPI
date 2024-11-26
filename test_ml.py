import os
import pytest
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from ml.data import process_data
from ml.model import load_model


def test_rf_classifier():
    """
    Esnure model is RandomForestClassifier
    
    """
    project_path = "/Users/dylanokelley/Deploying-a-Scalable-ML-Pipeline-with-FastAPI"
    data_path = os.path.join(project_path, "data", "census.csv")
    model_path = os.path.join(project_path, "model", "model.pkl")
    rf_model = load_model(model_path)
    assert isinstance(rf_model, RandomForestClassifier)


def test_for_null():
    """
    Testing for Null Values, as these could severely alter the outcome of ML models
    """
    project_path = "/Users/dylanokelley/Deploying-a-Scalable-ML-Pipeline-with-FastAPI"
    data_path = os.path.join(project_path, "data", "census.csv")
    data = pd.read_csv(data_path)
    assert sum(data.isnull().sum()) == 0


def test_random_state_42():
    """
    Esnure random state is 42
    
    """
    project_path = "/Users/dylanokelley/Deploying-a-Scalable-ML-Pipeline-with-FastAPI"
    data_path = os.path.join(project_path, "data", "census.csv")
    model_path = os.path.join(project_path, "model", "model.pkl")
    rf_model = load_model(model_path)
    assert rf_model.random_state == 42
import os
import pytest
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from ml.data import process_data
from ml.model import load_model
from train_model import model_path


def test_rf_classifier():
    """
    Esnure model is RandomForestClassifier
    
    """
    #made ajustments to get Github Action to work
    rf_model = load_model(model_path)
    assert isinstance(rf_model, RandomForestClassifier)


def test_for_null():
    """
    Testing for Null Values, as these could severely alter the outcome of ML models
    """

    data_path = 'data/census.csv'
    data = pd.read_csv(data_path)
    assert sum(data.isnull().sum()) == 0


def test_random_state_42():
    """
    Esnure random state is 42
    
    """

    rf_model = load_model(model_path)
    assert rf_model.random_state == 42
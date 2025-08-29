import pytest
from src.model import predict, load_model

def test_model_prediction_all():
    model = load_model("models/test_model.pkl")
    result = predict(model, "all")
    assert "value" in result

def test_model_prediction_country():
    model = load_model("models/test_model.pkl")
    result = predict(model, "India")
    assert "value" in result

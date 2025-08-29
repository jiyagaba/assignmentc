from fastapi import FastAPI
from src.model import load_model, predict

app = FastAPI(title="Country Prediction API")
model = load_model("models/model_v1.pkl")

@app.get("/predict")
def get_prediction(country: str = "all"):
    return {"country": country, "prediction": predict(model, country)}

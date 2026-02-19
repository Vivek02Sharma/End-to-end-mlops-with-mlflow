from fastapi import FastAPI

from src.schemas.medical import MedicalInput
from src.pipeline.predict_pipeline import PredictionPipeline


app = FastAPI(
    title = "Medical Cost Prediction API",
    description = "An end-to-end ML pipeline powered by MLflow",
    version = "1.0.0"
)

predictor = PredictionPipeline()

@app.get("/")
def home():
    return {
        "status": "API is running...",
        "message": "This project is built with an end-to-end ML pipeline integrated with MLflow for tracking and model versioning."
    }

@app.post("/predict")
def predict(data: MedicalInput):
    input_data = data.dict()
    prediction = predictor.predict(input_data)

    return {
        "status": "success",
        "predicted_cost": float(prediction[0])
    }

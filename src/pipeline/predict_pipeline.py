import pandas as pd

from src.utils.helpers import load_model
from configs.config import settings

class PredictionPipeline:
    def __init__(self):
        self.model_path = f"models:/{settings.model_registry_name}/Production"
        self.model = load_model(self.model_path, settings.mlflow_tracking_uri)

    def predict(self, input_data):
        if isinstance(input_data, dict):
            input_data = pd.DataFrame([input_data])

        predictions = self.model.predict(input_data)
        return predictions
    
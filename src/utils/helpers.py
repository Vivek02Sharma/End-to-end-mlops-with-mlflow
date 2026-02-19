import mlflow.pyfunc


def load_model(model_path: str, mlflow_tracking_uri: str):
    mlflow.set_tracking_uri(mlflow_tracking_uri)
    
    model = mlflow.pyfunc.load_model(model_path)
    print(f"Model loaded from {model_path}")
    return model


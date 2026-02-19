from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    mlflow_tracking_uri: str
    mlflow_experiment_name: str
    model_registry_name: str
    best_run_name: str
    dataset_path: str

    
    model_config = SettingsConfigDict(
        env_file = ".env",
        env_file_encoding = "utf-8"
    )

settings = Settings()
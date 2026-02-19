from src.data.data_loader import DataLoader
from src.data.preprocessor import DataPreprocessor
from src.models.trainer import ModelTrainer
from configs.config import settings

class TrainingPipeline:
    def __init__(self):
        self.dataset_path = settings.dataset_path

    def move_model_to_production(self):
    
        from mlflow.tracking import MlflowClient

        client = MlflowClient()
        latest_version = client.get_latest_versions(settings.model_registry_name)[0].version
        client.transition_model_version_stage(
            name = settings.model_registry_name,
            version = latest_version,
            stage = "Production"
        )

    def run(self):
        try:
            data_loader = DataLoader(self.dataset_path)
            df = data_loader.load_data()

            preprocessor = DataPreprocessor()
            X_train, X_test, y_train, y_test = preprocessor.split_data(df)
            
            preprocessor_pipeline = preprocessor.data_preprocessor()
            trainer = ModelTrainer(preprocessor_pipeline)
            trainer.train_models(X_train, y_train, X_test, y_test)

            self.move_model_to_production()
            print("\nModel successfully moved to production.")
        except Exception as e:
            raise e
        

def main():
    pipeline = TrainingPipeline()
    pipeline.run()

if __name__ == "__main__":
    main()

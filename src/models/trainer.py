from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import xgboost as xgb

import numpy as np

import mlflow


class ModelTrainer:
    def __init__(self, preprocessor):
        self.preprocessor = preprocessor

        self.models = {
            "LinearRegression": LinearRegression(),
            "RandomForest": RandomForestRegressor(n_estimators = 200, random_state = 42),
            "XGBoost": xgb.XGBRegressor(n_estimators = 200, objective = 'reg:squarederror'),
            "GradientBoostingRegressor": GradientBoostingRegressor(n_estimators = 300)
        }

    def create_pipeline(self, model):
        return Pipeline(steps = [
            ('preprocessor', self.preprocessor),
            ('model', model)
        ])

    def evaluate_model(self, y_true, y_pred):
        metrics = {
            "mae": mean_absolute_error(y_true, y_pred),
            "rmse": np.sqrt(mean_squared_error(y_true, y_pred)),
            "r2": r2_score(y_true, y_pred)
        }

        return metrics

    def train_models(self, X_train, y_train, X_test, y_test):

        from configs.config import settings

        mlflow.set_tracking_uri(settings.mlflow_tracking_uri)
        mlflow.set_experiment(settings.mlflow_experiment_name)

        best_r2 = -np.inf
        best_run_id = None
        best_model_name = None
        best_model_pipeline = None

        for name, model in self.models.items():
            
            try:
                with mlflow.start_run(run_name = name) as run:
                    pipeline = self.create_pipeline(model)
                    pipeline.fit(X_train, y_train)
                    
                    y_train_pred = pipeline.predict(X_train)
                    y_test_pred = pipeline.predict(X_test)

                    train_metrics = self.evaluate_model(y_train, y_train_pred)
                    test_metrics = self.evaluate_model(y_test, y_test_pred)

                    metrics = {
                        'train_mae': train_metrics['mae'],
                        'train_rmse': train_metrics['rmse'],
                        'train_r2': train_metrics['r2'],

                        'test_mae': test_metrics['mae'],
                        'test_rmse': test_metrics['rmse'],
                        'test_r2': test_metrics['r2']
                    }

                    mlflow.set_tag("model_name", name)
                    mlflow.log_metrics(metrics)

                    # select best run
                    if metrics['test_r2'] > best_r2:
                        best_r2 = metrics['test_r2']
                        best_run_id = run.info.run_id
                        best_model_name = name
                        best_model_pipeline = pipeline

                    print(f"\n\nLogged successfully {name}")

            except Exception as e:
                print(f"Error training {name}: {str(e)}")
            
        print("\nBest model found: ")
        print("Best Model:", best_model_name)
        print("Best Run ID:", best_run_id)
        print("Best R2:", best_r2)

        with mlflow.start_run(run_name = settings.best_run_name):

            mlflow.set_tag("best_model", best_model_name)
            mlflow.log_metric("Best_R2", best_r2)

            mlflow.sklearn.log_model(
                best_model_pipeline,
                name = "best_pipeline",
                registered_model_name = settings.model_registry_name
            )

        print("Best Model Registered Successfully")
            
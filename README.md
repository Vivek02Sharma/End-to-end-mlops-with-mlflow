# Medical Cost Prediction

An end-to-end MLOps pipeline for predicting annual medical costs, built with MLflow for experiment tracking and model registry, FastAPI for serving predictions, and Streamlit for the frontend.

## Project Structure

```
Medical-Cost-Prediction/
├── configs/config.py          
├── data/
│   └── raw/                   
├── src/
│   ├── api/            
│   ├── data/                   
│   ├── models/
│   ├── pipeline/
│   ├── schemas/
│   └── utils/
├── notebook/
├── main.py
├── .env
└── pyproject.toml
```

## Setup

1. Clone the repo and install dependencies:
```bash
git clone <repository-url>
cd Medical-Cost-Prediction
uv sync
```

2. Activate the virtual environment:
```bash
source .venv/bin/activate
```

3. Create `.env` file:
```bash
MLFLOW_TRACKING_URI=http://127.0.0.1:5000
MLFLOW_EXPERIMENT_NAME=Medical_Cost_Prediction
MODEL_REGISTRY_NAME=MedicalCostBestPipeline
BEST_RUN_NAME=best_run
DATASET_PATH=data/raw/medical_cost_prediction_dataset.csv
```

## Usage

**1. Start MLflow server:**
```bash
mlflow server --port 5000
```

**2. Train models:**
```bash
python -m src.pipeline.train_pipeline
```

**3. Start API:**
```bash
uvicorn src.api.app:app --reload
```

**4. Start Streamlit:**
```bash
streamlit run main.py
```

## Models

| Model | Type |
|---|---|
| Linear Regression | Baseline |
| Random Forest | 200 estimators |
| XGBoost | 200 estimators |
| Gradient Boosting | 300 estimators |

Best model is automatically selected by R² score and promoted to production in MLflow registry.

## Tech Stack

`Python` `MLflow` `FastAPI` `Streamlit` `scikit-learn` `XGBoost` `Pydantic` `Pandas`

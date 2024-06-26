import os
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score

from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from src.riskDemo.entity.config_entity import ModelEvaluationConfig
from src.riskDemo.utils.common import save_json
from pathlib import Path


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self, actual, pred):
        acc = accuracy_score(actual, pred)
        roc = roc_auc_score(actual, pred)
        return acc, roc

    def log_into_mlflow(self):

        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        print(f"SEIYA: {tracking_url_type_store}")
        with mlflow.start_run():

            predicted_qualities = model.predict(test_x)

            (acc, roc) = self.eval_metrics(test_y, predicted_qualities)

            # Saving metrics as local
            scores = {"Accuracy": acc, "ROC_AUC_Score": roc}
            save_json(path=Path(self.config.metric_file_name), data=scores)

            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("Accuracy", acc)
            mlflow.log_metric("ROC_AUC_Score", roc)

            # Model registry does not work with file store
            if tracking_url_type_store != "file":

                # https://mlflow.org/docs/latest/model-registry.html#api-workflow
                mlflow.sklearn.log_model(
                    model, "model", registered_model_name="LogisticRegression"
                )
            else:
                mlflow.sklearn.log_model(model, "model")

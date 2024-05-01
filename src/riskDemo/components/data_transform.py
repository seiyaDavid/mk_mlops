import os
from src.riskDemo import logger
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
from src.riskDemo.entity.config_entity import DataTransformationConfig


class DataTransformation:

    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)

        X = data.drop("TARGET", axis=1)  # Features
        y = data["TARGET"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )

        X_train = pd.concat([X_train, y_train], axis=1)
        X_test = pd.concat([X_test, y_test], axis=1)

        train = X_train.drop("Unnamed: 0", axis=1)
        test = X_test.drop("Unnamed: 0", axis=1)

        X_train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        X_test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        # print(train.shape)
        # print(test.shape)

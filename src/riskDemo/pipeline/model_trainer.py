from src.riskDemo.config.configuration import ConfigurationManager
from src.riskDemo.components.model_tain import ModelTrainer
from src.riskDemo import logger


STAGE_NAME = "Model Trainer stage"


class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()

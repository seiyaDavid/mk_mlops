from src.riskDemo.config.configuration import ConfigurationManager
from src.riskDemo.components.data_val import DataValiadtion
from src.riskDemo import logger


STAGE_NAME = "Data Validation stage"


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.validate_all_columns()

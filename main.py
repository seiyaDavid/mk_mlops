from src.riskDemo import logger
from src.riskDemo.pipeline.initial_data_data_ingestion import (
    DataIngestionTrainingPipeline,
)

from src.riskDemo.pipeline.data_val import DataValidationTrainingPipeline
from src.riskDemo.pipeline.data_transformation import DataTransformationTrainingPipeline
from src.riskDemo.pipeline.model_trainer import ModelTrainerTrainingPipeline
from src.riskDemo.pipeline.model_evaluation import ModelEvaluationTrainingPipeline


STAGE_NAME = "Data Ingestion "
try:
    logger.info(f"=========== {STAGE_NAME} process has started ===========")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"=========== {STAGE_NAME} process is finished ===========\n\n")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation"
try:
    logger.info(f"=========== {STAGE_NAME} process has started ===========")
    data_ingestion = DataValidationTrainingPipeline()
    data_ingestion.main()
    logger.info(f"=========== {STAGE_NAME} process is finished ===========\n\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation "
try:
    logger.info(f"=========== {STAGE_NAME} process has started ===========")
    data_ingestion = DataTransformationTrainingPipeline()
    data_ingestion.main()
    logger.info(f"=========== {STAGE_NAME} process is finished ===========\n\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Trainer "
try:
    logger.info(f"=========== {STAGE_NAME} process has started ===========")
    data_ingestion = ModelTrainerTrainingPipeline()
    data_ingestion.main()
    logger.info(f"=========== {STAGE_NAME} process is finished ===========\n\n")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model evaluation "
try:
    logger.info(f"=========== {STAGE_NAME} process has started ===========")
    data_ingestion = ModelEvaluationTrainingPipeline()
    data_ingestion.main()
    logger.info(f"=========== {STAGE_NAME} process is finished ===========\n\n")
except Exception as e:
    logger.exception(e)
    raise e

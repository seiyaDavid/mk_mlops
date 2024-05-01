from src.riskDemo import logger
from src.riskDemo.pipeline.initial_data_data_ingestion import (
    DataIngestionTrainingPipeline,
)

from src.riskDemo.pipeline.data_val import DataValidationTrainingPipeline


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

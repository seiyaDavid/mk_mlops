from src.riskDemo import logger
from src.riskDemo.pipeline.initial_data_data_ingestion import (
    DataIngestionTrainingPipeline,
)


STAGE_NAME = "Data Ingestion "
try:
    logger.info(f"=========== {STAGE_NAME} process has started ===========")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"=========== {STAGE_NAME} process is finished ===========\n\n")
except Exception as e:
    logger.exception(e)
    raise e

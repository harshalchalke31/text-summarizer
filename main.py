from src.textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionForTraining
from src.textSummarizer.logging import logger

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"{STAGE_NAME} Started >>>>>>>>>>>>>>>>>>>>>")
    data_ingestion = DataIngestionForTraining()
    data_ingestion.main()
    logger.info(f"{STAGE_NAME} completed >>>>>>>>>>>>>>>>>>>>>")
except Exception as e:
    logger.exception(e)
    raise e

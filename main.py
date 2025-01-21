from src.textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionForTraining
from src.textSummarizer.pipeline.stage_02_data_validation import DataValidationForTraining
from src.textSummarizer.logging import logger

STAGE_NAME_1 = "Data Ingestion Stage"

try:
    logger.info(f"{STAGE_NAME_1} Started >>>>>>>>>>>>>>>>>>>>>")
    data_ingestion = DataIngestionForTraining()
    data_ingestion.main()
    logger.info(f"{STAGE_NAME_1} completed >>>>>>>>>>>>>>>>>>>>>")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME_2 = "Data Validation Stage"

try:
    logger.info(f"{STAGE_NAME_2} Started >>>>>>>>>>>>>>>>>>>>>")
    data_validation = DataValidationForTraining()
    data_validation.main()
    logger.info(f"{STAGE_NAME_2} completed >>>>>>>>>>>>>>>>>>>>>")
except Exception as e:
    logger.exception(e)
    raise e
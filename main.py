from src.textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionForTraining
from src.textSummarizer.pipeline.stage_02_data_validation import DataValidationForTraining
from src.textSummarizer.pipeline.stage_03_data_transformation import DataTransformationForTraining
from src.textSummarizer.pipeline.stage_04_model_trainer import ModelTrainingPipeline
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


STAGE_NAME_3 = "Data Transformation Stage"

try:
    logger.info(f"{STAGE_NAME_3} Started >>>>>>>>>>>>>>>>>>>>>")
    data_transformation = DataTransformationForTraining()
    data_transformation.main()
    logger.info(f"{STAGE_NAME_3} completed >>>>>>>>>>>>>>>>>>>>>")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME_4 = "Model Training Stage"

try:
    logger.info(f"{STAGE_NAME_4} Started >>>>>>>>>>>>>>>>>>>>>")
    data_transformation = ModelTrainingPipeline()
    data_transformation.main()
    logger.info(f"{STAGE_NAME_4} completed >>>>>>>>>>>>>>>>>>>>>")
except Exception as e:
    logger.exception(e)
    raise e
import os
from textSummarizer.entity import DataValidationConfig
from textSummarizer.logging import logger

class DataValidation:
    def __init__(self,config: DataValidationConfig):
        self.config = config
    
    def validate_all_files(self)->bool:
        try:
            validation_status=None
            all_files=os.listdir(os.path.join('artifacts','data_ingestion','summary_data'))

            for file in all_files:
                if file not in self.config.ALL_REQUIRED_FILES:
                    validation_status=False
                    with open(self.config.STATUS_FILE,'w') as status:
                        status.write(f"Validation Status: {validation_status} for the file {file}.")
                    logger.info(f"Data validation unsuccessful.")
                else:
                    validation_status=True
                    with open(self.config.STATUS_FILE,'w') as status:
                        status.write(f"Validation Status: {validation_status} for the all files.")
                    logger.info("Data Validation Succesful.")
            return validation_status
        except Exception as e:
            raise e                
from textSummarizer.utils.common import read_yaml, create_directories, get_size
from textSummarizer.logging import logger
from textSummarizer.constants import *
from textSummarizer.entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(self,
                 config_file_path=CONFIG_FILE_PATH,
                 params_file_path=PARAMS_FILE_PATH):
        # paths accessed via constant.py -> config.yaml,params.yaml
        self.config=read_yaml(config_file_path)
        self.params=read_yaml(params_file_path)

        create_directories([self.config.artifacts_root]) # due to configbox setup

    def get_data_ingestion_config(self) -> DataIngestionConfig:

        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            local_data_file=config.local_data_file,
            source_URL=config.source_URL,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config
from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_transformation import DataTransformation

class DataTransformationForTraining:
    def __init__(self):
        pass

    def main():
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation=DataTransformation(config=data_transformation_config)
        data_transformation.convert()
from recommed.components.data_ingestion import DataIngestion
from recommed.components.data_validation import DataValidation
from recommed.logger.loggng import logging


logging.info("Enter the training pipeline")
class TrainingPipeline:
    def __init__(self):
        self.data_ingestion = DataIngestion()
        self.data_validation=DataValidation()
    

    def start_training_pipeline(self):
        self.data_ingestion.initiate_data_ingestion()
        self.data_validation.initiate_data_validation()
    logging.info("Exited the training pipeline")
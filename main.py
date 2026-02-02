from networksecurity.components.data_ingestion import DateIngestion
from networksecurity.components.data_validation import DataValidation, DataValidationConfig
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
import sys


if __name__ == "__main__":
    try:
        training_pipeline_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config)
        data_ingestion = DateIngestion(data_ingestion_config)
        logging.info("Initializing data ingestion")
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
        logging.info("Completed data ingestion")
        print(data_ingestion_artifact)

        data_validation_config = DataValidationConfig(training_pipeline_config)
        data_validation = DataValidation(
            data_ingestion_artifact, data_validation_config)
        logging.info("Initializing data validation")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("Completed data validation")
        print(data_validation_artifact)

    except Exception as e:
        logging.info(f"Error occurred in main.py: {e}")
        raise NetworkSecurityException(e, sys) from e

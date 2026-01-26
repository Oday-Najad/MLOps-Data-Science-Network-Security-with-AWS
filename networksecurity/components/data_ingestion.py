from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
import sys
import pandas as pd
import numpy as np
import os
import pymongo
from typing import List
from sklearn.model_selection import train_test_split
from networksecurity.entity.artifact_entity import DataIngestionArtifact


from dotenv import load_dotenv

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL_KEY")


class DateIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
            logging.info(f"{'>>'*20} Data Ingestion {'<<'*20}")
            self.data_ingestion_config = data_ingestion_config

        except Exception as e:
            raise NetworkSecurityException(e, sys) from e

    def export_collection_as_dataframe(self) -> pd.DataFrame:
        try:
            logging.info(f"Exporting collection data as dataframe")
            mongo_client = pymongo.MongoClient(MONGODB_URL)
            logging.info(f"Connected to Mongodb successfully to export data")
            database = mongo_client[self.data_ingestion_config.database_name]
            collection = database[self.data_ingestion_config.collection_name]
            df = pd.DataFrame(list(collection.find()))
            logging.info(f"Dataframe shape: {df.shape}")
            if "_id" in df.columns:
                logging.info(f"Dropping column: _id")
                df = df.drop(columns=["_id"], axis=1)
            df.replace(to_replace="na", value=np.nan, inplace=True)
            return df
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e

    def initiate_data_ingestion(self):
        try:
            logging.info(f"Initiating data ingestion")
            df = self.export_collection_as_dataframe()
            logging.info(f"Creating feature store folder if not available: "
                         f"{os.path.dirname(self.data_ingestion_config.feature_store_file_path)}")
            os.makedirs(os.path.dirname(
                self.data_ingestion_config.feature_store_file_path), exist_ok=True)
            logging.info(f"Saving data to feature store folder: "
                         f"{self.data_ingestion_config.feature_store_file_path}")
            df.to_csv(self.data_ingestion_config.feature_store_file_path,
                      index=False, header=True)
            logging.info(f"Splitting data into train and test set with test size: "
                         f"{self.data_ingestion_config.train_test_split_ratio}")
            train_set, test_set = train_test_split(
                df,
                test_size=self.data_ingestion_config.train_test_split_ratio,
                random_state=42
            )
            logging.info(f"Creating ingested folder if not available: "
                         f"{os.path.dirname(self.data_ingestion_config.train_file_path)}")
            os.makedirs(os.path.dirname(
                self.data_ingestion_config.train_file_path), exist_ok=True)
            logging.info(
                f"Saving training data to file: {self.data_ingestion_config.train_file_path}")
            train_set.to_csv(
                self.data_ingestion_config.train_file_path, index=False, header=True)
            logging.info(
                f"Saving testing data to file: {self.data_ingestion_config.test_file_path}")
            test_set.to_csv(
                self.data_ingestion_config.test_file_path, index=False, header=True)
            logging.info(f"Data ingestion completed successfully")

            data_ingestion_artifact = DataIngestionArtifact(
                train_file_path=self.data_ingestion_config.train_file_path,
                test_file_path=self.data_ingestion_config.test_file_path
            )
            logging.info(f"Data Ingestion Artifact: {data_ingestion_artifact}")
            return data_ingestion_artifact

        except Exception as e:
            raise NetworkSecurityException(e, sys) from e

import os
import sys
import json
import certifi
import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging


from dotenv import load_dotenv

load_dotenv()

mongodb_url = os.getenv("MONGODB_URL_KEY")

ca = certifi.where()


class NetworkDataExtract:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e

    def csv_to_json(self, file_path: str) -> str:
        """This function will convert CSV data to JSON format"""
        try:
            df = pd.read_csv(file_path)
            df.reset_index(drop=True, inplace=True)
            json_data = list(json.loads(df.T.to_json()).values())
            return json_data
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e

    def insert_data_to_mongodb(self, records, database, collection) -> None:
        """This function will insert data into MongoDB collection"""
        try:
            self.database = database
            self.collection = collection
            self.records = records
            self.mongoClient = pymongo.MongoClient(mongodb_url, tlsCAFile=ca)

            self.database = self.mongoClient[self.database]
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            logging.info("Data inserted successfully into MongoDB")
            return len(self.records)
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e


if __name__ == "__main__":
    FILE_PATH = "Network_Data/phisingData.csv"
    DATABASE_NAME = "odaynajad_NS_DB"
    COLLECTION_NAME = "phishing_data"
    network_object = NetworkDataExtract()
    network_object.csv_to_json(file_path=FILE_PATH)
    number_of_records = network_object.insert_data_to_mongodb(
        records=network_object.csv_to_json(file_path=FILE_PATH),
        database=DATABASE_NAME,
        collection=COLLECTION_NAME
    )

    records = network_object.csv_to_json(file_path=FILE_PATH)
    print(records)
    print(f"Number of records inserted: {number_of_records}")

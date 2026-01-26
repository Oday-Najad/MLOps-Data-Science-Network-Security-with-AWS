import os
import sys
import pandas as pd
import numpy as np


"""
Defining common constant variables for training pipeline
"""

TARGET_COLUMN = "Result"
PIPELINE_NAME: str = "NetworkSecurity"
ARTIFACT_DIR: str = "Artifacts"
FILE_NAME: str = "phishingData.csv"

TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"


"""
Data Ingestion related constants start with DATA_INGESTION variable name
"""

DATA_INGESTION_COLLECTION_NAME: str = "phishing_data"
DATA_INGESTION_DATABASE_NAME: str = "odaynajad_NS_DB"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested_data"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION: float = 0.2

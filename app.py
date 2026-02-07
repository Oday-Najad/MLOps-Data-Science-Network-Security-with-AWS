from networksecurity.constants.training_pipeline import DATA_INGESTION_DATABASE_NAME
from networksecurity.constants.training_pipeline import DATA_INGESTION_COLLECTION_NAME
from networksecurity.utils.main_utils.utils import load_object
from uvicorn import run as app_run
import pandas as pd
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.middleware.cors import CORSMiddleware
from networksecurity.pipeline.training_pipeline import TrainingPipeline
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException
import pymongo
from dotenv import load_dotenv
import os
import sys

import certifi

ca = certifi.where()


load_dotenv()

mongodb_url = os.getenv("MONGODB_URL_KEY")
print(mongodb_url)


client = pymongo.MongoClient(mongodb_url)
database = client[DATA_INGESTION_DATABASE_NAME]
collection = database[DATA_INGESTION_COLLECTION_NAME]


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")


@app.get("/train", tags=["train"])
async def train_route():
    try:
        train_pipeline = TrainingPipeline()
        train_pipeline.run_pipeline()
        return Response(content="Training successful!!")
    except Exception as e:
        raise NetworkSecurityException(e, sys)


if __name__ == "__main__":
    app_run(app, host="localhost", port=8000)

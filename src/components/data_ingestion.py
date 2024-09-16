import sys 
import os 
import pandas as pd 
import numpy as np
from pymongo import MongoClient # type: ignore
from zipfile import Path
from src.constant import *
from src.exception import CustomException
from src.logger import logging
from src.utils.main_utils import MainUtils # type: ignore
from dataclasses import dataclass


@dataclass 
class DataIngestionConfig:
    artifacts_Folder: str = os.path.join(artifact_folder)


class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.utils = MainUtils()

    def export_collection_as_dataframe(self,collection_name,db_name):

        try:
            mongo_client = MongoClient(MONGO_DB_URL)

            collection = mongo_client[db_name][collection_name]

            df = pd.DataFrame(list(collection.find()))

            if "_id" in df.columns.to_list():
                  df = df.drop(columns=['_id'],axis=1)

            df.replace({"na":np.nan},inplace=True)

            return df
        except Exception as e:
            raise CustomException(np.e,sys)
    
    def export_data_into_feature_store_file_path(self) -> pd.DataFrame:

        try:

            logging.info(f"Exporting data from mongodb")
            raw_file_path = self.data _ingestion_config.artifacts_folder # type: ignore

            os.makedirs(raw_file_path,exist_ok =True)

            sensor_data = self.export_collection_as_dataframe(
                collection_name= MONGO_COLLECTION_NAME,
                db_name= MONGO_DATABASE_NAME
            )

            logging.info(f"saving exported data into feature store file path :{raw_file_path}")

            feature_store_file_path = os.path.join(raw_file_path,'wafer_fault.csv')

            sensor_data.to_csv(feature_store_file_path, index=False)

            return feature_store_file_path
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def intiate_data_ingestion(self) -> os.path :

        logging.info("Entered intiated_data_ingestion method of data_integration class")

        try:
            feature_store_file_path = self.export_data_inti_feature_store_file_path()

            logging.info("got the data from mongodb")

            logging.info("exited intiated_data_ingestion method of data ingestion class ")

            return feature_store-file_path # type: ignore
        except Exception as e:
            raise CustomException(e,sys)
            
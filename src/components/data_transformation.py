import sys
import os 
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.impute import simpleImputer 
from sklearn.preprocessing import RobustScaler,FunctionTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from src.constant import *
from src.exception import CustomException
from src.logger import logging
from src.utils.main_utils import Mainutils # type: ignore
from dataclasses import dataclass


@dataclass
class DataTransformationConfig:
    artifact_dir = os.path.join(artifact_folder)
    transformed_train_file_path =os.path.join(artifact_dir,'train.npy')
    transformed_test_file_path =os.path.join(artifact_dir,'test.npy')
    transformed_object_file_path =os.path.join(artifact_dir,'preprocessor.pk1')


class DataTransformation:
    def __init__(self,feature_store_file_path):
        self.festure-store-feature_store_file_path= feature_store_file_path

        self.data_transformation_config = DataTransformationConfig()

        self.utils = Mainutils()




        try:

            data = pd.read_csv(feature_store_file_path)

            data.rename(columns={"Good/Bad": TARGET_COLUMN}, inplace=True)

            return data
        except Exception as e:
            raise CustomException(e,sys)
        
    def get_data_transform_object(self):

        try:

            imputer_step = ('imputer',simpleImputer(strategy = 'constant', fill_value= 0))
            scaler_step = ('scaler', RobustScaler())

            preprocessor = Pipeline(
                steps=[
                    imputer_step,
                    scaler_step
                ]
            )

            return preprocessor
        except Exception as e:
            raise CustomException(e,sys)
        
    def intiate_data_transformation(self):

        logging.info("entered intiate data transformation method of data transformation class")    
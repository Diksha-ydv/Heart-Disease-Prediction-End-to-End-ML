import os 
import sys 
from src.logger import logging 
from src.exception import HeartDiseaseError
from dataclasses import dataclass
import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split
from src.components.data_transformation import DataTransformation,DataTransformationConfig

@dataclass
class DataIngestionConfig:
    train_data_path = os.path.join("artifacts","train_data.csv")
    test_data_path = os.path.join("artifacts","test_data.csv")
    raw_data_path = os.path.join("artifacts","data.csv")


class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()


    def initiate_datapath(self,file_path):
        try:
            logging.info("Data ingestion started")
            df = pd.read_csv(file_path)

            os.makedirs(os.path.dirname(self.data_ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.data_ingestion_config.raw_data_path,index=None,header=True)

            train_data,test_data = train_test_split(df,test_size=0.2,random_state=1)
            logging.info("Train test split done")

            train_data.to_csv(self.data_ingestion_config.train_data_path,index=None,header=True)
            test_data.to_csv(self.data_ingestion_config.test_data_path,index=None,header=True)

            return train_data,test_data
        
        except Exception as e:
            raise HeartDiseaseError(e,sys)
        

if __name__=="__main__":
    data_ingestion = DataIngestion()
    train_data,test_data = data_ingestion.initiate_datapath("notebook/data/heart.csv")

    data_transform = DataTransformation()
    x_train_arr,x_test_arr,preprocessor_obj = data_transform.perform_transformation(train_data,test_data)
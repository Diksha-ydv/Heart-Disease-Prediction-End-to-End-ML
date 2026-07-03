import os 
import sys 
from src.logger import logging 
from src.exception import HeartDiseaseError
from dataclasses import dataclass
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
import numpy as np 
from src.utils import save_object


@dataclass
class DataTransformationConfig:
    preprocessor_path = os.path.join("artifacts","preprocessor.pkl")


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def initiate_transformation(self):
        try:
            num_features = ['Age',
                            'RestingBP',
                            'Cholesterol', 
                            'FastingBS', 
                            'MaxHR', 
                            'Oldpeak']
            
            cat_features = ['Sex', 
                            'ChestPainType', 
                            'RestingECG', 
                            'ExerciseAngina', 
                            'ST_Slope']
            
            logging.info("Creating pipelines")
            num_pipeline = Pipeline(steps=[
                ("imputer",SimpleImputer(strategy="median")),
                ("standard_scaler",StandardScaler())
            ])

            cat_pipeline = Pipeline(steps=[
                ("imputer",SimpleImputer(strategy="most_frequent")),
                ("onehotencoder",OneHotEncoder(drop="first"))
            ])
            logging.info("creating preprocessor")

            preprocessor = ColumnTransformer(transformers=[
                ("num pipeline",num_pipeline,num_features),
                ("cat pipeline",cat_pipeline,cat_features)
            ])

            return preprocessor
        
        except Exception as e:
            raise HeartDiseaseError(e,sys)
        
    def perform_transformation(self,train_data,test_data):
        try:
            x_train_df = train_data.drop("HeartDisease",axis=1)
            x_train_target = train_data["HeartDisease"]

            x_test_df = test_data.drop("HeartDisease",axis=1)
            x_test_target = test_data["HeartDisease"]
            preprocessor_obj = self.initiate_transformation()

            x_train_transform = preprocessor_obj.fit_transform(x_train_df)
            x_test_transform = preprocessor_obj.transform(x_test_df)
            logging.info("Preprocessing done")

            x_train_arr = np.c_[x_train_transform,np.array(x_train_target)]
            x_test_arr = np.c_[x_test_transform,np.array(x_test_target)]

            save_object(file_path = self.data_transformation_config.preprocessor_path,obj = preprocessor_obj)
            logging.info("Preprocessor saved")

            return x_train_arr,x_test_arr,preprocessor_obj
        
        except Exception as e:
            raise HeartDiseaseError(e,sys)

    

        

import os 
import sys 
from src.exception import HeartDiseaseError
from src.logger import logging 
from src.utils import load_object
import pandas as pd 

class predict:
    def __init__(self):
        pass 

    def pred_val(self,features):
        try:
            model_path = os.path.join("artifacts","model.pkl")
            preprocessor_path = os.path.join("artifacts","preprocessor.pkl")
            model = load_object(file_path = model_path)
            preprocessor = load_object(file_path = preprocessor_path)
            data_scaled = preprocessor.transform(features)
            predict_val = model.predict(data_scaled)
            

            return predict_val[0]
        except Exception as e:
            raise HeartDiseaseError(e,sys)
    

class predict_datapnt:
    def __init__(self,
                 Age:int,
                 Sex:str,
                 ChestPainType:str,
                 RestingBP:int,
                 Cholesterol:int,
                 FastingBS:int,
                 RestingECG:str,
                 MaxHR:int,
                 ExerciseAngina:str,
                 Oldpeak:float,
                 ST_Slope:str):
        
        self.Age = Age 
        self.Sex = Sex
        self.ChestPainType = ChestPainType
        self.RestingBP = RestingBP
        self.Cholesterol = Cholesterol
        self.FastingBS = FastingBS
        self.RestingECG = RestingECG
        self.MaxHR = MaxHR
        self.ExerciseAngina = ExerciseAngina
        self.Oldpeak = Oldpeak
        self.ST_Slope = ST_Slope

    def csv_to_dataframe(self):
        try:
            custom_data = pd.DataFrame({
                "Age":[self.Age],
                "Sex":[self.Sex],
                "ChestPainType":[self.ChestPainType],
                "RestingBP":[self.RestingBP],
                "Cholesterol":[self.Cholesterol],
                "FastingBS":[self.FastingBS],
                "RestingECG":[self.RestingECG],
                "MaxHR":[self.MaxHR],
                "ExerciseAngina":[self.ExerciseAngina],
                "Oldpeak":[self.Oldpeak],
                "ST_Slope":[self.ST_Slope]

            })
            return custom_data
        except Exception as e:
            raise HeartDiseaseError(e,sys)

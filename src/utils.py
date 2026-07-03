#Creating generic functions for complete code 
import os 
import sys 
from src.logger import logging 
from src.exception import HeartDiseaseError
import pickle 

def save_object(file_path,obj):
    try:
        os.makedirs(os.path.dirname(file_path),exist_ok=True)

        with open(file_path,"wb") as file:
            pickle.dump(obj,file)
    
    except Exception as e:
        raise HeartDiseaseError(e,sys)


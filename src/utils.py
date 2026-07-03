#Creating generic functions for complete code 
import os 
import sys 
from src.logger import logging 
from src.exception import HeartDiseaseError
import pickle 
from sklearn.metrics import f1_score,roc_auc_score

def save_object(file_path,obj):
    try:
        os.makedirs(os.path.dirname(file_path),exist_ok=True)

        with open(file_path,"wb") as file:
            pickle.dump(obj,file)
    
    except Exception as e:
        raise HeartDiseaseError(e,sys)


def evaluate_model(y_train,y_train_pred,y_test,y_test_pred):
    f1_train = f1_score(y_train,y_train_pred)
    roc_train = roc_auc_score(y_train,y_train_pred)

    f1_test = f1_score(y_test,y_test_pred)
    roc_test = roc_auc_score(y_test,y_test_pred)

    return f1_train,roc_train,f1_test,roc_test

def load_object(file_path):
    try:
        with open(file_path,"rb") as file:
            return pickle.load(file)

    except Exception as e:
        raise HeartDiseaseError(e,sys)
    


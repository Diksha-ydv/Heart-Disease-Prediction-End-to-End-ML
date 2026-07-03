import os 
import sys
from src.exception import HeartDiseaseError
from src.logger import logging 
from dataclasses import dataclass
import matplotlib.pyplot as plt 
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier,AdaBoostClassifier,GradientBoostingClassifier
from xgboost import XGBClassifier
from catboost import CatBoostClassifier
from sklearn.metrics import f1_score
from src.utils import evaluate_model, save_object
import pandas as pd 

@dataclass
class ModelTrainerConfig:
    model_path = os.path.join("artifacts","model.pkl")


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_training(self,train_arr,test_arr):
        try:
            x_train,y_train,x_test,y_test = [train_arr[:,:-1],train_arr[:,-1],test_arr[:,:-1],test_arr[:,-1]]

            models = {
                "logistic regression":LogisticRegression(),
                "support vector classifier":SVC(),
                "K neighbors classifier":KNeighborsClassifier(),
                "Decision tree classifier":DecisionTreeClassifier(),
                "Random forest classifier":RandomForestClassifier(),
                "Adaboost Classifier":AdaBoostClassifier(),
                "Gradient boost classifier":GradientBoostingClassifier(),
                "XGB classifier":XGBClassifier(),
                "catboost classifier":CatBoostClassifier(verbose=False)
            }
            logging.info("model training started")
            model_lst = []
            score_lst = []
            for name,model in models.items():
                model.fit(x_train,y_train)
                y_train_pred = model.predict(x_train)
                y_test_pred = model.predict(x_test)

                f1_train,roc_train,f1_test,roc_test = evaluate_model(y_train,y_train_pred,y_test,y_test_pred)

                model_lst.append(name)
                score_lst.append(f1_test)

                model_score_df = pd.DataFrame(data=list(zip(model_lst,score_lst)),columns=["model_name","score"]).sort_values(by="score",ascending=False)
                best_model_name = model_score_df.iloc[0,0]
                best_model = models[best_model_name]
                logging.info(f"best model found is {best_model_name}")
                #training using best model 
                best_model.fit(x_train,y_train)
                best_model_predict = best_model.predict(x_test)

                score = f1_score(y_test,best_model_predict)
                logging.info("best score is {}".format(score))

                save_object(file_path=self.model_trainer_config.model_path,obj=best_model)
                return score 
            
        except Exception as e:
            raise HeartDiseaseError(e,sys)
        

                


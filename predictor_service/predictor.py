# app/main.py
from pydantic import BaseModel, ValidationError
import numpy as np
from typing import Literal
import joblib
import json
import pandas as pd
import pickle
import warnings
import xgboost
warnings.filterwarnings('ignore')


class UserInput(BaseModel):
    Sex:Literal['male','female']
    Age: int
    Height: float
    Weight: float
    Duration: float
    Heart_Rate: int
    Body_Temp: float





def feature_engineering(user_input:UserInput):

    user = user_input.model_dump()
    with open(r"parameters\Sex_TE_Global_Means.json",'r') as f:
        sex_te_means = json.load(f)
    # Target Encoding of categorical variables
    user['TE_Sex']=sex_te_means[user['Sex']]
# BMR
    user['BMR'] = [10 * user['Weight'] + 6.25 * user['Height']/100 - 5 * user['Age'] + 5\
                if user['Sex']=='male'\
                    else 10 * user['Weight'] + 6.25 * user['Height']/100 - 5 * user['Age'] - 161][0]
    #BMI
    user['BMI'] = user['Weight'] / ((user['Height'] / 100) ** 2)
    # Duration / Heart Rate
    user["Duration_per_HeartRate"] = user["Duration"] / (user["Heart_Rate"] + 1e-5)
        # Intensity
    user['Intensity'] = user["Heart_Rate"] / (user["Duration"] + 1e-5)

        # Other
    user["Duration_x_HeartRate"] = user["Duration"] * user["Heart_Rate"]

        # Label Encode
    user['Sex']=[0 if user['Sex']=='female' else 1][0]

    # Clustering features
    clustering_features = ['Age', 'Height', 'Duration', 'Heart_Rate', 'Body_Temp']
    for feature in clustering_features:
        user[f'{feature}_clusters']=joblib.load(f'parameters/{feature}_kmeans.pkl').predict(\
            pd.DataFrame([[user[feature]]],columns=[feature])).item()
    
    # return pd.DataFrame([user])
    return user

def trained_model():
    with open("model/calories_prediction_model.pkl", "rb") as f:
         model = pickle.load(f)
    return model         
# if __name__ == "__main__":
#     feature_values=feature_engineering()
#     with open("model/calories_prediction_model.pkl", "rb") as f:
#          model = pickle.load(f)
#     prediction=model.predict(pd.DataFrame([feature_values])).item()
#     print(prediction)


    
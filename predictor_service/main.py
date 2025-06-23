# FastAPI Microservice
from fastapi import FastAPI
from pydantic import BaseModel
from predictor import feature_engineering, trained_model
import pandas as pd
app = FastAPI()

model=trained_model()

class UserInput(BaseModel):
    Sex: str
    Age: int
    Height: float
    Weight: float
    Duration: float
    Heart_Rate: int
    Body_Temp: float

@app.post("/predict")
def predict(user_input: UserInput):
    features = feature_engineering(user_input=user_input)
    features_df = pd.DataFrame([features])
    prediction = model.predict(features_df)
    return {"prediction":prediction.item()}

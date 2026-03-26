from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pickle

app = FastAPI()

# Load model
loaded_model = pickle.load(open("sonar_model.sav","rb"))

# Define input structure
class SonarData(BaseModel):
    data: list[float]

@app.get("/")
def home():
    return {"message":"SONAR API is running"}

@app.post("/predict")
def predict(input: SonarData):

    input_data = np.asarray(input.data)
    input_reshaped = input_data.reshape(1,-1)

    prediction = loaded_model.predict(input_reshaped)

    if prediction[0] == "R":
        result = "Rock"
    else:
        result = "Mine"

    return {"Prediction": result}
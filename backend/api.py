# backend/api.py
import os
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(title="Core Liver Diagnostic Service")

# Locate serialized pipeline objects in the 'core' folder
CORE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'core'))
scaler = joblib.load(os.path.join(CORE_DIR, 'production_scaler.joblib'))
model = joblib.load(os.path.join(CORE_DIR, 'best_liver_model.joblib'))

class PatientLabData(BaseModel):
    Age: int
    Gender: int
    Total_Bilirubin: float
    Direct_Bilirubin: float
    Alkaline_Phosphotase: int
    Alamine_Aminotransferase: int
    Aspartate_Aminotransferase: int
    Total_Protiens: float
    Albumin: float
    Albumin_and_Globulin_Ratio: float

@app.post("/predict")
def run_predict(patient: PatientLabData):
    # Assemble feature vector matching original feature matrix dimensions
    features = np.array([[
        patient.Age, patient.Gender, patient.Total_Bilirubin, patient.Direct_Bilirubin,
        patient.Alkaline_Phosphotase, patient.Alamine_Aminotransferase, 
        patient.Aspartate_Aminotransferase, patient.Total_Protiens, 
        patient.Albumin, patient.Albumin_and_Globulin_Ratio
    ]])
    
    # Scale and make prediction
    scaled_features = scaler.transform(features)
    prediction = int(model.predict(scaled_features)[0])
    probability = float(model.predict_proba(scaled_features)[0][1])
    
    return {
        "disease_detected": True if prediction == 1 else False,
        "risk_percentage": round(probability * 100, 2)
    }

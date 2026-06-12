import os
import joblib
import numpy as np
import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# 1. Initialize the FastAPI application
app = FastAPI(title="Liver Disease Diagnostic Backend", version="1.0")

# 🔴 THE FIX: Enable CORS so your Streamlit frontend can connect safely
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows any frontend website to access this API
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP actions (POST, GET, etc.)
    allow_headers=["*"],  # Allows all headers
)

# 2. Define the exact path to your trained models
# Looks inside the core/ folder where train.py saves them
MODEL_PATH = os.path.join("..", "core", "best_liver_model.joblib")
SCALER_PATH = os.path.join("..", "core", "production_scaler.joblib")

# Fallback pathing in case Render executes from the root directory
if not os.path.exists(MODEL_PATH):
    MODEL_PATH = os.path.join("core", "best_liver_model.joblib")
    SCALER_PATH = os.path.join("core", "production_scaler.joblib")

# 3. Load the machine learning assets into system memory
try:
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    print("[+] Successfully loaded clinical model and scaler assets.")
except Exception as e:
    print(f"[-] Critical Error loading assets: {str(e)}")
    model = None
    scaler = None

# 4. Define the incoming patient data structure using Pydantic
class PatientData(BaseModel):
    Age: float
    Gender: int  # 1 = Male, 0 = Female
    Total_Bilirubin: float
    Direct_Bilirubin: float
    Alkaline_Phosphotase: float
    Alamina_Aminotransferase: float
    Aspartate_Aminotransferase: float
    Total_Protiens: float
    Albumin: float
    Albumin_and_Globulin_Ratio: float

@app.get("/")
def read_root():
    return {"status": "healthy", "message": "Liver Disease Prediction API is operational."}

@app.post("/predict")
def predict_risk(patient: PatientData):
    if model is None or scaler is None:
        raise HTTPException(status_code=500, detail="Machine learning models are not loaded on the server.")
    
    try:
        # Convert incoming JSON data into a dataframe row
        input_data = pd.DataFrame([patient.dict()])
        
        # Scale the features using the frozen production scaler
        scaled_features = scaler.transform(input_data)
        
        # Run inference using the winning Random Forest model weights
        prediction = model.predict(scaled_features)[0]
        probability = model.predict_proba(scaled_features)[0][1]
        
        # Return structured response to frontend
        return {
            "risk_status": int(prediction),  # 1 = High Risk, 0 = Low Risk
            "confidence_score": float(probability)
        }
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Inference error: {str(e)}")

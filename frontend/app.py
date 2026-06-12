import streamlit as st
import requests

st.set_page_config(page_title="Liver Health Dashboard", page_icon="🧪", layout="centered")
st.title("🧪 Real-Time Liver Function Diagnostic Engine")
st.write("Provide laboratory analytics below to run an instant diagnostic assessment loop.")

col1, col2 = st.columns(2)

with col1:
    age = st.slider("Patient Age", 1, 100, 45)
    gender = st.selectbox("Biological Gender", ["Male", "Female"])
    tot_bil = st.number_input("Total Bilirubin (mg/dL)", value=1.0)
    dir_bil = st.number_input("Direct Bilirubin (mg/dL)", value=0.3)
    alk_phos = st.number_input("Alkaline Phosphotase (IU/L)", value=150)

with col2:
    alt = st.number_input("Alamine Aminotransferase / SGPT (IU/L)", value=35)
    ast = st.number_input("Aspartate Aminotransferase / SGOT (IU/L)", value=30)
    proteins = st.number_input("Total Proteins (g/dL)", value=6.8)
    albumin = st.number_input("Albumin (g/dL)", value=3.5)
    ag_ratio = st.number_input("Albumin and Globulin Ratio", value=1.0)

if st.button("Execute Real-Time Diagnosis", type="primary"):
   payload = {
        "Age": float(age),
        "Gender": 1 if gender == "Male" else 0,
        "Total_Bilirubin": float(tot_bil),
        "Direct_Bilirubin": float(dir_bil),
        "Alkaline_Phosphotase": float(alk_phos),
        "Alamina_Aminotransferase": float(alt),  # 🔴 FIXED: Changed from Alamine to Alamina
        "Aspartate_Aminotransferase": float(ast),
        "Total_Protiens": float(proteins),
        "Albumin": float(albumin),
        "Albumin_and_Globulin_Ratio": float(ag_ratio)
    }
    
    # 🔴 ADDED THE MISSING ENDPOINT LINK: /predict
    BACKEND_URL = "https://liver-backend-nrjs.onrender.com/predict"
    
    try:
        response = requests.post(BACKEND_URL, json=payload)
        if response.status_code == 200:
            output = response.json()
            
            # Extract data using the exact keys your backend sends back
            risk_status = output["risk_status"]  # 1 = High Risk, 0 = Low Risk
            confidence = round(output["confidence_score"] * 100, 2)
            
            st.write("---")
            if risk_status == 1:
                st.error(f"🚨 **High Risk Warning:** Active tissue degeneration indicators tracked (Confidence Score: {confidence}%).")
            else:
                st.success(f"💚 **Low Risk Confirmed:** Patient blood work falls within normal functioning baseline metrics. (Confidence Score: {100 - confidence}%)")
        else:
            st.error(f"Server processing rejection. Error Code: {response.status_code}")
    except Exception as e:
        st.error(f"API link unreachable. Technical details: {str(e)}")

# 🩺 Liver Disease Risk Prediction System

A Machine Learning-based web application that predicts the likelihood of liver disease using patient clinical data.

This project follows a complete end-to-end workflow, including data preprocessing, model training, backend API development, and frontend deployment. Users can enter patient health parameters through an interactive web interface and receive real-time disease risk predictions.

Key Components
Machine Learning Pipeline for data preprocessing, feature engineering, model training, and evaluation
FastAPI Backend for serving prediction requests through REST APIs
Streamlit Frontend for an interactive and user-friendly interface
Model Comparison Framework to evaluate multiple machine learning algorithms and select the best-performing model
---

# 📌 Project Architecture

The application is organized into three independent modules:

```text
Liver-Disease-Risk-Prediction/
│
├── core/
│   ├── train.py
│   ├── target_distribution.png
│   ├── correlation_matrix.png
│   ├── datasets/
│   ├── models/
│   └── preprocessing/
│
├── backend/
│   ├── api.py
│   └── requirements.txt
│
├── frontend/
│   ├── app.py
│   └── requirements.txt
│
└── README.md
```

---

# 🚀 Features

### Machine Learning Pipeline

* Data preprocessing and cleaning
* Feature engineering
* Model training and evaluation
* Multiple model comparison
* Model persistence for deployment

### Backend API

* Built using **FastAPI**
* RESTful prediction endpoints
* Fast inference performance
* JSON-based communication

### Frontend Dashboard

* Built using **Streamlit**
* Interactive patient data input
* Real-time prediction results
* Clean and intuitive user interface

### End-to-End Workflow

```text
Patient Data
      ↓
Data Preprocessing
      ↓
Trained ML Model
      ↓
FastAPI Backend
      ↓
Streamlit Frontend
      ↓
Risk Prediction Output
```

---

# 📊 Exploratory Data Analysis (EDA)

## Target Label Balance

![Target Label Balance](core/target_distribution.png)

### Purpose

Understanding class distribution is critical in medical datasets because severe imbalance can lead to biased predictions and poor generalization.

---

## Feature Interaction Correlations

![Feature Interaction Correlations](core/correlation_matrix.png)

### Purpose

Correlation analysis helps identify:

* Highly related features
* Potential multicollinearity
* Important feature interactions
* Data-driven feature selection opportunities

---

# 🤖 Machine Learning Models Evaluated

The following classification models were trained and compared.

| Model Architecture     | Accuracy | Precision | Recall (Sensitivity) | F1-Score |
| ---------------------- | -------- | --------- | -------------------- | -------- |
| KNN                    | 65.52%   | 73.12%    | 81.93%               | 77.27%   |
| Decision Tree          | 71.55%   | 77.78%    | 84.34%               | 80.92%   |
| Random Forest Ensemble | 73.28%   | 75.49%    | 92.77%               | 83.24%   |
| XGBoost Framework      | 74.14%   | 76.53%    | 90.36%               | 82.87%   |

---

# 🏆 Best Performing Model

### XGBoost Framework

The XGBoost model achieved the highest overall accuracy while maintaining strong precision, recall, and F1-score performance.

### Key Advantages

* Excellent generalization capability
* Handles complex feature interactions
* Reduced overfitting compared to standalone trees
* Strong performance on structured healthcare datasets

---

# ⚠️ Why Recall (Sensitivity) Matters Most

In medical diagnosis systems, **Recall (Sensitivity)** is often the most important evaluation metric.

### Recall Formula

```text
Recall = True Positives / (True Positives + False Negatives)
```

### Why It Is Critical

A **False Negative** occurs when:

```text
Patient has liver disease
BUT
Model predicts healthy
```

This is the most dangerous error because:

* Disease remains undetected
* Treatment may be delayed
* Health complications may worsen
* Patient outcomes may be negatively affected

### Project Objective

The primary goal is to identify as many potentially affected patients as possible.

Therefore:

✅ High Recall = More diseased patients correctly detected

❌ Low Recall = Higher risk of missing actual cases

For healthcare applications, minimizing False Negatives is often more important than maximizing overall accuracy.

---

# 🛠️ Technology Stack

## Machine Learning

* Python
* Scikit-Learn
* XGBoost
* NumPy
* Pandas

## Data Visualization

* Matplotlib
* Seaborn

## Backend

* FastAPI
* Uvicorn

## Frontend

* Streamlit

---

# ⚙️ Installation & Setup

## 1. Clone Repository

```bash
git clone https://github.com/your-username/liver-disease-risk-prediction.git
cd liver-disease-risk-prediction
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Complete System

Open **three separate terminal windows**.

---

## Window 1 — Train the Model

Navigate to the core directory:

```bash
cd core
python train.py
```

This step:

* Loads the dataset
* Performs preprocessing
* Trains the model
* Saves trained artifacts

---

## Window 2 — Start FastAPI Backend

Navigate to the backend directory:

```bash
cd backend
uvicorn api:app --reload
```

Backend will start at:

```text
http://127.0.0.1:8000
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Window 3 — Launch Streamlit Frontend

Navigate to the frontend directory:

```bash
cd frontend
streamlit run app.py
```

The Streamlit application will open automatically in your browser.

---

# 📡 API Workflow

```text
Streamlit Frontend
        ↓
FastAPI Backend
        ↓
ML Prediction Model
        ↓
Prediction Result
        ↓
Frontend Display
```

---

# 📈 Future Improvements

* Advanced feature engineering
* Hyperparameter optimization
* Explainable AI (SHAP/LIME)
* Docker containerization
* Cloud deployment
* Continuous model monitoring
* Electronic Health Record (EHR) integration

---

# 🎯 Project Highlights

✅ End-to-End Machine Learning Workflow

✅ Healthcare-Oriented Risk Prediction

✅ FastAPI Production Backend

✅ Streamlit Interactive Dashboard

✅ Multiple Model Benchmarking

✅ Automated Training Pipeline

✅ Medical Metric Focus (Recall Optimization)

✅ Recruiter-Friendly Architecture

---

# 👩‍💻 Author

**Durga Devi Ravipati**

B.Tech – Computer Science & Engineering (Cyber Security)

Passionate about:

* Machine Learning
* Artificial Intelligence
* Full Stack Development
* Healthcare AI Solutions

---

# ⭐ Acknowledgements

Special thanks to the open-source community and the developers of:

* Scikit-Learn
* XGBoost
* FastAPI
* Streamlit
* Pandas
* NumPy
* Matplotlib

for providing the tools that made this project possible.

---

## 📜 License

This project is intended for educational, research, and portfolio purposes.

Please verify all medical decisions with qualified healthcare professionals. This system is designed to assist prediction workflows and should not replace professional medical diagnosis.

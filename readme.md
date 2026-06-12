# 🩺 Liver Disease Risk Prediction System

A production-ready Machine Learning application that predicts the risk of liver disease using patient clinical and laboratory data. The project implements a complete end-to-end ML workflow, including data preprocessing, exploratory data analysis (EDA), model training, evaluation, API development, and web application deployment.

The system enables users to enter patient health parameters and receive real-time liver disease risk predictions through a FastAPI backend and Streamlit frontend.

---

## 📌 Project Overview

Liver disease is a significant global health concern, and early detection is critical for effective treatment and improved patient outcomes. This project leverages supervised machine learning algorithms to identify potential liver disease cases based on patient health indicators.

### Key Objectives

- Develop an accurate liver disease prediction model
- Compare multiple machine learning algorithms
- Deploy the model through a scalable API
- Provide a user-friendly prediction interface
- Minimize false negatives in medical predictions

---

## 🏗️ System Architecture

```text
Patient Data
      │
      ▼
Data Preprocessing
      │
      ▼
Feature Engineering
      │
      ▼
Machine Learning Model
      │
      ▼
FastAPI Backend
      │
      ▼
Streamlit Frontend
      │
      ▼
Risk Prediction
```

---

## 📂 Project Structure

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
│   ├── model_loader.py
│   └── requirements.txt
│
├── frontend/
│   ├── app.py
│   └── requirements.txt
│
├── requirements.txt
└── README.md
```

---

## 🔬 Exploratory Data Analysis (EDA)

Exploratory Data Analysis was performed to understand the dataset, identify patterns, analyze feature relationships, and support model development.

### Target Label Distribution

![Target Label Balance](core/target_distribution.png)

#### Analysis

- Examined class distribution of target labels
- Identified potential class imbalance
- Evaluated the need for resampling techniques
- Ensured reliable model evaluation

---

### Feature Correlation Matrix

![Feature Interaction Correlations](core/correlation_matrix.png)

#### Analysis

- Identified relationships between features
- Detected highly correlated variables
- Evaluated multicollinearity
- Supported feature selection decisions

---

## ⚙️ Data Preprocessing Pipeline

The preprocessing workflow includes:

### Data Cleaning

- Handling missing values
- Removing inconsistent records
- Data validation and quality checks

### Feature Engineering

- Feature transformation
- Feature scaling and normalization
- Feature selection

### Dataset Preparation

- Train-test split
- Target encoding
- Input feature preparation

---

## 🤖 Machine Learning Models Evaluated

The following classification algorithms were trained and evaluated:

### 1. K-Nearest Neighbors (KNN)

A distance-based algorithm that classifies samples using the nearest neighboring data points.

### 2. Decision Tree

A tree-based supervised learning algorithm that generates interpretable decision rules.

### 3. Random Forest Ensemble

An ensemble model that combines multiple decision trees to improve generalization and reduce overfitting.

### 4. XGBoost Framework

A gradient boosting algorithm optimized for performance, scalability, and predictive accuracy.

---

## 📊 Model Performance Comparison

| Model Architecture | Accuracy | Precision | Recall (Sensitivity) | F1-Score |
|-------------------|----------|-----------|----------------------|----------|
| KNN | 65.52% | 73.12% | 81.93% | 77.27% |
| Decision Tree | 71.55% | 77.78% | 84.34% | 80.92% |
| Random Forest Ensemble | 73.28% | 75.49% | 92.77% | 83.24% |
| XGBoost Framework | 74.14% | 76.53% | 90.36% | 82.87% |

---

## 🏆 Best Performing Model

### XGBoost Framework

XGBoost achieved the highest overall accuracy while maintaining strong precision, recall, and F1-score values across the evaluation dataset.

### Advantages

- Strong predictive performance
- Efficient gradient boosting implementation
- Handles complex feature interactions
- Good generalization capability
- Robust performance on structured healthcare datasets

---

## 🚨 Why Recall (Sensitivity) Matters Most

For medical diagnosis systems, **Recall (Sensitivity)** is often the most important evaluation metric.

### Formula

```text
Recall = True Positives / (True Positives + False Negatives)
```

### Why It Is Critical

A **False Negative** occurs when:

```text
Actual Condition : Liver Disease Present
Prediction       : Healthy
```

This is the most dangerous error because:

- The disease remains undetected
- Treatment may be delayed
- Clinical intervention may not occur in time
- Patient outcomes may worsen

### Project Goal

The primary objective is to identify as many patients with liver disease as possible.

✅ High Recall → More diseased patients correctly identified

❌ Low Recall → Higher risk of missing actual disease cases

For this reason, Recall was treated as a key evaluation metric during model selection.

---

## 🚀 Technology Stack

### Programming Language

- Python

### Machine Learning

- Scikit-Learn
- XGBoost

### Data Processing

- Pandas
- NumPy

### Data Visualization

- Matplotlib
- Seaborn

### Backend

- FastAPI
- Uvicorn

### Frontend

- Streamlit

---

## ⚡ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/liver-disease-risk-prediction.git
cd liver-disease-risk-prediction
```

### Create Virtual Environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS**

```bash
python -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

Open **three separate terminal windows**.

### Window 1 — Train the Model

```bash
cd core
python train.py
```

This step:

- Loads the dataset
- Performs preprocessing
- Trains machine learning models
- Saves trained model artifacts

---

### Window 2 — Start FastAPI Backend

```bash
cd backend
uvicorn api:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

API Documentation:

```text
http://127.0.0.1:8000/docs
```

---

### Window 3 — Launch Streamlit Frontend

```bash
cd frontend
streamlit run app.py
```

Frontend URL:

```text
http://localhost:8501
```

---

## 🔌 API Workflow

```text
Streamlit Frontend
        │
        ▼
FastAPI Backend
        │
        ▼
Trained ML Model
        │
        ▼
Prediction Result
```

---

## 📈 Future Enhancements

- Hyperparameter tuning
- Explainable AI using SHAP
- Docker containerization
- CI/CD integration
- Cloud deployment
- Model monitoring
- Automated retraining pipeline

---

## 🎯 Key Highlights

- End-to-End Machine Learning Workflow
- Healthcare Risk Prediction Application
- FastAPI REST API Deployment
- Interactive Streamlit Dashboard
- Multiple Model Benchmarking
- Comprehensive EDA
- Recall-Oriented Model Evaluation
- Modular and Scalable Architecture

---

## 👩‍💻 Author

**Durga Devi Ravipati**

B.Tech, Computer Science & Engineering (Cyber Security)

### Areas of Interest

- Machine Learning
- Artificial Intelligence
- Data Science
- Healthcare Analytics
- Full Stack Development

GitHub: https://github.com/DurgaDevi335

---

## 📜 Disclaimer

This project is intended for educational, research, and portfolio purposes only. Predictions generated by the system should not be used as a substitute for professional medical diagnosis, treatment, or clinical decision-making.

---

⭐ If you found this project useful, consider giving it a star!

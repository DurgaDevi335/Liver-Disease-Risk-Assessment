# core/train.py
import os
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Import all 4 required models
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

# ==========================================
# 1. LOAD DATASET
# ==========================================
data_path = os.path.join('..', 'data', 'HealthCareData.csv')
if not os.path.exists(data_path):
    data_path = os.path.join('data', 'HealthCareData.csv')

dataset = pd.read_csv(data_path)

# ==========================================
# 2. EXPLORATORY DATA ANALYSIS (EDA) PHASE
# ==========================================
print("--- Launching Exploratory Data Analysis (EDA) ---")

# Chart A: Target Label Distribution
plt.figure(figsize=(6, 4))
sns.countplot(x='Dataset', data=dataset, palette='Set2')
plt.title('Distribution of Target Labels (1: Disease, 2: Healthy)')
plt.xlabel('Diagnosis Label')
plt.ylabel('Patient Count')
plt.tight_layout()
plt.savefig('target_distribution.png')
plt.close()

# Temporary encoded dataset copy to safely plot a numerical correlation heatmap
eda_copy = dataset.copy()
eda_copy['Gender'] = eda_copy['Gender'].map({'Male': 1, 'Female': 0})

# Chart B: Feature Correlation Heatmap Matrix
plt.figure(figsize=(10, 8))
sns.heatmap(eda_copy.corr(), annot=True, fmt='.2f', cmap='coolwarm', linewidths=0.5)
plt.title('Feature Correlation Matrix Heatmap')
plt.tight_layout()
plt.savefig('correlation_matrix.png')
plt.close()
print("Saved EDA plots: 'target_distribution.png' and 'correlation_matrix.png'")

# ==========================================
# 3. PREPROCESSING: HANDLING MISSING VALUES
# ==========================================
for column in dataset.columns:
    if dataset[column].isnull().sum() > 0:
        dataset[column].fillna(dataset[column].median(), inplace=True)

# ==========================================
# 4. PREPROCESSING: CATEGORICAL DATA ENCODING
# ==========================================
dataset['Gender'] = dataset['Gender'].map({'Male': 1, 'Female': 0})
dataset['Dataset'] = dataset['Dataset'].replace({2: 0}) # 1 = Disease, 0 = Healthy

# ==========================================
# 5. PREPROCESSING: OUTLIER HANDLING (IQR FENCE)
# ==========================================
numerical_cols = ['Total_Bilirubin', 'Direct_Bilirubin', 'Alkaline_Phosphotase', 
                  'Alamine_Aminotransferase', 'Aspartate_Aminotransferase', 
                  'Total_Protiens', 'Albumin', 'Albumin_and_Globulin_Ratio']

for col in numerical_cols:
    Q1 = dataset[col].quantile(0.25)
    Q3 = dataset[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    dataset[col] = np.clip(dataset[col], lower_bound, upper_bound)

# Split features and target labels
X = dataset.drop('Dataset', axis=1)
y = dataset['Dataset']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

# ==========================================
# 6. PREPROCESSING: COLUMN STANDARDIZATION
# ==========================================
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Save the scaling state
joblib.dump(scaler, 'production_scaler.joblib')

# ==========================================
# 7. MODEL TRAINING AND ALL-METRIC COMPARISON
# ==========================================
models = {
    "KNN": KNeighborsClassifier(n_neighbors=5),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42),
    "XGBoost": XGBClassifier(random_state=42, eval_metric='logloss')
}

best_accuracy = 0
best_model_name = ""
best_model_obj = None
comparison_records = []

print("\n==================================================================")
print("              MULTI-ARCHITECTURE BENCHMARK PARADIGM               ")
print("==================================================================")

for name, model in models.items():
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    
    # Compute all 4 core classification metrics
    acc = accuracy_score(y_test, y_pred)
    pre = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    f1  = f1_score(y_test, y_pred)
    
    comparison_records.append({
        "Model": name, 
        "Accuracy": acc,
        "Precision": pre,
        "Recall": rec,
        "F1-Score": f1
    })
    
    print(f"\nModel Paradigm: [ {name} ]")
    print(f" └── Accuracy  : {acc*100:.2f}%")
    print(f" └── Precision : {pre*100:.2f}%")
    print(f" └── Recall    : {rec*100:.2f}%")
    print(f" └── F1-Score  : {f1*100:.2f}%")
    
    if acc > best_accuracy:
        best_accuracy = acc
        best_model_name = name
        best_model_obj = model

print("\n==================================================================\n")

# ==========================================
# 8. VISUAL ALL-METRIC SIDE-BY-SIDE GRAPH
# ==========================================
comparison_df = pd.DataFrame(comparison_records)
df_melted = pd.melt(comparison_df, id_vars="Model", var_name="Metric", value_name="Score")

plt.figure(figsize=(10, 5))
sns.barplot(x="Model", y="Score", hue="Metric", data=df_melted, palette="muted")
plt.title("Comprehensive Model Comparison Across All Metrics")
plt.ylim(0, 1.05)
plt.ylabel("Score Range (0.0 - 1.0)")
plt.xlabel("Machine Learning Algorithms")
plt.legend(loc="lower right")
plt.tight_layout()
plt.savefig('model_comparison.png')
plt.close()

# Export chosen pipeline winner
print(f"🏆 Model Pipeline Winner: {best_model_name} ({best_accuracy*100:.2f}%)")
joblib.dump(best_model_obj, 'best_liver_model.joblib')
print("Successfully generated and saved core deployment binaries!")
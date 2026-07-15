# ❤️ Heart Disease Prediction using Machine Learning

## 📌 Project Overview

Heart Disease Prediction is a Machine Learning classification project that predicts whether a person is likely to have heart disease based on various medical attributes.

The goal of this project is to build an end-to-end ML pipeline that includes data preprocessing, feature engineering, handling class imbalance, model training,model evaluation, and deployment using a web application.

This project helps demonstrate how machine learning can assist in early detection of cardiovascular disease risks.

---

🌐 Live Demo

🚀 Try the deployed application here:

https://heart-disease-prediction-end-to-end-ml-2.onrender.com

Note: Since the application is hosted on Render's free tier, it may take 30–60 seconds to load if it has been inactive.

# 🎯 Problem Statement

Heart disease is one of the leading causes of death worldwide. Early prediction can help healthcare professionals identify high-risk patients and provide timely treatment.

The objective of this project is to develop a classification model that predicts the presence or absence of heart disease using patient health information.

---

# 📂 Dataset Information

The dataset contains medical records with various patient attributes.

### Features:

| Feature | Description |
|---------|-------------|
| Age | Age of the patient |
| Sex | Gender of the patient |
| ChestPainType | Type of chest pain experienced |
| RestingBP | Resting blood pressure |
| Cholesterol | Serum cholesterol level |
| FastingBS | Fasting blood sugar |
| RestingECG | Resting electrocardiogram results |
| MaxHR | Maximum heart rate achieved |
| ExerciseAngina | Exercise induced angina |
| Oldpeak | ST depression induced by exercise |
| ST_Slope | Slope of peak exercise ST segment |
| HeartDisease | Target variable (0 = No Disease, 1 = Disease) |

---

# 🛠️ Technologies Used

### Programming Language
- Python

### Libraries

- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn

### Deployment

- Flask
- HTML
- CSS

### Development Tools

- Jupyter Notebook
- VS Code
- Git & GitHub
- Render

---

# 🔍 Exploratory Data Analysis (EDA)

Performed analysis to understand the dataset:

- Checking missing values
- Statistical analysis
- Distribution analysis of numerical features
- Feature relationship visualization

# ⚙️ Machine Learning Workflow

The complete pipeline consists of:

## 1. Data Ingestion

- Loaded the dataset
- Performed initial data checks
- Split data into training and testing sets

---

## 2. Data Preprocessing

### Numerical Features:

Applied:

- Missing value handling
- Feature scaling using StandardScaler

### Categorical Features:

Applied:

- One Hot Encoding

### ColumnTransformer:

Used to apply different transformations to numerical and categorical features.

---


# 🤖 Machine Learning Models Used

The following classification algorithms were trained and evaluated:

- Logistic Regression
- Random Forest Classifier
- Support Vector Machine (SVM)
- K-Nearest Neighbors
- Decision Tree Classifier
- Adaboost Classifier
- Gradient Boost Classifier
- XGB Classifier 
- Catboost classifier 

---

# 📊 Model Evaluation Metrics

The models were evaluated using:

### F1 Score

Balances precision and recall.

### ROC-AUC Score

Measures model's ability to distinguish between classes.

---

# 📈 Results

The best performing model was selected based on evaluation metrics.

Final model achieved:

- High f1 score
- Good roc auc score for heart disease detection

---

# 🌐 Deployment

The trained model was deployed using Flask and Render.

The web application allows users to enter patient medical details and receive a prediction.

### Application Features:

- User-friendly interface
- Takes patient health parameters as input
- Predicts heart disease risk instantly

---

# 📁 Project Structure
Heart-Disease-Prediction/

│
├── artifacts/
│ ├── model.pkl
│ └── preprocessing.pkl
│
├── notebooks/
│ └── feature_engg_EDA.ipynb
│
├── src/
│ ├── components/
│ │ ├── data_ingestion.py
│ │ ├── data_transformation.py
│ │ └── model_trainer.py
│ │
│ ├── pipeline/
│ │ └── predict_pipeline.py
│ │
│ ├── logger.py
│ └── exception.py
│
├── templates/
│ └── home.html
│
├── app.py
├── requirements.txt
├── README.md
└── setup.py


---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/Diksha-ydv/Heart-Disease-Prediction-End-to-End-ML
```

Move into the project directory

```bash
cd Heart-Disease-Prediction-End-to-End-ML
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open your browser and visit

```
http://localhost:8000
```

---
Future Improvements:

Deploy using AWS / Azure 
Add real-time patient database integration
Improve model performance using advanced ensemble methods
Add more explainability features
Integrate deep learning models

## 👩‍💻 Author

**Diksha Yadav**

GitHub: https://github.com/Diksha-ydv

---

## ⭐ Show Your Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

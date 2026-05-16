# 🫀 Heart Stroke Prediction using Logistic Regression
## Project Objective
The objective of this project is to build a Machine Learning model that predicts the risk of heart disease based on various medical and health-related parameters. The goal is to assist in early detection and support healthcare decision-making using data-driven insights.

## Project Description
- This project focuses on predicting heart disease risk using a Logistic Regression model trained on a healthcare dataset.
- It involves data preprocessing, feature engineering, exploratory data analysis (EDA), model training, and evaluation.
- A user-friendly web application was also developed using Streamlit for real-time predictions.


## Key Performance Indicators (KPIs)
- Age
- Sex
- Chest Pain Type
- Resting Blood Pressure
- Cholesterol Level
- Fasting Blood Sugar
- Resting ECG Results
- Maximum Heart Rate
- Exercise-Induced Angina
- Oldpeak (ST Depression)
- ST Slope
- Heart Disease Risk (Target Variable)

## Dataset used
- <a href="/kaggle/input/datasets/adhurimquku/ford-car-price-prediction/ford.csv">Dataset</a>

# Project Process

## 1️. Data Collection
- The dataset was sourced from Kaggle and contains medical records related to heart disease prediction.
- It includes both categorical and numerical healthcare attributes.

## 2️. Data Cleaning & Preparation
- Handled missing and null values
- Removed duplicate records
- Encoded categorical variables
- Checked and corrected data types
- Applied feature scaling using StandardScaler

## 3️. Exploratory Data Analysis (EDA)
- Analyzed relationships between health factors and heart disease
- Visualized trends and distributions using charts and graphs
- Identified patterns and outliers in the dataset
- Studied feature impact on prediction outcomes

## 4️. Feature Engineering & Correlation Analysis
- Performed correlation analysis to identify important features
- Removed irrelevant or less impactful variables
- Prepared optimized feature set for model training

## 5️. Model Development
- Implemented Logistic Regression algorithm
- Split data into training and testing datasets
- Trained the model on scaled data
- Saved trained model using Joblib

## 6️. Model Evaluation
- Evaluated model performance using Accuracy Score
- Tested prediction reliability on unseen data
- Achieved effective prediction performance for heart disease classification

# Web Application Development
- Built an interactive web application using Streamlit
- Designed a responsive multi-column UI
- Added real-time prediction functionality
- Improved user experience with custom styling and layout

# Tech Stack
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib
- Matplotlib / Seaborn

## User Interface
- <a href="">View User Interface</a>
# Project Insights
- Chest pain type and maximum heart rate significantly influence prediction
- Higher cholesterol and resting blood pressure increase heart disease risk
- Exercise-induced angina is an important indicator
- Age and ST slope also contribute strongly to prediction results

# Conclusion
This project demonstrates how Machine Learning can assist in predicting heart disease risk effectively. The Logistic Regression model provides reliable classification results, while the Streamlit web application enables users to interact with the model easily through a modern interface.

# Future Scope
- Implement advanced ML models like Random Forest and XGBoost
- Add probability-based risk visualization
- Deploy application on cloud platforms
- Integrate real-time healthcare analytics
- Improve model accuracy using hyperparameter tuning

import streamlit as st
import pandas as pd
import joblib

model = joblib.load("Log_reg_heart.pkl")
scaler =joblib.load("scaler.pkl")
expected_columns = joblib.load("Columns.pkl")

st.title("Heart Stroke Prediction")
st.markdown()

import pandas as pd
import streamlit as st
import pickle
# with open('model_pickle','rb') as file:
#     x =pickle.load(file)
import joblib

model = joblib.load('model_joblib')
st.title("House Price Prediction")
area = st.number_input("Enter the area")

def prediction(area):
    p = model.predict([[area]])
    return p

if(st.button("Predict")):
    result = prediction(area)
    st.success("The Predicted price is {}".format(result))
    
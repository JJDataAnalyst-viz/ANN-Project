import streamlit as st
import numpy as np
import tensorflow as tf
import pickle
import pandas as pd
import keras
import time

model = keras.models.load_model('notebooks/mlruns/models/model.keras')

# with open('notebooks/mlruns/models/xgb_model.pkl','rb') as f:
#     model = pickle.load(f)

# Przykład z przyciskiem



with open('artifacts/preprocess.pkl','rb') as f:
    preprocess = pickle.load(f)


cat_pipeline = preprocess.named_transformers_['cat_preprocessed']
one_hot_encoder = cat_pipeline.named_steps['OneHotEncoder']


st.title('Prediction of customer churn')

CreditScore = st.number_input('CreditScore')
Geography = st.selectbox('Geography',one_hot_encoder.categories_[0])
Gender = st.selectbox('Gender',one_hot_encoder.categories_[1])
Age = st.slider('Age',12,92)
Tenure = st.slider("Tenure",0,10)
Balance = st.number_input('Balance',step=1)
NumOfProducts =st.slider("Number of Products",1,4)
HasCrCard = st.selectbox("Has a Credit Card",[0,1])
IsActiveMember = st.selectbox("Is Active Member",[0,1])
EstimatedSalary = st.number_input("Estimated Salary",step=1)

input_data = pd.DataFrame({
    'CreditScore': [CreditScore],
    'Geography':[Geography],
    'Gender' :[Gender],
    'Age':[Age],
    'Tenure':[Tenure],
    'Balance':[Balance],
    'NumOfProducts' :[NumOfProducts],
    'HasCrCard':[HasCrCard],
    'IsActiveMember':[IsActiveMember],
    'EstimatedSalary' :[EstimatedSalary]
})


input_data_scaled = preprocess.transform(input_data)
pred = model.predict(input_data_scaled)
pred = np.squeeze(pred)*100
st.write(f'Churn prediction probability is {np.round(pred,decimals=0)} %')

if np.squeeze(pred) > 0.5:
    st.write('Customer is likely to churn')
else:
    st.write('Customer is not likely to churn')

import streamlit as st
import pandas as pd
import numpy as np
import pickle #to load a saved model

pickle_in = open('model_uas.pkl', 'rb')
nb = pickle.load(pickle_in)

def prediction(age, sex, bmi, children, smoker):

    prediction = nb.predict([[age, sex, bmi, children, smoker]])
    print(prediction)
    return prediction

app_mode = st.sidebar.selectbox('Select Page',['Home','Prediction']) #two pages

if app_mode=='Home':
    st.title('Prediksi Pembayaran Premi Asuransi :') 
    st.title("Aplikasi Prediksi Pembayaran Premi Asuransis Dengan Algoritma Regresi Linier")
    st.write("Fauzan Samy Nadzeva_2019230087")
    st.markdown('Dataset :')
    data=pd.read_csv('insurance1.csv')
    st.write(data.head())

elif app_mode == 'Prediction':
    st.write('\n')
    st.markdown('Silakan, isi form berikut ini :')
    
    st.write('\n')
    age = st.number_input("Age", 0)
    sex = st.number_input("Sex", 0)
    bmi = st.number_input("BMI", 0)
    children = st.number_input("Children", 0)
    smoker = st.number_input("Smoker", 0)
    result =""
    
    if st.button("KLIK DI SINI UNTUK PREDIKSI"):
        result = prediction(age, sex, bmi, children, smoker)
    st.success('Hasil Prediksi = {}'.format(result))
    
 
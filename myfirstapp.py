import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import time


st.header("Body Mass Index (BMI) Calculator")

from PIL import Image
image = Image.open('bmi.jpg')
st.image(image, caption='Body mass index')

st.write("This app calculate BMI for adult (age 18 years and above only)")

st.sidebar.header("Body Mass Index")
st.sidebar.write("Body Mass Index or BMI refers to  defined as a person’s weight in kilograms divided by the square of the person’s height in metres")

st.sidebar.header("Precaution")
st.sidebar.write("BMI screens for weight categories that may lead to health problems, but it does not diagnose the body fatness or health of an individual. Other health screening is needed to determine the health status of an individual")

data = {'BMI': ['Below 18.5','18.5 - 24.9', '25 - 29.9', '30 - 34.9', '35 and above'],'Classification': ['Underweight','Normal', 'Overweight', 'Obese', 'Extremely obese'] }
df = pd.DataFrame(data)
st.sidebar.header("BMI Classification")
st.sidebar.write(df)


option = st.selectbox(
    'Select gender',
     ['Male','Female'])

if option=='Male':

    age = ['18-19', '20-29', '30-39','40-49', '50-59' ]
    fig = go.Figure([go.Bar(x=age, y=[21.75, 24.43, 25.62, 25.77, 25.61])])
    fig.show()
    fig.update_layout(title='Mean BMI of Men in Malaysia , (*National Health and Morbidity Survey 2014*)')
    st.plotly_chart(fig, caption='Mean BMI of Men in Malaysia')


elif option=='Female':
    age = ['18-19', '20-29', '30-39','40-49', '50-59' ]
    fig = go.Figure([go.Bar(x=age, y=[22.95, 24.92, 26.40, 27.07, 27.13])])
    fig.show()
    fig.update_layout(title='Mean BMI of Women in Malaysia , (*National Health and Morbidity Survey 2014*)')
    st.plotly_chart(fig)


age = st.slider('age', 18, 60, 30)
gender = st.radio ("gender:", ('Male','Female'))
Weight = st.number_input ("Please enter your weight (in kg):",min_value=1.0)
Height = st.number_input ("Please enter your height (in m):",min_value=1.0)
BMI = Weight / (Height ** 2)

def user_input_features():
    data = {'age': age,
            'gender': gender,
            'Weight': Weight,
            'Height': Height}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()
st.subheader('User Information')
st.write(df)
   
if(st.button("Calculate")):
  
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
   
        latest_iteration.text(f'Calculating {i+1}')
        bar.progress(i + 1)
        time.sleep(0.1)

    '...and now we\'re done!'

    st.text("Your BMI is " + str(round(BMI)))

    if (BMI < 18.5):
        st.warning ("Underweight")
    if (BMI >= 18.5 and BMI < 25):
        st.success ("Underweight")
    if (BMI >= 25 and BMI < 30):
        st.warning ("Overweight")
    if (BMI >= 30 and BMI < 35):
        st.error ("Obese")
    elif (BMI >= 35):
        st.error ("Extremely Obese")


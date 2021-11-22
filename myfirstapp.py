import streamlit as st
import numpy as np
import pandas as pd

st.header("Body Mass Index (BMI) Calculator")

from PIL import Image
image = Image.open('bmi.jpg')
st.image(image, caption='Body mass index')

st.write("This app calculate BMI for adult (age 18 years and above only)")

st.sidebar.header("Body Mass Index")
st.sidebar.write("Body Mass Index or BMI refers to  defined as a person’s weight in kilograms divided by the square of the person’s height in metres")

st.sidebar.header("Precaution")
st.sidebar.write("BMI screens for weight categories that may lead to health problems, but it does not diagnose the body fatness or health of an individual")

data = {'BMI': ['Below 18','18 - 25', '25 - 30'],'Classification': ['Underweight','Normal', 'Overweight'] }
df = pd.DataFrame(data)
st.sidebar.header("BMI Classification")
st.sidebar.write(df)

age = st.slider('age', 18, 100, 40)
gender = st.radio ("gender:", ('Male','Female'))
Weight = st.number_input ("Weight (in kg):",min_value=1.0)
Height = st.number_input ("Height (in m):",min_value=1.0)
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
    st.text("Your BMI is " + str(round(BMI)))

    if (BMI < 18):
        st.warning ("Underweight")
    if (BMI >= 18 and BMI < 25):
        st.success ("Underweight")
    if (BMI >= 25 and BMI < 30):
        st.warning ("Overweight")
    elif (BMI >= 30):
        st.error ("Obese")


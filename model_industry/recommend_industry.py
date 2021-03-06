import streamlit as st
import numpy as np
import pandas as pd
import random
from PIL import Image
import joblib
import json
from sklearn.preprocessing import LabelEncoder
import warnings

warnings.filterwarnings('ignore')


@st.cache(ttl=10)
def get_random_string():
    sentences = [
        '`Lisboa` was the `Residence District` most reported in the 2021 Tech Careers Survey PT?',
        '`34 years old` was the average `Age` of the workers that answered the 2021 Tech Careers Survey PT?',
        'workers in the `Security` industry reported the largest average value for `Salary Fairness` in the 2021 Tech Careers Survey PT?',
        'workers in the `Nonprofit` industry reported the largest average value for `Training/Development programs at work` as job motivator in the 2021 Tech Careers Survey PT?',
        'workers in the `Real estate` industry reported the largest average value for `Computer/Office equipment allowance` as job perk in the 2021 Tech Careers Survey PT?',
        'workers in the `Data and analytics` industry reported the largest average value for `Flexible schedule` as job motivator in the 2021 Tech Careers Survey PT?',
        'workers in the `Security` industry reported the largest average value for `Stock options or shares` as job perk in the 2021 Tech Careers Survey PT?']
    return random.choice(sentences)


@st.cache
def load_data():
    with open('./model_industry/data/employee_industry_labelencoder.joblib', 'rb') as fl:
        le = joblib.load(fl)
    with open('./model_industry/data/employee_industry_model.joblib', 'rb') as fm:
        model = joblib.load(fm)
    with open('./model_industry/data/employee_industry_features.json', 'r', encoding='utf8') as ff:
        features = json.load(ff)

    return le, features, model


def get_predict(row, le, model, feat_cols):
    df = pd.DataFrame([row], columns=feat_cols)
    df['Residence_District'] = df['Residence_District'].astype('category')
    pred = model.predict(df)

    return le.inverse_transform(pred)[0]


def app():
    st.header('Recommend Industry')
    
    st.text("\n")
    st.write("This page recommends the best industry to work in depending on profile and preferences")
    st.markdown("***")

    left_column, center_column, right_column = st.beta_columns((1, 0.25, 0.5))

    le, features, model = load_data()
    
    with left_column:
        st.write('Add the profile and preferences and press the button at the end')
        
        residence_district = st.selectbox("Residence District", (sorted(features['Residence_District'])), index = 10,
                                          format_func=lambda x: 'Residence District' if x == '' else x)
        age = st.slider("Age (Years)", 16, 67, 42, 1)
        salary_fairness = st.slider("How important is Salary Fairness", 1, 7, 4, 1)
        training = st.slider("How important are Training/Development programs at work", 1, 7, 4, 1)
        equipment_allowance = st.slider("How important is Allowance for Computer / Office equip", 1, 7, 4, 1)
        flexible_schedule = st.slider('How important is Flexible schedule', 1, 7, 4, 1)
        stock_options = st.slider("How important are Stock options or shares", 1, 7, 4, 1)

        row = [residence_district, age, salary_fairness, training, equipment_allowance, flexible_schedule,
               stock_options]

        feat_cols = ['Residence_District',
                     'Age',
                     'Salary_Fairness',
                     'Job_Motivator_Training/Development_programs_at_work',
                     'Job_Perk_Computer/_Office_equipment_allowance',
                     'Job_Motivator_Flexible_schedule',
                     'Job_Perk_Stock_options_or_shares']

        st.text("\n")
        if st.button('Recommend Industry'):
            result = get_predict(row, le, model, feat_cols)
            st.write(f'According to your profile and preferences, the best industry to work in is: `{result}`')

        st.markdown("***")
    
    with right_column:
        image = Image.open('images/question-mark.png')
        image = image.resize((125, 125), Image.ANTIALIAS)
        st.image(image)
        st.write('Did you know that ' + get_random_string())

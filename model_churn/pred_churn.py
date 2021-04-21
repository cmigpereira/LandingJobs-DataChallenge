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
        '`Younger` people are more likely to churn in the next few months',
        'people who live in `Beja` are the ones who most want to leave the company where they work, followed by those who live in `Bragança`?', 
        'one of the main factors that lead people to churn is `Salary Fairness`?', 
        'one of the main factors that lead people to churn is the `Salary Change` in recent months?', 
        '`Females` are more likely to leave their jobs in the next few months than `Males`?', 
        'people working `In-Office` are more likely to leave their jobs than those working in `Full Remote`?', 
        'people working in `Consultancy` industry are more willing to churn than people working in other industries?']
    return random.choice(sentences)


@st.cache
def load_data():
    with open('./model_churn/data/company_churn_model.pkl', 'rb') as fm:
        model = joblib.load(fm)
    with open('./model_churn/data/company_churn_variables.json', 'r', encoding='utf8') as ff:
        features = json.load(ff)

    return features, model


def get_predict(row, model, feat_cols):
    df = pd.DataFrame([row], columns=feat_cols)

    df.loc[df['Salary_Change'] == 'Decreased more than 15%', 'Salary_Change_Encoded'] = 0
    df.loc[df['Salary_Change'] == '[-15%, -5%[', 'Salary_Change_Encoded'] = 1
    df.loc[df['Salary_Change'] == '[-5%, 0%[', 'Salary_Change_Encoded'] = 2
    df.loc[df['Salary_Change'] == 'Hasn\'t changed', 'Salary_Change_Encoded'] = 3
    df.loc[df['Salary_Change'] == ']0%, 5%]', 'Salary_Change_Encoded'] = 4
    df.loc[df['Salary_Change'] == ']5%,15%]', 'Salary_Change_Encoded'] = 5
    df.loc[df['Salary_Change'] == 'Increased more than 15%', 'Salary_Change_Encoded'] = 6
    df = df.drop('Salary_Change', axis=1)

    df = df[['Avg_Salary', 'Salary_Change_Encoded', 'Job_Role',
             'Residence_District', 'Employer_Industry']]

    df.loc[:, df.dtypes == 'object'] = df.select_dtypes(['object']).apply(lambda x: x.astype('category'))

    probability = model.predict(df)[0]
    output = 1 if probability >= 0.23 else 0

    lift = round((probability / 0.161), 2)

    return lift, output


def app():
    st.header('Predict Churn')

    st.text("\n")
    st.write("This page allows to predict whether an employee will leave (churn) a company in the next 6 months or not taking into consideration the profile")
    st.markdown("***")

    left_column, center_column, right_column = st.beta_columns((1, 0.25, 0.5))

    features, model = load_data()

    with left_column:
        st.write('Add the employee profile and press the button at the end')
        
        salary = st.number_input("Salary", 0, 200000, 20000, 500)
        salary_change = st.selectbox("Salary Change in last year", (features['Salary_Change']),
                                     format_func=lambda x: 'Salary Change in last year' if x == '' else x)
        job_role = st.selectbox("Job Role", (sorted(features['Job_Role'])),
                                format_func=lambda x: 'Job Role' if x == '' else x)
        residence_district = st.selectbox("Employee Residence District", (sorted(features['Residence_District'])), index = 10,
                                          format_func=lambda x: 'Employee Residence District' if x == '' else x)
        employer_industry = st.selectbox("Employer Industry", (sorted(features['Employer_Industry'])),
                                         format_func=lambda x: 'Employer Industry' if x == '' else x)

        row = [salary, salary_change, job_role, residence_district, employer_industry]

        feat_cols = ['Avg_Salary',
                     'Salary_Change',
                     'Job_Role',
                     'Residence_District',
                     'Employer_Industry']

        st.text("\n")
        if st.button('Predict Churn'):
            lift, output = get_predict(row, model, feat_cols)
            if output:
                st.write(
                    f'According to the employee profile, it is predicted to `leave` your company in the next 6 months. The probability of this happening is `{lift}x higher` than average.')
            else:
                st.write('According to the employee profile, it is predicted to `stay` in your company.')
        
        st.markdown("***")
        
    with right_column:
        image = Image.open('images/question-mark.png')
        image = image.resize((125, 125), Image.ANTIALIAS)
        st.image(image)
        st.write('Did you know that ' + get_random_string())

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
        '`34 years` old was the average `Age` of the workers that answered the 2021 Tech Careers Survey PT?',
        'workers in the `Security` industry reported the largest average value for `Salary Fairness` in the 2021 Tech Careers Survey PT?',
        'workers in the `Nonprofit` industry reported the largest average value for `Training/Development programs at work` as job motivator in the 2021 Tech Careers Survey PT?',
        'workers in the `Real estate` industry reported the largest average value reported for `Computer/Office equipment allowance` as job perk in the 2021 Tech Careers Survey PT?',
        'workers in the `Data and analytics` industry reported the largest average value reported for `Flexible schedule` as job motivator in the 2021 Tech Careers Survey PT?',
        'workers in the `Security` industry reported the largest average value reported for `Stock options or shares` as job perk in the 2021 Tech Careers Survey PT?']
    return random.choice(sentences)


@st.cache
def load_data():
    with open('./data/company_churn.pkl', 'rb') as fm:
        model = joblib.load(fm)
    with open('./data/company_churn_variables.json', 'r', encoding='utf8') as ff:
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
    st.header('Predict churn employee')

    st.text("\n")
    st.write("This page allows companies to predict the probability of an employee, given certain profile, churning the company in the next 6 months.")
    st.markdown("***")

    left_column, center_column, right_column = st.beta_columns((1, 1, 1))

    features, model = load_data()

    with left_column:

        salary = st.number_input("Salary", 0, 200000, 20000, 500)
        salary_change = st.selectbox("Salary Change", (sorted(features['Salary_Change'])),
                                     format_func=lambda x: 'Salary Change' if x == '' else x)
        job_role = st.selectbox("Job Role", (sorted(features['Job_Role'])),
                                format_func=lambda x: 'Job Role' if x == '' else x)
        residence_district = st.selectbox("Residence District", (sorted(features['Residence_District'])),
                                          format_func=lambda x: 'Residence District' if x == '' else x)
        employer_industry = st.selectbox("Employer Industry", (sorted(features['Employer_Industry'])),
                                         format_func=lambda x: 'Employer Industry' if x == '' else x)

        row = [salary, salary_change, job_role, residence_district, employer_industry]

        feat_cols = ['Avg_Salary',
                     'Salary_Change',
                     'Job_Role',
                     'Residence_District',
                     'Employer_Industry']

    with center_column:
        st.write('Add employee profile on the left and press:')
        if st.button('Predict churn'):
            lift, output = get_predict(row, model, feat_cols)
            if output:
                st.write(
                    f'According to the employee profile, it is predicted that he/she `wants to leave` your company in the next 6 months. The probability of this happening is `{lift}x higher` than average.')
            else:
                st.write(
                    f'According to the employee profile, it is predicted that he/she `wants to stay` in your company.')

    with right_column:
        image = Image.open('images/question-mark.jpg')
        image = image.resize((125, 125), Image.ANTIALIAS)
        st.image(image)
        st.write('Did you know that ' + get_random_string())

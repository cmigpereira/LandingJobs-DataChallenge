import streamlit as st
import numpy as np
import pandas as pd
import random
from PIL import Image
import joblib
import json
from sklearn.preprocessing import OrdinalEncoder
import warnings
import xgboost as xgb

warnings.filterwarnings('ignore')


def process_user_input(df, oe):
    categorical_list = ['Job_Role', 'Employer_Industry', 'Employer_Org_Type',
                        'Work_Company_Country']

    df[categorical_list] = oe.transform(df[categorical_list])

    df.loc[df['Working_Experience'] == 'No working experience',
           'Working_Experience'] = 0
    df.loc[df['Working_Experience'] == 'Less than 1 year',
           'Working_Experience'] = 1
    df.loc[df['Working_Experience'] == 'Between 1 - 3 years',
           'Working_Experience'] = 2
    df.loc[df['Working_Experience'] == 'Between 3 - 6 years',
           'Working_Experience'] = 3
    df.loc[df['Working_Experience'] == 'Between 6 - 9 years',
           'Working_Experience'] = 4
    df.loc[df['Working_Experience'] == 'More than 9 years',
           'Working_Experience'] = 5
    df['Working_Experience'] = df['Working_Experience'].astype(int)

    df.loc[df['Employer_Size'] == 'Less than 10 employees',
           'Employer_Size'] = 0
    df.loc[df['Employer_Size'] == '10 - 19 employees',
           'Employer_Size'] = 1
    df.loc[df['Employer_Size'] == '20 - 99 employees',
           'Employer_Size'] = 2
    df.loc[df['Employer_Size'] == '100 - 499 employees',
           'Employer_Size'] = 3
    df.loc[df['Employer_Size'] == '500 - 999 employees',
           'Employer_Size'] = 4
    df.loc[df['Employer_Size'] == '1000 - 4.999 employees',
           'Employer_Size'] = 5
    df.loc[df['Employer_Size'] == 'More than 5.000 employees',
           'Employer_Size'] = 6
    df['Employer_Size'] = df['Employer_Size'].astype(int)

    return df


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


@st.cache(hash_funcs={xgb.Booster: id})
def load_data():
    with open('./data/company_salary_ordinalencoder.joblib', 'rb') as fl:
        oe = joblib.load(fl)
    with open('./data/company_salary_features.json', 'r', encoding='utf8') as ff:
        features = json.load(ff)

    model = xgb.Booster()
    model.load_model('./data/company_salary_model.model')

    return oe, features, model


def get_predict(row, oe, model, feat_cols):
    df = pd.DataFrame([row], columns=feat_cols)
    df = process_user_input(df, oe)
    df = xgb.DMatrix(df.values)

    pred = model.predict(df)

    return round(int(pred[0]), -3)


def app():
    st.header('Salary Costs Prediction as a future Employee')
    
    st.text("\n")
    st.write("This page helps you predict the costs your company will have with an employee.")
    st.markdown("***")

    left_column, center_column, right_column = st.beta_columns((1, 1, 1))

    oe, features, model = load_data()

    with left_column:
        age = st.slider("Age (Years)", 16, 67, 42, 1)
        job_role = st.selectbox("Job Role", (sorted(features['Job_Role'])),
                                format_func=lambda x: 'Job Role' if x == '' else x)
        employer_industry = st.selectbox("Employer Industry", (sorted(features['Employer_Industry'])),
                                         format_func=lambda x: 'Employer Industry' if x == '' else x)
        working_experience = st.selectbox("Working Experience", (sorted(features['Working_Experience'])),
                                          format_func=lambda x: 'Working Experience' if x == '' else x)
        employer_size = st.selectbox("Employer Size", (sorted(features['Employer_Size'])),
                                     format_func=lambda x: 'Employer Size' if x == '' else x)
        employer_org_type = st.selectbox("Employer Org Type", (sorted(features['Employer_Org_Type'])),
                                         format_func=lambda x: 'Employer Org Type' if x == '' else x)
        work_company_country = st.selectbox("Work Company Country", (sorted(features['Work_Company_Country'])),
                                            format_func=lambda x: 'Work Company Country' if x == '' else x)

        row = [age, job_role, employer_industry, working_experience,
               employer_size, employer_org_type, work_company_country]

        feat_cols = ['Age',
                     'Job_Role',
                     'Employer_Industry',
                     'Working_Experience',
                     'Employer_Size',
                     'Employer_Org_Type',
                     'Work_Company_Country']

    with center_column:
        st.write('Add the employee and company profiles on the left and press:')
        if st.button('Predict Salary Costs'):
            result = get_predict(row, oe, model, feat_cols)
            st.write(f'According to the inserted profiles, the salary should be around: `{result}`€')

    with right_column:
        image = Image.open('images/question-mark.png')
        image = image.resize((125, 125), Image.ANTIALIAS)
        st.image(image)
        st.write('Did you know that ' + get_random_string())

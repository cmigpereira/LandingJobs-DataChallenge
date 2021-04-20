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
                        'Work_Company_Country', 'Work_Company_PT_District']

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

    with open('./data/employee_salary_ordinalencoder.joblib', 'rb') as fl:
        oe = joblib.load(fl)
    with open('./data/employee_salary_features.json', 'r', encoding='utf8') as ff:
        features = json.load(ff)

    model = xgb.Booster()
    model.load_model('./data/employee_salary_model.model')

    return oe, features, model


def get_predict(row, oe, model, feat_cols):
    df = pd.DataFrame([row], columns=feat_cols)
    df = process_user_input(df, oe)
    df = xgb.DMatrix(df.values)

    pred = model.predict(df)

    return round(int(pred[0]), -3)


def app():
    st.header('Salary Prediction as an Employee')
    
    st.text("\n")
    st.write("This page suggests a salary according to the inserted profile.")
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
        employer_org_type = st.selectbox("Employer Org Type", (sorted(features['Employer_Org_Type'])),
                                         format_func=lambda x: 'Employer Org Type' if x == '' else x)
        work_company_country = st.selectbox("Work Company Country", (sorted(features['Work_Company_Country'])),
                                            format_func=lambda x: 'Work Company Country' if x == '' else x)
        work_company_pt_district = st.selectbox("Work Company District", (sorted(features['Work_Company_PT_District'])),
                                                format_func=lambda x: 'Work Company District' if x == '' else x)

        row = [age, job_role, employer_industry, working_experience,
               employer_org_type, work_company_country, work_company_pt_district]

        feat_cols = ['Age',
                     'Job_Role',
                     'Employer_Industry',
                     'Working_Experience',
                     'Employer_Org_Type',
                     'Work_Company_Country',
                     'Work_Company_PT_District']

    with center_column:
        st.write('Add your profile and preferences on the left and press:')
        if st.button('Find Predicted Salary'):
            result = get_predict(row, oe, model, feat_cols)
            st.write(f'According to the inserted profile, the salary should be around: `{result}€`')

    with right_column:
        image = Image.open('images/question-mark.jpg')
        image = image.resize((125, 125), Image.ANTIALIAS)
        st.image(image)
        st.write('Did you know that ' + get_random_string())

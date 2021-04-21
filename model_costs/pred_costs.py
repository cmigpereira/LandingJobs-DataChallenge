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
        '`Mobile Apps Developer` role has, on average, a `higher salary` than other developer roles? Contrarily, `Computer & Network Security` roles earn the less.',
        '`Contractors` earn, on average, `55% more` than Permanent Employees?', 
        'people in `Lisbon`, on average, earn `2x more` than their counterparts in `Vila Real`? Interestingly enough, people in `Beja` earn almost the same as people in `Lisbon`.', 
        'people who get into the tech industry through `Code Bootcamps` earn, on average, `30% less` than those who have a degree?',
        '`Scale-ups` offer the best salaries? About 50% more than other types of organizations!', 
        'people being paid `under 30k` gross a year always think they are paid `unfairly`?', 
        'people who do not care about work-life balance have, on average, a 50% higher salary?']
    return random.choice(sentences)


@st.cache(hash_funcs={xgb.Booster: id})
def load_data():
    with open('./model_costs/data/company_salary_ordinalencoder.joblib', 'rb') as fl:
        oe = joblib.load(fl)
    with open('./model_costs/data/company_salary_features.json', 'r', encoding='utf8') as ff:
        features = json.load(ff)

    model = xgb.Booster()
    model.load_model('./model_costs/data/company_salary_model.model')

    return oe, features, model


def get_predict(row, oe, model, feat_cols, age_increase, experience_increase):
    df = pd.DataFrame([row], columns=feat_cols)
    df = process_user_input(df, oe)
    df["Age"] = df["Age"] + age_increase
    df["Working_Experience"] = df["Working_Experience"] + experience_increase
    df = xgb.DMatrix(df.values)

    pred = model.predict(df)

    return pred[0]


def get_predict_years(row, oe, model, feat_cols, years_long):
    # doesnt change working_experience
    if ((years_long == 1) | (years_long == 2)):
        original_row = row.copy()
        years_added = 0
        result = 0
        while (years_added < years_long):
            result += get_predict(row, oe, model, feat_cols, years_added, 0) * 1.23
            row = original_row.copy()
            years_added = years_added + 1
    # changes working experience
    else:
        # first two years
        original_row = row.copy()
        years_added = 0
        result = 0
        while (years_added < 2):
            result += get_predict(row, oe, model, feat_cols, years_added, 0) * 1.23
            row = original_row.copy()
            years_added = years_added + 1
        # the rest of the years
        while (years_added < years_long):
            result += get_predict(row, oe, model, feat_cols, years_added, 1) * 1.23
            row = original_row.copy()
            years_added = years_added + 1

    return int(round(result, -2))

def app():
    st.header('Predict Costs')
    
    st.text("\n")
    st.write("This page helps to predict the costs a company will have with a future employee over the years taking into consideration the profile")
    st.markdown("***")

    left_column, center_column, right_column = st.beta_columns((1, 0.25, 0.5))

    oe, features, model = load_data()

    with left_column:
        st.write('Add the employee profile along with the years of salary to predict and press the button at the end')
        
        age = st.slider("Age (Years)", 16, 67, 42, 1)
        job_role = st.selectbox("Job Role", (sorted(features['Job_Role'])),
                                format_func=lambda x: 'Job Role' if x == '' else x)
        employer_industry = st.selectbox("Employer Industry", (sorted(features['Employer_Industry'])),
                                         format_func=lambda x: 'Employer Industry' if x == '' else x)
        working_experience = st.selectbox("Employee Working Experience", (features['Working_Experience']),
                                          format_func=lambda x: 'Employee Working Experience' if x == '' else x)
        employer_size = st.selectbox("Employer Size", (features['Employer_Size']),
                                     format_func=lambda x: 'Employer Size' if x == '' else x)
        employer_org_type = st.selectbox("Employer Org Type", (sorted(features['Employer_Org_Type'])),
                                         format_func=lambda x: 'Employer Org Type' if x == '' else x)
        work_company_country = st.selectbox("Employer Original Country", (sorted(features['Work_Company_Country'])), index = 27,
                                            format_func=lambda x: 'Employer Original Country' if x == '' else x)
        years_long = st.slider("Years of Costs Calculation", 1, 5, 3, 1)
        
        row = [age, job_role, employer_industry, working_experience,
               employer_size, employer_org_type, work_company_country]

        feat_cols = ['Age',
                     'Job_Role',
                     'Employer_Industry',
                     'Working_Experience',
                     'Employer_Size',
                     'Employer_Org_Type',
                     'Work_Company_Country']

        st.text("\n")
        if st.button('Predict Costs'):
            result = get_predict_years(row, oe, model, feat_cols, years_long)
            st.write(f'According to the inserted profiles, the salary should be around: `{result}`€')

        st.markdown("***")
        
    with right_column:
        image = Image.open('images/question-mark.png')
        image = image.resize((125, 125), Image.ANTIALIAS)
        st.image(image)
        st.write('Did you know that ' + get_random_string())

import streamlit as st
from multiapp import MultiApp
from apps import home, churn, recommend_salary, pred_salary, industry

app = MultiApp()

st.set_page_config(page_title="People Analytics @ Team Vectorize", layout='wide')

#Apps
app.add_app("Home", home.app)
app.add_app("Churn Employee", churn.app)
app.add_app("Recommend Salary", recommend_salary.app)
app.add_app("Predict Salary", pred_salary.app)
app.add_app("Recommend Industry", industry.app)
# Main app
app.run()

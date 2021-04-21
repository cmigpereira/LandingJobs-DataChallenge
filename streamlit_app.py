import streamlit as st
from multiapp import MultiApp
import home
from model_churn import pred_churn
from model_costs import pred_costs
from model_salary import pred_salary
from model_industry import recommend_industry
import about

app = MultiApp()

st.set_page_config(page_title="People Analytics @ Team Vectorize", layout='wide')

#Apps
app.add_app("Home", home.app)
app.add_app("Predict Churn", pred_churn.app)
app.add_app("Predict Costs", pred_costs.app)
app.add_app("Predict Salary", pred_salary.app)
app.add_app("Recommend Industry", recommend_industry.app)
app.add_app("About the models", about.app)
# Main app
app.run()

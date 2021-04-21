import streamlit as st


def app():

    st.header('About the models')
    st.markdown("***")
    
    st.subheader('Predict Churn model')

    st.markdown("""
    #### Goal
    Employee churn is when employees leave the company where they are. Although inevitable, when very high, churn is very costly for the company because recruiting, hiring, and training a new employee requires some financial effort and some loss of productivity. 
    Moreover, an unusually high churn rate indicates problems within the company, such as lousy policy practices or even uncompetitive salaries.
    
    #### Problem
    Until now, companies have been forecasting how many employees might leave by calculating the churn rate each time. 
    Consequently, companies know, in average, how many people might leave the company, but they don't know who will leave. 
    If they can anticipate who will leave, they might avoid it or, at least, be prepared for it.
    
    In this model, we devised a Machine Learning approach based on a LightGBM algorithm.
    We predict an employee leaving the company in the next six months using the variables considered most relevant for the prediction:
    - Salary: What's the employee gross annual income in euros? Keep in mind that this may include commission, bonuses, etc.
    - Salary Change in last year: How much did the employee income change in the last 12 months? Remember how important wage increases are in the world of employment...
    - Job Role: Depending on the job role, the salaries increase or decrease. Usually related to demand and the industry where this role is needed more! :)
    - Employee Residence District: The district of residence is often the district of work. Therefore, it is mainly related to the cost of living in certain districts, but, with competition between companies, salaries vary.
    - Employer Industry: Whether you like it or not, although having the same job role, different industries pay different salaries.

    #### Performance
    A broader set of variables would slightly improve the performance of the model. 
    However, it would bring some complexity to you. 
    Therefore, we chose the most important variables for the calculation, which allowed us to leverage a ROC AUC metric of 0.7.
    
    #### Interesting Observations
    We noticed that negative wage changes lead to people's dissatisfaction and a propensity to churn. 
    It is also curious that this has even more importance than the value of the salary itself.""")
    st.markdown("***")

    st.subheader('Predict Costs model')
    st.markdown("""
    #### Goal
    The goal of this model is to predict the costs a company will have with the given candidate profile, over a selected period of years. 
    It calculates the costs with salary increases and taxes.
    
    #### Problem
    The salary increase calculation is based on the value of the employee after each year in the company: as employees get more experienced, they earn more money, which is an important factor for the calculation of the total costs! 
    In this type of problem, the standard approach is to find similar profiles to the given one and calculate the average salary costs for those profiles.
    However, we cannot just sit here without having a bit of fun, so we implemented a salary costs prediction model, based on a XGBoost algorithm, using the following variables:
    - Age: Not only related with working experience but also to the natural desire of stability and the recognition of knowledge.
    - Job Role: Depending on the job role, the salaries increase or decrease. Usually related with demand and the industry where this role is needed more! :)
    - Employer Industry: Whether you like it or not, although having the same job role, different industries pay different salaries.
    - Employee Working Experience: Ok, pretty obvious... :)
    - Employer Size: Size of organizations affect their structures, resulting in varying salaries.
    - Employer Org Type: SMEs, Startups, Scale-ups, ... Different types of organizations have different needs and flexibility, resulting in salary variations.
    - Employer Original Country: Depending on the country of the company you work for (in case of working remotely), or where you work in, the salaries vary to meet the traditional office salaries of that same country.
    
    #### Performance
    We could increase the number of variables and increase the performance of this model, but we chose to keep it simple for you. 
    The impact of having this low number of variables isn't that big, and we ended up with a MAE (mean absolute error) metric of 9500. 
    This essentially means that the predicted salary, when we evaluated the model, was wrong (in terms of what you really payed to the employee, according to the market) in about 9500€. 

    #### Interesting Observations
    We noticed that lower experience workers usually get salary costs predictions below the expected. 
    This is probably related with the fact that, with time and experience, the salary increase is not linear.""")
    
    st.markdown("***")

    st.subheader('Predict Salary model')
    st.markdown("""
    #### Goal
    The goal of this model is to predict the salary of an employee with the given profile.
    
    #### Problem
    In this type of problem, the standard approach is to find similar profiles to the given one and calculate the average salary of those profiles.
    
    However, we cannot just sit here without having a bit of fun, so we implemented a salary prediction model, based on a XGBoost algorithm, using the following variables:
    - Age: Not only related with working experience but also to the natural desire of stability and the recognition of knowledge.
    - Job Role: Depending on the job role, the salaries increase or decrease. Usually related with demand and the industry where this role is needed more! :)
    - Employer Industry: Whether you like it or not, although having the same job role, different industries pay different salaries.
    - Employee Working Experience: Ok, pretty obvious... :)
    - Employer Org Type: SMEs, Startups, Scale-ups, ... Different types of organizations have different needs and flexibility, resulting in varying salaries.
    - Employer Original Country: Depending on the country of the company you work for (in case of working remotely), or where you work in, the salaries vary to meet the traditional office salaries of that same country.
    - Employer Portugal District: Mainly related with the cost-of-living in certain districts, but, with competition between companies, salaries vary.
    
    #### Performance
    We could increase the number of variables and increase the performance of this model, but we chose to keep it simple for you. 
    The impact of having this low number of variables isn't that big, and we ended up with a MAE (mean absolute error) of 9500. 
    This essentially means that the predicted salary, when we evaluated the model, was wrong (in terms of what you really deserve, according to the market) in about 9500€.
   
    #### Interesting Observations
    We noticed that lower experience workers usually get salary predictions below the deserved. 
    This is probably related with the fact that, with time and experience, the salary increase is not linear. 
    Cool! (but we would love it to be linear, don't we?)""")

    st.markdown("***")

    st.subheader('Recommend Industry model')
    st.markdown("""
    #### Goal
    The goal of this model is to predict the best industry for a person to work taking into consideration its own preferences. 
    
    #### Problem
    Many times, when a person search for the first or a new opportunity, they do not know what lies ahead. 
    When accepting the offer, initial expectations might not be met (e.g., worklife balance can become cumbersome).  
    In this type of situations, the standard approach is to ask colleagues or familiars; however, they their help is also limited from their own experience. 
    If it becomes possible to predict and recommend the best industry to work in, then disappointments, frustrations and, ultimately, employee churn could be reduced.
    For this, we devised a Machine Learning approach based on a LightGBM algorithm. 
    The model recommends the best industry to work in using the variables considered most relevant for the recommendation:
    - Residence District: People usually prefer to stay close to home, a huge point to consider when changing companies.
    - Age: Not only related with working experience but also to the natural desire of stability and the recognition of knowledge.
    - Salary Fairness: Different industries have better profitability rates, which increases the employees salaries, making employees feel that they're fairly payed.
    - Training/Development programs at work: Younger folks like to have training and development programs at work, which some industries are more prone to give. Cool!
    - Computer/Office equipment allowance: For some industries it doesn't make any sense to offer office equipment, while others feel the contrary. Employees take this in consideration when choosing a new job!
    - Flexible_schedule: Flexibility is key to some people. Being able to work anywhere or whenever an employee wants can make the difference when choosing a new industry to work.
    - Stock options or shares: Some industries are much more dynamic than others like startups that are willing to give employees options or shares.
    
    #### Performance
    A broader set of variables would slightly improve the performance of the model. 
    However, it would bring some complexity to you. 
    Therefore, we chose the most important variables for the calculation, which allowed us to leverage a micro-average multiclass AUROC metric of 0.6.

    #### Interesting 
    We noticed that Residence District is the most important indicator to recommend the industry to work in. Will this change if companies become more remote-working friendly?
    """)
    st.markdown("***")

# Predict Salary model
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
Cool! (but we would love it to be linear, don't we?)
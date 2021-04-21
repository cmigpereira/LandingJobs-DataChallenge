# Predict Churn model
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
It is also curious that this has even more importance than the value of the salary itself.
# Recommend Industry model
#### Goal
The goal of this model is to predict the best industry for a person to work taking into consideration its own preferences. 

#### Problem
Many times, when a person searches for the first or a new opportunity, one does not know what lies ahead. 
When accepting the offer, initial expectations might not be met (e.g., worklife balance can become cumbersome).  
In this type of situations, the standard approach is to ask colleagues or familiars; however, their help is also limited from their own experience. 
If it becomes possible to predict and recommend the best industry to work in, then disappointments, frustrations and, ultimately, employee churn could be reduced.
For this, we devised a Machine Learning approach based on a LightGBM algorithm. 
The model recommends the best industry to work in using the variables considered most relevant for the recommendation:
- Residence District: People usually prefer to stay close to home, a huge point to consider when changing companies.
- Age: Not only related with working experience but also to the natural desire for stability and the recognition of knowledge.
- Salary Fairness: Different industries have better profitability rates, which increases the employees' salaries, making employees feel that they're fairly payed.
- Training/Development programs at work: Younger folks like to have training and development programs at work, which some industries are more prone to give. Cool!
- Computer/Office equipment allowance: For some industries it does not make any sense to offer office equipment, while others feel the contrary. Employees take this in consideration when choosing a new job!
- Flexible_schedule: Flexibility is key to some people. Being able to work anywhere or whenever an employee wants can make the difference when choosing a new industry to work.
- Stock options or shares: Some industries are much more dynamic than others like startups that are willing to give employees options or shares.

#### Performance
A broader set of variables would slightly improve the performance of the model. 
However, it would bring some complexity to you. 
Therefore, we chose the most important variables for the calculation, which allowed us to leverage a micro-average multiclass AUROC metric of 0.6.

#### Interesting 
We noticed that Residence District is the most important indicator to recommend the industry to work in. 
Will this change if companies become more remote-working friendly?
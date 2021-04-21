# Jobs Wizard

[Jobs Wizard](https://www.jobswizard.tech/) aims to help both companies and employees to make better, data-driven decisions with respect to people management.

Leveraging data from the Tech Careers Report Portugal 2021, provided by Landing.Jobs, we devised 4 Machine Learning models (yes, that's right, 4 models!) to tackle 4 main challenges in the People Analytics area.

And, above all, we implemented them with a user interface to allow you to play with them.

## Predictive Models

* Predict Churn: predict whether an employee is about to leave (churn) the company or not;
* Predict Costs: predict the costs a company will have with a future employee over the years;
* Predict Salary: predict the salary a given employee should be earning today;
* Recommend Industry: recommend the best industry to work in.

You can learn more about each model in the respective *Readme.md* inside each model's folder.

## Run locally the app

In order to run locally the app, you just need to install the required packages listed in *requirements.txt* and run:
```
streamlit run streamlit_app.py
```

## Have fun but be socially responsible!

Please remember that any Machine Learning model can fail, and their performance is tightly related to the data, both in data quality and data size used for training the models.

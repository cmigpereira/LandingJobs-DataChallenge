import streamlit as st


def app():
    st.header('Shedding light on the Portugal tech market with People Analytics')
   # st.markdown("<h1 style='text-align: center; color: red;'>Shedding light on the Portugal tech market with People Analytics</h1>", unsafe_allow_html=True)

    st.markdown("***")
    


    st.write('This app aims helping both companies and employees to make better, data-driven decisions with respect to people management.')
    st.write('Leveraging data from the Tech Careers Report Portugal 2021, provided by Landing.Jobs, we devised 4 Machine Learning models (yes, that\'s right, 4 models!) to tackle 4 main challenges in the People Analytics area.')
    st.write('And, above all, we implemented them with a user interface to allow you to play with them.')
    st.write('They are:')
    st.markdown(
        """    
        - *Predict Churn*: predict whether an employee is about to leave (churn) the company or not;
        - *Predict Costs*: predict the costs a company will have with a future employee over the years;
        - *Predict Salary*: predict the salary a given employee should be earning today;
        - *Recommend Industry*: recommend employees the best industry to work in.
        """)
    st.write('Use the navigation sidebar in the left to browse through the models. Have fun but be socially responsible!')
    st.write('')
    st.markdown('You can learn more about the models in the *About the models* page.')
    st.write('Please remember that any Machine Learning model can fail and their quality is tightly related with the data, both in quality and size.')

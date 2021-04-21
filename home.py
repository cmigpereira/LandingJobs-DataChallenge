import streamlit as st


def app():
    
    #Title rendering
    Title_html = """
    <style>
        .title h1{
          user-select: none;
          text-align: center;
          font-size: 36px;
          background: black;
          -webkit-background-clip: text;
        }
    </style> 
    
    <div class="title">
        <h1>Shedding light on Portugal Tech market with People Analytics</h1>
    </div>
    """
    st.markdown(Title_html, unsafe_allow_html=True)
    st.markdown("***")
    
    st.markdown('*Jobs Wizard* aims helping both companies and employees to make better, data-driven decisions with respect to people management.')
    st.write('Leveraging data from the Tech Careers Report Portugal 2021, provided by Landing.Jobs, we devised 4 Machine Learning models (yes, that\'s right, 4 models!) to tackle 4 main challenges in the People Analytics area.')
    st.write('And, above all, we implemented them with a user interface to allow you to play with them.')
    st.write('They models are:')
    st.markdown(
        """    
        - *Predict Churn*: predict whether an employee is about to leave (churn) the company or not;
        - *Predict Costs*: predict the costs a company will have with a future employee over the years;
        - *Predict Salary*: predict the salary a given employee should be earning today;
        - *Recommend Industry*: recommend employees the best industry to work in.
        """)
    st.markdown('__Use the navigation sidebar in the top left__ to browse through the models. Have fun but be socially responsible!')
    st.write('')
    st.markdown('You can learn more about the models in the *About the models* page.')
    st.write('Please remember that any Machine Learning model can fail and their quality is tightly related with the data, both in quality and size.')

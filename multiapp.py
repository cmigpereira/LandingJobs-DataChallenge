import streamlit as st
from PIL import Image 

class MultiApp:
    """Framework for combining multiple streamlit applications.
    """

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        """Adds a new application.
        Parameters
        ----------
        func:
            the python function to render this app.
        title:
            title of the app. Appears in the dropdown in the sidebar.
        """
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        
        image = Image.open('images/jobswizard.png')
        image = image.resize((125, 30), Image.ANTIALIAS)
        st.image(image)
        st.sidebar.write("")

        app = st.sidebar.selectbox(
            'Navigation',
            self.apps,
            format_func=lambda app: app['title'])

        st.sidebar.write("")
        st.sidebar.write("")
        st.sidebar.write("We leverage People Analytics to improve people-decisions.")
        st.sidebar.write("Jobs Wizard is brought to you by:")
        st.sidebar.write(
            "[Carlos Pereira] (https://linkedin.com/in/carlos-miguel-pereira/), [Sérgio Jorge](https://linkedin.com/in/sergiotj/) and [Vitor Castro](https://linkedin.com/in/vitorcastroit/).")
        st.sidebar.write(
            "The data is from the Tech Careers Report 2021, provided by [Landing.Jobs](https://taikai.network/en/landingjobs/challenges/datachallenge).")
        st.sidebar.write(
            "Visit our [Github](https://github.com/cmigpereira/LandingJobs-DataChallenge).")
        app['function']()


 
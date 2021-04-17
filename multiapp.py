import streamlit as st

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
        app = st.sidebar.selectbox(
            'Navigation',
            self.apps,
            format_func=lambda app: app['title'])

        st.sidebar.write("")
        st.sidebar.write("")
        st.sidebar.write("This app is brought to you by:")
        st.sidebar.write("[Carlos Pereira] (https://linkedin.com/in/carlos-miguel-pereira/), [Sérgio Jorge](https://linkedin.com/in/sergiotj) and [Vitor Castro](https://linkedin.com/in/vitorcastroit).")
        st.sidebar.write("We leverage People Analytics to make people-decisions.")
        st.sidebar.write("The data is from the Tech Careers Report 2021, provided by [Landing.Jobs](https://taikai.network/en/landingjobs/challenges/datachallenge).")
        app['function']()

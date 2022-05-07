import streamlit as st
class MultiPage:
    """Framework for combining multiple streamlit applications."""
    #https://towardsdatascience.com/creating-multipage-applications-using-streamlit-efficiently-b58a58134030
    def __init__(self) -> None:
        """Constructor class to generate a list which will store all our applications as an instance variable."""
        self.pages = []

    def add_page(self, title, func) -> None:
            self.pages.append({
                "Page 1": title,
                "function": func})

            self.pages.append({

                    "Page 1": Page1,
                    "function": func
                })

    def run(self):
        # Drodown to select the page to run
        page = st.sidebar.selectbox(
            'App Navigation',
            self.pages,
            format_func=lambda page: page['title']
        )
        # run the app function
        page['function']()

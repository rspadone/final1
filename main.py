"""
Name: Ruby Spadone
CS230: CS230.1
Data: Which data set you used URL: Link to your web application online

Description: This program ... (a few sentences about your program and the queries and charts) """

import app as app
import pandas as pd
import matplotlib.pyplot as plt
import sys

import pipreqs as pipreqs
import streamlit as st


# Getting the data
def get_data():
    homes = pd.read_csv('Cambridge_Property_Database_FY2022_8000_sample.csv')
    print(homes)


# Creating multiple pagies
# Define the multipage class to manage the multiple apps in our program
# Adding names
import streamlit as st
import Home_page
import Page_1
import Page_2
import Page_3
import Page_4
import Page_5

PAGES = {
    "Home Page": Home_page,
    "Bedrooms v. Price of Property": Page_1,
    "Months Sold v. Type of Home": Page_2,
    "Condition v. Year built": Page_3,
    "Map of Cambridge": Page_4,
    "Top 5 most frequent values for all columns": Page_5
}
st.sidebar.title('Navigation')
selection = st.sidebar.selectbox("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()


def main():
    data_frame = get_data()


main()



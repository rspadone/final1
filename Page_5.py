import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import pandas as pd

def app():
    st.title('Top 5 most frequent values for all columns!')
    st.write("This shows the top 5 most frequent values in each column as well as how many times they show up")
    homes = pd.read_csv('Cambridge_Property_Database_FY2022_8000_sample.csv')
    #https://datascientyst.com/get-most-frequent-values-pandas-dataframe/#:~:text=To%20get%20the%20most%20frequent,It%20can%20be%20multiple%20values.
    from pandas.api.types import is_categorical_dtype
    for col in homes.columns:
        print(col, end=' - \n')
        print('_' * 50)
        if col in ['Magnitude'] or is_categorical_dtype(col):
            st.write(pd.DataFrame(homes[col].astype('str').value_counts().sort_values(ascending=False).head(3)))
        else:
            st.write(pd.DataFrame(homes[col].value_counts().sort_values(ascending=False).head(5)))

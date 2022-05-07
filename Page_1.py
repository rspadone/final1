import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import pandas as pd

def app():
    st.title('Bedrooms v. Price of Property')
    homes = pd.read_csv('Cambridge_Property_Database_FY2022_8000_sample.csv')
    homes= homes[homes["AssessedValue"] > 1 ] #gets rid of unknown sales prices
    selected_bedroom = st.slider("Pick how many bedrooms", 0, 20)
    if selected_bedroom not in homes["Interior_Bedrooms"].unique():
        st.write("Sorry, there are no homes with this number of bedrooms")
    else:
        homes = homes[homes["Interior_Bedrooms"] == selected_bedroom]
        col1, col2 = col1, col2 = st.columns(2)
        maxsale = int(homes["AssessedValue"].max())
        fig, ax = plt.subplots()
        ranges = range(0, maxsale)
        bins = 200
        ax.hist(homes["AssessedValue"], bins =bins, range= [0, 28200200] , color = "blue", histtype = 'bar', rwidth = 0.8)
        col1.write(homes["AssessedValue"])
        col2.write(homes["Interior_Bedrooms"])
        ax.set_xlabel('Sale Price')
        ax.set_ylabel('No. Homes Sold')
        ax.set_title('Sales Price v. No. Homes Sold')
        st.pyplot(fig)

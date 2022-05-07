import altair
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import altair as alt
import seaborn as sns

def app():
    st.title('Months Sold v. Type of Home')
    homes = pd.read_csv('Cambridge_Property_Database_FY2022_8000_sample.csv')
    month = st.selectbox(
        'What month would you like to look at?',
        ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'))
    l = []
    for i in homes["SaleDate"].index:
        l.append(str(homes.loc[i,"SaleDate"]).split("/")[0])
    homes["month of sale"] = l
    homes_months = homes[homes["month of sale"] == month]
    val_count  = homes_months["Exterior_Style"].value_counts()
    col1, col2 = st.columns(2)
    sns.barplot(val_count.index, val_count.values, alpha=0.8)
    plt.title('Types of homes sold in Month')
    plt.ylabel('No. Homes', fontsize=12)
    plt.xlabel('Type of Home', fontsize= 12,)
    plt.xticks(rotation= "vertical", fontsize= 6)
    st.pyplot(plt)
    col1.write(homes_months["Exterior_Style"])
    col2.write(homes_months["SaleDate"])

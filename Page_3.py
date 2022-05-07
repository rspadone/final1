import matplotlib
import streamlit
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from altair.examples.pyramid import df
from datetime import datetime

from jedi.api.refactoring import inline
#%matplotlib inline
plt.style.use('seaborn-whitegrid')
import numpy as np

def app():
    st.title('Condition v. Year built')
    homes = pd.read_csv('Cambridge_Property_Database_FY2022_8000_sample.csv')
    homes = homes.sort_values(by=["Condition_OverallCondition"])
    homes= homes[homes["Condition_YearBuilt"] > 1 ] #gets rid of unknown sales prices
    types_of_condition= homes["Condition_OverallCondition"].unique()
    product = homes['Condition_OverallCondition'].values.tolist()
    condition= []
    condition.append(product)
    condition.sort(reverse = True)#sorts unique conditions
    selected_condition = st.multiselect(
     'What conditions would you like to view',
     [types_of_condition[i] for i in range(len(types_of_condition))],
     [])
    homes= homes[homes["Condition_OverallCondition"].isin(selected_condition)]
    col1, col2 = st.columns(2)
    col1.write(homes["Condition_OverallCondition"])
    number_year = homes["Condition_YearBuilt"].value_counts()
    y = number_year
    x = y.index
    col2.write(y)
    plt.bar(x, y)
    fig, chart= plt.subplots()
    chart.bar(x,y)
    chart.xaxis.set_label_text("Year Built")
    chart.yaxis.set_label_text("No. Homes Sold")
    chart.set_facecolor("crimson")
    fig.suptitle("Year homes was built v. Condition of home")
    st.pyplot(fig)



def main():
    return app()


import streamlit as st
import pandas as pd

def app():
    st.title('Home Page')
   #for n in name:
    #    name = st.text_input("What is your name?")
     #   st.write("Welcome", name, "!")
    st.write("This is a site for people interested in Cambridge Property's")
    st.write("It will provide you with information on buying the best house for you")

    from PIL import Image
    image = Image.open('Cam Image.jpg')
    st.image(image, caption='')

#Show a table of the data being used
    df = pd.read_csv("Cambridge_Property_Database_FY2022_8000_sample.csv")  # read a CSV file inside the 'data" folder next to 'app.py'
    st.title("The data we are using")  # add a title
    st.write(df)  # visualize my dataframe in the Streamlit app

    df =df[df.eval("PropertyTaxAmount>=6000 & (LandValue <1000) & Owner_Name.str.startswith('S').values")]
    st.title("Filtered data set: "
             "Property tax greater than 6000, "
             "land values greater than 100 "
             "and owners that start with S")
    st.write(df)


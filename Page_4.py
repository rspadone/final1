import streamlit as st
from streamlit_folium import folium_static
import pandas as pd
import numpy as np
import folium
import pydeck as pdk
import os

homes = pd.read_csv('Cambridge_Property_Database_FY2022_8000_sample.csv')
# homes= homes[homes["Latitude"] > 0 ]
# homes= homes[homes["Longitude"] > 0]
# st.write(homes)

def app():
    st.title('Map of Cambridge')
    st.write("This is a map of all the properties in Cambridge")
    homes = pd.read_csv( os.path.join( 'Cambridge_Property_Database_FY2022_8000_sample.csv'),
                  usecols = ['Latitude', 'Longitude'])
    new_homes = homes.copy()
    new_homes.Latitude.replace(["<NA>"], "0", inplace=True)#replaces properties without coordinates with a 0
    homes= new_homes[new_homes["Latitude"] > 1 ]#filters out 0
    st.write(homes)
    homes.rename(columns={'Latitude': 'lat', 'Longitude': 'lon'}, inplace=True)#changes name of latitude and longitude
    #https://docs.streamlit.io/library/api-reference/charts/st.pydeck_chart
    st.pydeck_chart(pdk.Deck(
     map_style='mapbox://styles/mapbox/light-v9',
     initial_view_state=pdk.ViewState(
         latitude=homes["lat"].mean(),
         longitude=homes["lon"].mean(),
         zoom=11,
         pitch=50,
     ),
     layers=[
         pdk.Layer(
            'HexagonLayer',
            data=homes,
            get_position='[lon, lat]',
            radius=200,
            elevation_scale=4,
            elevation_range=[0, 1000],
            pickable=True,
            extruded=True,
         ),
         pdk.Layer(
             'ScatterplotLayer',
             data=homes,
             get_position='[lon, lat]',
             get_color='[200, 30, 0, 160]',
             get_radius=200,
         ),
     ],
 ))

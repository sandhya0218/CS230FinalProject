"""
Name: Sandhya Sangappa
CS230: Section 4 FA21
Data: Skyscrapers2021.csv
URL: Link to your web application online

Description: This program creates five visualizations out of the skyscraper data with Streamlit UI widgets.
            The visualizations include a bar chart that displays number of buildings constructed by over time based on
            building material. The skyscraper map displays the coordinates of skyscrapers constructed over time via a slider.
            A line chart displays number of skyscrapers built based on hemisphere, and a seaborn relational plot displays
            a relationship between completion year and number of floors with the plots colored (hue) by material.
"""
import streamlit as st
import pandas as pd
from PIL import Image

import Material_BarChart as mbc
import Skyscraper_Map as sm
import Function_PieChart as fpc
import Hemisphere_LineChart as hlc
import Seaborn_Chart as sc

# Read in data
def read_data():
    df = pd.read_csv("Skyscrapers2021.csv").set_index("RANK")
    return df

def main():
    # Create header for streamlit page
    img = Image.open("BurjKhalifa.jpg")

    st.title("Data Visualization with Python")
    st.write("Welcome to Global 2021 Skyscraper Data!")
    st.header("2021 Global Skyscrapers")
    st.image(img, width = 300)
    st.sidebar.write("Please choose your options to display data.")

    df = read_data()

    SKYSCRAPER_VISUALIZATIONS = {
        "Material Bar Chart": mbc,
        "Skyscraper Map": sm,
        "Function Pie Chart": fpc,
        "Hemisphere Line Chart": hlc,
        "Seaborn Relational Plot": sc
    }

    st.sidebar.title('Skyscraper Visualizations')
    selection = st.sidebar.radio("Go to", list(SKYSCRAPER_VISUALIZATIONS.keys()))
    visualization = SKYSCRAPER_VISUALIZATIONS[selection]
    visualization.display(df)

main()

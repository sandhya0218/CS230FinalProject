import streamlit as st
import pydeck as pdk

# Create list of unqiue years of skyscraper completion
def get_unique_years(df):
    unique_years = []
    year_list = df['COMPLETION'].tolist()
    for year in year_list: # TODO: make this a list comprehension
        if year not in unique_years:
            unique_years.append(int(year))

    unique_years.sort()

    # print(unique_years)

    return unique_years

# Create Skyscrapers Over Time map
def generate_map(df, year):
    map_df = df.filter(['NAME', 'Latitude', 'Longitude', 'COMPLETION'])
    map_df = map_df[map_df.COMPLETION <= year]
    # print(map_df)
    # view_state = pdk.ViewState(latitude=map_df['Latitude'].mean(),
    #                            longitude=map_df['Longitude'].mean(),
    #                            zoom = 8)
    layer = pdk.Layer("ScatterplotLayer",data = map_df,
                      get_position = '[Longitude, Latitude]',
                      get_radius = 400000,
                      get_color = [20, 175, 250],
                      pickable = True)
    tool_tip = {'html': 'Listing:<br/><b>{NAME}</b>', 'style': {'backgroundColor': 'steelblue', 'color': 'white'}}
    skyscraper_map = pdk.Deck(map_style='mapbox://styles/mapbox/light-v9',
                   layers=[layer],
                   tooltip=tool_tip)

    st.pydeck_chart(skyscraper_map)

def display(df):
    # Create header for Skyscrapers By Location Over Time
    unique_years = get_unique_years(df)
    st.header("Skyscrapers Over Time")
    year = st.slider('Show skyscrapers constructed up to:', min(unique_years), max(unique_years))
    st.write(year)

    generate_map(df, year)

import streamlit as st
import matplotlib.pyplot as plt

def construct_hemisphere_data(df):
    east_and_west_dict = {}
    map_df = df.filter(['Longitude', 'COMPLETION'])
    east_df = map_df[map_df.Longitude > 0]
    west_df = map_df[map_df.Longitude <= 0]

    east_and_west_dict['East'] = construct_year_building_count(east_df)
    east_and_west_dict['West'] = construct_year_building_count(west_df)

    return east_and_west_dict

def construct_year_building_count(df):
    year_to_building_count = {}
    for row in df.itertuples():
        if row.COMPLETION in year_to_building_count.keys():
            building_count = year_to_building_count[row.COMPLETION]
            building_count += 1
            year_to_building_count[row.COMPLETION] = building_count
        else:
            year_to_building_count[row.COMPLETION] = 1

    return year_to_building_count

# Create Hemisphere Line Chart
def hemisphere_line_chart(hemisphere_dict, east_type, west_type):
    fig,ax = plt.subplots()

    if east_type:
        east_years = sorted(hemisphere_dict['East'])
        east_building_count = ([value for (key, value) in sorted(hemisphere_dict['East'].items())])
        ax.plot(east_years, east_building_count)
        ax.set_title("Skyscrapers Built Over Time by Hemisphere")
        ax.set_ylabel("Number of Skyscrapers Built")
        ax.set_xlabel("Year")

    if west_type:
        west_years = sorted(hemisphere_dict['West'])
        west_building_count = ([value for (key, value) in sorted(hemisphere_dict['West'].items())])
        ax.plot(west_years, west_building_count)
        ax.set_title("Skyscrapers Built Over Time by Hemisphere")
        ax.set_ylabel("Number of Skyscrapers Built")
        ax.set_xlabel("Year")

    st.pyplot(fig)

def display(df):
    hemisphere_dict = construct_hemisphere_data(df)

    # Create Header for Hemisphere Line Chart
    st.header("Skyscrapers By Hemisphere Over Time")
    east_type = st.checkbox("East of the Prime Meridian", value = True)
    west_type = st.checkbox('West of the Prime Meridian', value = True)

    hemisphere_line_chart(hemisphere_dict, east_type, west_type)

import streamlit as st
import matplotlib.pyplot as plt

def get_unique_materials(df):
    unique_materials = []
    material_list = df['MATERIAL'].tolist()
    for material in material_list:
        if material not in unique_materials:
            unique_materials.append(material)

    return unique_materials

def construct_material_data(df):
    material_dict = {}
    for row in df.itertuples():
        # print(f"{row.MATERIAL:20s}{row.COMPLETION}")
        if row.MATERIAL in material_dict.keys():
            year_to_building_count = material_dict[row.MATERIAL]
            building_count = 1
            if row.COMPLETION in year_to_building_count.keys():
                building_count = year_to_building_count[row.COMPLETION]
                building_count += 1

            year_to_building_count[row.COMPLETION] = int(building_count)
            material_dict[row.MATERIAL] = year_to_building_count
        else:
            year_to_building_count = {}
            year_to_building_count[row.COMPLETION] = int(1)
            material_dict[row.MATERIAL] = year_to_building_count

    return material_dict

# Create Bar Chart for Skyscrapers By Material
def skyscraper_material_plot(material_dict, material):
    global year_x_axis, num_y_axis
    year_x_axis = []
    num_y_axis = []
    for year, num in material_dict[material].items():
        year_x_axis.append(year)
        num_y_axis.append(num)

    return (year_x_axis, num_y_axis)

def display(df):
    material_dict = construct_material_data(df)

    # Create header for Skyscrapers By Material
    st.header("Skyscrapers By Material")
    material = st.selectbox(
        'Select which type of skyscraper to display: ',
        get_unique_materials(df)
    )

    st.write(f"This skyscraper is made out of {material} material.")
    year_x_axis, num_y_axis = skyscraper_material_plot(material_dict, material)

    fig, ax = plt.subplots()
    plt.yticks(num_y_axis)
    ax.bar(year_x_axis, num_y_axis, color = 'purple')
    ax.set_title('Skyscrapers Built Over Time by Material')
    ax.set_ylabel("Number of Skyscrapers Built")
    ax.set_xlabel("Year")
    st.pyplot(fig)

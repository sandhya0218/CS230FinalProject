import streamlit as st
import matplotlib.pyplot as plt

def get_unique_function(df):
    unique_functions = []
    clean_function_list = []
    function_dict = {}
    function_list = df['FUNCTION'].tolist()
    for function in function_list:
        for x in function.split(" / "):
            clean_function_list.append(x)
            if x not in unique_functions:
                unique_functions.append(x)

    # print(clean_function_list)

    function_count = 0
    for function in clean_function_list:
        if function in function_dict.keys():
            function_dict[function] += 1
        else:
            function_dict[function] = 1

    # pp.pprint(function_dict)

    return unique_functions, function_dict

def display(df):
    st.header("Skyscrapers By Building Function")
    unique_function_dict = get_unique_function(df)

    # Create Pie Chart for Skyscrapers By Building Function
    fig,ax = plt.subplots()
    ax.axis('equal')
    ax.pie(unique_function_dict[1].values(), labels = None, autopct='%0.2f%%', pctdistance=1.2, radius=1.0)
    # labels = [f'{l}, {s:0.1f}%' for l, s in zip(unique_function_dict[1].keys(), unique_function_dict[1].values())]
    ax.legend(bbox_to_anchor=(0,1), loc = 'right', labels = unique_function_dict[1].keys())
    st.pyplot(fig)

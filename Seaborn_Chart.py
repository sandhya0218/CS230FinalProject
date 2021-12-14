import seaborn as sns
import streamlit as st

# I used https://seaborn.pydata.org/generated/seaborn.relplot.html
def display(df):
    st.subheader("Relationship between Completion Year and Number of Floors by Material")
    fig = sns.relplot(x='COMPLETION', y='FLOORS', data = df, hue = 'MATERIAL')
    st.pyplot(fig)




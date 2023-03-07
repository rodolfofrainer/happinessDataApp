import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('happy.csv')

st.title('In Search of Happiness')

x_axis = st.selectbox('Data for X-axis',
                      ["GDP", "Happiness", "Generosity"])

y_axis = st.selectbox('Data for Y-axis',
                      ["GDP", "Happiness", "Generosity"])

st.subheader(f'{x_axis} and {y_axis}')
scatter_graph = px.scatter(
    x=df[x_axis.lower()],
    y=df[y_axis.lower()],
    labels={"x": f"{x_axis}", "y": f"{y_axis}"})

st.plotly_chart(scatter_graph)

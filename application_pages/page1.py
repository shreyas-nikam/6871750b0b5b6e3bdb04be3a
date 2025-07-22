
import streamlit as st
import pandas as pd
import plotly.express as px

def run_page1():
    st.header("Page 1: Introduction to Risk")
    st.write("This page provides an introduction to the concept of risk and its importance in operational management.")
    df = pd.DataFrame({'Risk Type': ['Operational', 'Financial', 'Strategic'], 'Description': ['Risks from internal processes', 'Risks from market fluctuations', 'Risks from business strategy']})
    st.dataframe(df)
    fig = px.bar(df, x='Risk Type', y='Description')
    st.plotly_chart(fig)


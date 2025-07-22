
import streamlit as st
import pandas as pd
import plotly.express as px

def run_page2():
    st.header("Page 2: Risk Assessment")
    st.write("This page demonstrates a simple risk assessment process.")
    df = pd.DataFrame({'Risk': ['Cybersecurity breach', 'Supply chain disruption', 'Regulatory non-compliance'], 'Likelihood': [0.6, 0.3, 0.2], 'Impact': [10, 8, 7]})
    df['Risk Score'] = df['Likelihood'] * df['Impact']
    st.dataframe(df)
    fig = px.scatter(df, x='Likelihood', y='Impact', text='Risk', size='Risk Score')
    fig.update_traces(textposition='top center')
    st.plotly_chart(fig)



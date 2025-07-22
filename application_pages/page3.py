
import streamlit as st
import pandas as pd
import plotly.express as px

def run_page3():
    st.header("Page 3: Risk Mitigation")
    st.write("This page explores various risk mitigation strategies.")
    df = pd.DataFrame({'Mitigation Strategy': ['Insurance', 'Redundancy', 'Process improvement'], 'Description': ['Transferring risk to an insurer', 'Creating backups to minimize disruption', 'Improving processes to reduce risk']})
    st.dataframe(df)
    fig = px.pie(df, values='Description', names='Mitigation Strategy')
    st.plotly_chart(fig)


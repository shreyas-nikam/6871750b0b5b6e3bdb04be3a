
import streamlit as st

st.set_page_config(page_title="Risk Appetite Framework Explorer", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("Risk Appetite Framework Explorer")
st.divider()
st.markdown("""
This application provides an interactive environment for understanding and managing operational risk within an organization.
It simulates key elements of an operational risk appetite framework, allowing users to define risk tolerance levels and observe their implications on a simulated organization's risk profile and capital management.

**Purpose and Objectives:**
* Simulate Operational Risk: Generate synthetic time-series data for business operations, financial performance, and simulated operational loss events.
* Define Risk Appetite: Enable users to set quantitative risk appetite statements (e.g., maximum acceptable Expected Loss, Unexpected Loss, tolerance for severe loss events, KRI limits).
* Visualize Risk Profile & Capacity: Display the simulated 'Risk Capacity' and evolving 'Risk Profile' over time, comparing them against defined risk appetite thresholds.
* Monitor Breaches: Track and visualize instances where the simulated risk profile exceeds the defined risk appetite.
* KRI Dashboard: Present a dashboard of simulated Key Risk Indicators (KRIs) and their status relative to pre-set thresholds.
* Educational Value: Help users understand core risk management concepts such as Risk Capacity, Risk Appetite, Expected Loss ($EL$), Unexpected Loss ($UL$), and Key Risk Indicators (KRIs), as outlined in the 'Operational Risk Manager Handbook' [1].
""")

page = st.sidebar.selectbox(label="Navigation", options=["Data Generation & Risk Appetite", "Risk Profile Calculation & Monitoring", "Visualizations & References"])

if page == "Data Generation & Risk Appetite":
    from application_pages.page1 import run_page1
    run_page1()
elif page == "Risk Profile Calculation & Monitoring":
    from application_pages.page2 import run_page2
    run_page2()
elif page == "Visualizations & References":
    from application_pages.page3 import run_page3
    run_page3()

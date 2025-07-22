
import streamlit as st
st.set_page_config(page_title="Module 6 Lab 1", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("Module 6 Lab 1")
st.divider()
st.markdown(\"\"\"
This lab explores the concepts of risk appetite and its impact on operational risk management.  You'll be able to interactively define risk tolerance levels and see their effects on simulated organizational risk profiles and capital management.  This lab uses synthetic data to demonstrate the relationships between various risk management concepts and parameters.
\"\"\")
page = st.sidebar.selectbox(label="Navigation", options=["Page 1", "Page 2", "Page 3"])
if page == "Page 1":
    from application_pages.page1 import run_page1
    run_page1()
elif page == "Page 2":
    from application_pages.page2 import run_page2
    run_page2()
elif page == "Page 3":
    from application_pages.page3 import run_page3
    run_page3()


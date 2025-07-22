
import streamlit as st
st.set_page_config(page_title="QuLab", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab")
st.divider()
st.markdown("""
In this lab, we will explore the Risk Appetite Framework. This framework is a key component of operational risk management, allowing organizations to define their risk tolerance and monitor their risk profile against these defined thresholds.

We will simulate various business operations, revenues, and loss events to generate synthetic data. Users can adjust parameters such as growth rate, loss frequency, and loss severity to observe their impact on key risk metrics.

**Key Concepts:**

*   **Risk Capacity:** The maximum amount of risk an organization can take, often determined by its financial resources or regulatory requirements.
*   **Risk Appetite:** The level of risk an organization is willing to accept in pursuit of its objectives.
*   **Expected Loss ($EL$):** The average loss an organization expects to incur over a given period.
    $$EL = rac{1}{n} \sum_{i=1}^{n} L_i$$
*   **Unexpected Loss ($UL$):** The potential for losses to exceed the expected loss, often quantified using the standard deviation.
    $$UL = \sqrt{rac{1}{n-1} \sum_{i=1}^{n} (L_i - EL)^2}$$
*   **Key Risk Indicators (KRIs):** Metrics used to monitor and track key risks within the organization.

This application will provide a dynamic environment to:

1.  **Simulate Data:** Generate synthetic time-series data for business operations, financial performance, and simulated operational loss events.
2.  **Define Risk Appetite:** Enable users to set quantitative risk appetite statements (e.g., maximum acceptable Expected Loss, Unexpected Loss, tolerance for severe loss events, KRI limits).
3.  **Visualize Risk Profile & Capacity:** Display the simulated 'Risk Capacity' and evolving 'Risk Profile' over time, comparing them against defined risk appetite thresholds.
4.  **Monitor Breaches:** Track and visualize instances where the simulated risk profile exceeds the defined risk appetite.
5.  **KRI Dashboard:** Present a dashboard of simulated Key Risk Indicators (KRIs) and their status relative to pre-set thresholds.
""")
# Your code starts here
page = st.sidebar.selectbox(label="Navigation", options=["Data Generation & Visualization", "Risk Profile & Monitoring", "References"])
if page == "Data Generation & Visualization":
    from application_pages.page1 import run_page1
    run_page1()
elif page == "Risk Profile & Monitoring":
    from application_pages.page2 import run_page2
    run_page2()
elif page == "References":
    from application_pages.page3 import run_page3
    run_page3()
# Your code ends

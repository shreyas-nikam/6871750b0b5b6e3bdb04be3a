
import streamlit as st

st.set_page_config(page_title=\"QuLab\", layout=\"wide\")
st.sidebar.image(\"https://www.quantuniversity.com/assets/img/logo5.jpg\")
st.sidebar.divider()
st.title(\"QuLab: Risk Appetite Framework Explorer\")
st.divider()
st.markdown(r\"\"
## Module 6 Lab 1: Interactive Operational Risk Appetite Framework

Welcome to the **Risk Appetite Framework Explorer**. This lab lets you **simulate, define, and visualize** how an organization's risk appetite interacts with its operational risk profile and key risk indicators.

### Business Context
An effective **operational risk framework** helps organizations balance opportunity and protection by defining how much risk they're willing to accept — their **Risk Appetite**. 

With this application, you can:
* Simulate business and risk data using customizable parameters.
* Set thresholds for **Expected Loss ($EL$)**, **Unexpected Loss ($UL$)**, and **KRIs**.
* Visualize and monitor breaches in real time.
* Learn how **Risk Profile** and **Risk Capacity** interact.

#### Key Concepts (with formulae):

- **Expected Loss ($EL$):**
    $$
    EL = \frac{1}{n} \sum_{i=1}^n L_i
    $$
    where $L_i$ denotes the $i$th loss amount.

- **Unexpected Loss ($UL$):**
    $$
    UL = \sqrt{\frac{1}{n-1} \sum_{i=1}^n (L_i - EL)^2}
    $$

- **Key Risk Indicator (KRI):** Quantitative metric signaling elevated operational risk.

- **Risk Appetite:** The maximum loss or exposure levels the organization is willing to tolerate.

**Navigate using the sidebar** to explore simulation (Page 1), risk profile monitoring (Page 2), and KRI dashboard & references (Page 3).
\"\"\")
# ---- Page navigation ----
page = st.sidebar.selectbox(
    label=\"Navigation\",
    options=[\"Page 1: Data Generation\", \"Page 2: Risk Profile Monitoring\", \"Page 3: KRI Dashboard & References\"]
)
if page == \"Page 1: Data Generation\":
    from application_pages.page1 import run_page1
    run_page1()
elif page == \"Page 2: Risk Profile Monitoring\":
    from application_pages.page2 import run_page2
    run_page2()
elif page == \"Page 3: KRI Dashboard & References\":
    from application_pages.page3 import run_page3
    run_page3()

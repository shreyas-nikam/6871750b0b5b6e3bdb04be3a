id: 6871750b0b5b6e3bdb04be3a_documentation
summary: Module 6 Lab 1 Documentation
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# QuLab: Risk Appetite Framework Explorer Codelab

This codelab guides you through the QuLab application, a Risk Appetite Framework Explorer designed to simulate and visualize elements of an operational risk appetite framework. You will learn how to use the application to define risk tolerance levels and observe their impact on a simulated organization's risk profile and capital management. This tool provides a hands-on way to understand abstract risk concepts and their practical implications.

**Key Concepts Covered:**

*   Operational Risk Management
*   Risk Appetite Framework Components
*   Relationship Between Risk Appetite, Risk Capacity, and Risk Outcomes
*   Key Risk Indicators (KRIs) and their role in monitoring risk
*   Alignment of risk appetite with business strategy and capital allocation

Let's dive in!

## Setting up the Environment
Duration: 00:05

Before you start, make sure you have the following:

*   Python 3.6 or higher installed.
*   Streamlit installed (`pip install streamlit`).
*   Other required libraries installed (`pip install pandas numpy plotly`).

Create a directory for your project and save the provided code snippets for `app.py`, `application_pages/page1.py`, and `application_pages/page2.py`, and `application_pages/page3.py` into their respective files.

## Running the Application
Duration: 00:02

1.  Open your terminal.
2.  Navigate to the project directory where you saved `app.py`.
3.  Run the application using the command: `streamlit run app.py`

Streamlit will automatically open the application in your web browser.

## Understanding the Application Structure
Duration: 00:10

The application is structured into three main pages accessible via a sidebar navigation:

1.  **Data Generation:** Simulates business data (revenue, expenses, profit) and operational loss events.
2.  **Risk Appetite Definition:** Allows you to define risk appetite parameters like maximum expected loss, unexpected loss, and KRI limits.
3.  **Risk Monitoring:** (Not provided in the code, but would ideally) visualize the simulated risk profile against the defined risk appetite.

## Exploring the Data Generation Page
Duration: 00:15

This page focuses on generating synthetic data for business operations and operational losses.

1.  **Navigate to the "Data Generation" page:** Select "Data Generation" from the sidebar.
2.  **Observe the Sidebar Input Widgets:** The sidebar contains several input widgets to control the data generation process:
    *   **Start Date/End Date:** Defines the period for which data will be generated.
    *   **Average Daily Revenue:** The average revenue generated per day.
    *   **Revenue Volatility:** Controls the fluctuation in daily revenue.
    *   **Baseline Daily Expenses:** The fixed daily expenses.
    *   **Average Daily Losses:** The average number of operational losses per day (modeled using a Poisson distribution).
    *   **Severity Mu/Severity Sigma:** Parameters for the log-normal distribution used to simulate loss amounts.
    *   **Severe Loss Threshold:**  A threshold to classify losses as severe.
3.  **Interact with the Input Widgets:** Change the values of the input widgets and observe how the generated data and visualizations change. For example, increase the `Revenue Volatility` to see a more erratic revenue trend.
4.  **Review the Output:** The page displays two main sections:
    *   **Business Data:** A DataFrame showing the simulated revenue, expenses, and profit for each day, along with a line chart visualizing these trends.
    *   **Operational Losses Data:** A DataFrame containing simulated operational loss events, including the date and loss amount.  A histogram shows the distribution of loss amounts, and a bar chart compares the number of severe and non-severe losses.

**Code Snippets Explained (page1.py):**

*   `generate_business_data(start_date, end_date, avg_revenue, revenue_volatility, baseline_expenses)`: This function generates the business data time series. It uses a normal distribution to simulate revenue with a specified average and volatility, and fixed expenses.
*   `simulate_operational_losses(start_date, end_date, avg_daily_losses, severity_mu, severity_sigma, severe_loss_threshold)`:  This function simulates operational losses. It uses a Poisson distribution to determine the number of loss events per day and a log-normal distribution to simulate the loss amounts.
*   The `run_page1()` function handles the Streamlit UI, retrieves input values from the sidebar, calls the data generation functions, and displays the results using `st.dataframe` and `st.plotly_chart`.

## Exploring the Risk Appetite Definition Page
Duration: 00:10

This page allows you to define the risk appetite parameters for the simulated organization.

1.  **Navigate to the "Risk Appetite Definition" page:** Select "Risk Appetite Definition" from the sidebar.
2.  **Observe the Sidebar Input Widgets:** The sidebar provides widgets to define the following:
    *   **Max Expected Loss Threshold:** The maximum acceptable level of expected loss.
    *   **Max Unexpected Loss Threshold:** The maximum acceptable level of unexpected loss.
    *   **Severe Loss Event Tolerance:** The maximum number of severe loss events that are acceptable.
    *   **Number of KRIs:** Defines how many Key Risk Indicators you want to define.
    *   **KRI Limits:**  Allows you to set limits for each KRI.
3.  **Interact with the Input Widgets:** Modify the values of the risk appetite parameters and KRI limits.
4.  **Review the Output:** The page displays the values of the defined risk appetite parameters and KRI limits.

**Code Snippets Explained (page2.py):**

*   The `run_page2()` function creates the Streamlit UI for defining risk appetite parameters. It uses `st.sidebar.number_input` to collect input values from the user and then displays these values using `st.write`.

## (Hypothetical) Risk Monitoring Page & Putting it All Together
Duration: 00:20

<aside class="negative">
<b>Important:</b> The original code doesn't include a `page3.py` file or the "Risk Monitoring" page's logic.  This section outlines *how it *would* work* based on the application's description. You would need to implement this functionality.
</aside>

This page would be the heart of the application, where the simulated risk profile is compared against the defined risk appetite.  Here's how it *could* function:

1.  **Data Retrieval:**  The page would need to access the business data and operational losses data generated on the "Data Generation" page, as well as the risk appetite parameters defined on the "Risk Appetite Definition" page. One way to accomplish this is to store data to Streamlit's session state (st.session_state).

2.  **Risk Profile Calculation:**  The page would calculate the organization's risk profile based on the simulated data. This could involve:
    *   Calculating Expected Loss (EL) and Unexpected Loss (UL) based on the loss data. Use the formulas provided in the introduction of the main `app.py` file:
        *   $\text{Expected Loss (EL) = PD_A * L}$
        *   $\text{Unexpected Loss (UL) = 3 * sigma}$, estimated by $\text{UL = 3 * PD_A * (1 - PD_A) * L}$
        (Where $PD_A$ is the Probability of default, and $L$ is the loss)
    *   Calculating KRI values based on the business and loss data.  The specific calculations would depend on the nature of the KRIs (e.g., Loss Amount / Revenue, Number of Loss Events, etc.).

3.  **Breach Monitoring:** The page would compare the calculated risk profile against the defined risk appetite thresholds. It would identify instances where the risk profile exceeds the risk appetite.

4.  **Visualization:**  The page would present visualizations to show:
    *   The evolution of the risk profile over time, benchmarked against the risk appetite thresholds. This could be a line chart showing EL and UL over time, with horizontal lines indicating the maximum acceptable levels.
    *   Instances where the risk profile exceeds the risk appetite, highlighted as trend plots.
    *   A KRI dashboard showing the status of each KRI relative to its limit. This could use color-coding to indicate whether a KRI is within acceptable limits (green), approaching its limit (yellow), or exceeding its limit (red).

**Example `page3.py` Code (Conceptual):**

```python
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def calculate_el(loss_data):
    # Placeholder for Expected Loss calculation
    # Replace with your actual calculation logic
    if loss_data.empty:
        return 0
    return loss_data['Loss_Amount'].mean()  # Example: average loss amount

def calculate_ul(loss_data):
    # Placeholder for Unexpected Loss calculation
    # Replace with your actual calculation logic
    if loss_data.empty:
        return 0
    return loss_data['Loss_Amount'].std() * 3 # Example: 3 times standard deviation

def generate_kris(business_data, loss_data, num_kris):
    kris = {}
    # Example calculations, replace with real KRI definitions
    if num_kris >= 1:
        kris["KRI 1"] = loss_data['Loss_Amount'].sum() / business_data['Revenue'].sum() if not business_data.empty and not loss_data.empty else 0
    if num_kris >= 2:
        kris["KRI 2"] = len(loss_data) if not loss_data.empty else 0
    return kris

def run_page3():
    st.header("Risk Monitoring")

    # Example: Retrieving Data from Session State (You'd need to store it there first!)
    if 'business_data' not in st.session_state or 'losses_data' not in st.session_state:
        st.warning("Please generate data first on the 'Data Generation' page.")
        return

    business_data = st.session_state['business_data']
    losses_data = st.session_state['losses_data']
    # Assuming risk appetite parameters are also in session state
    max_expected_loss_threshold = st.session_state.get('max_expected_loss_threshold', 50000.0) #Provide a default
    max_unexpected_loss_threshold = st.session_state.get('max_unexpected_loss_threshold', 150000.0)
    num_kris = st.session_state.get('num_kris', 2)

    # Calculate Risk Profile
    el = calculate_el(losses_data)
    ul = calculate_ul(losses_data)
    kris = generate_kris(business_data, losses_data, num_kris)


    # Display Risk Profile and Compare to Risk Appetite
    st.subheader("Risk Profile")
    st.write(f"Expected Loss: {el}")
    st.write(f"Unexpected Loss: {ul}")

    if el > max_expected_loss_threshold:
        st.error(f"Expected Loss exceeds the threshold of {max_expected_loss_threshold}!")
    if ul > max_unexpected_loss_threshold:
        st.error(f"Unexpected Loss exceeds the threshold of {max_unexpected_loss_threshold}!")

    st.subheader("Key Risk Indicators")
    for kri_name, kri_value in kris.items():
        limit = st.session_state.get(f'{kri_name}_limit', 100.0) # Get Limit, provide default
        st.write(f"{kri_name}: {kri_value}")
        if kri_value > limit:
            st.error(f"{kri_name} exceeds its limit of {limit}!")

# To link properly:
# in app.py:
# elif page == "Risk Monitoring":
#     from application_pages.page3 import run_page3
#     run_page3()
```

## Key Takeaways

*   **Risk Appetite Framework:** The application demonstrates the core components of a risk appetite framework, including risk identification, risk measurement, risk appetite definition, and risk monitoring.
*   **Data-Driven Decision Making:** By simulating business data and operational losses, the application highlights the importance of using data to inform risk management decisions.
*   **Interactive Exploration:** The Streamlit interface allows you to interactively explore the relationship between risk appetite, risk profile, and business outcomes.

By completing this codelab, you have gained a practical understanding of how to build a Risk Appetite Framework Explorer using Streamlit. You can extend this application further by adding more sophisticated risk models, incorporating real-world data, and implementing advanced visualization techniques.

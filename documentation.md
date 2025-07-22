id: 6871750b0b5b6e3bdb04be3a_documentation
summary: Module 6 Lab 1 Documentation
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# QuLab: Risk Appetite Framework Explorer - Codelab

This codelab provides a comprehensive guide to understanding and utilizing the "QuLab: Risk Appetite Framework Explorer" Streamlit application. This application is designed to help developers and risk professionals simulate, define, and visualize an organization's risk appetite in relation to its operational risk profile and Key Risk Indicators (KRIs). By the end of this codelab, you will be able to:

*   Understand the key concepts of operational risk management, including Expected Loss (EL), Unexpected Loss (UL), KRIs, and Risk Appetite.
*   Navigate the application's three pages: Data Generation, Risk Profile Monitoring, and KRI Dashboard & References.
*   Configure simulation parameters to generate synthetic business and loss data.
*   Define risk appetite thresholds and monitor breaches.
*   Interpret visualizations and data tables to assess risk exposure.

## Step 1: Introduction and Setup
Duration: 00:05

This initial step will provide an overview of the application's purpose, key functionalities, and the concepts it illustrates. The Risk Appetite Framework Explorer is intended to bridge the gap between theoretical risk management principles and practical application.

## Step 2: Application Architecture
Duration: 00:10

The application is structured into three main pages, each addressing a specific aspect of the risk appetite framework:

*   **Page 1: Data Generation:** Allows users to simulate business operations and operational losses using configurable parameters.
*   **Page 2: Risk Profile Monitoring:** Enables users to define their organization's risk appetite and observe how the simulated risk profile performs against these thresholds.
*   **Page 3: KRI Dashboard & References:** Provides a summary of the Key Risk Indicator (KRI) performance and includes references to relevant resources.

Here's a simple diagram illustrating the application's flow:

```mermaid
graph LR
    A[Data Generation (Page 1)] --> B(Risk Profile Monitoring (Page 2));
    B --> C(KRI Dashboard & References (Page 3));
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#ccf,stroke:#333,stroke-width:2px
    style C fill:#ccf,stroke:#333,stroke-width:2px
```

## Step 3: Navigating the Application
Duration: 00:02

The application utilizes a Streamlit sidebar for navigation. The sidebar allows you to select which of the three pages to view. The main title and description are also present in the sidebar to provide context.

```python
import streamlit as st

st.set_page_config(page_title="QuLab", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab: Risk Appetite Framework Explorer")
st.divider()
```

The navigation is handled by a `selectbox` widget in the sidebar:

```python
page = st.sidebar.selectbox(
    label="Navigation",
    options=["Page 1: Data Generation", "Page 2: Risk Profile Monitoring", "Page 3: KRI Dashboard & References"]
)

if page == "Page 1: Data Generation":
    from application_pages.page1 import run_page1
    run_page1()
elif page == "Page 2: Risk Profile Monitoring":
    from application_pages.page2 import run_page2
    run_page2()
elif page == "Page 3: KRI Dashboard & References":
    from application_pages.page3 import run_page3
    run_page3()
```

## Step 4: Page 1 - Data Generation
Duration: 00:15

This page allows you to generate synthetic data for business operations and operational losses. This synthetic data will then be used in the subsequent pages for risk profile monitoring and KRI analysis. The simulation parameters are configured via sliders in the sidebar.

### Data Generation Parameters

The sidebar contains several sliders to control the simulation:

*   **Simulation Start/End Date:** Defines the date range for the simulation.
*   **Growth Rate:**  The annual growth rate for business volume.
*   **Loss Frequency Mean/Std Dev:** Parameters for the Poisson distribution used to simulate the number of loss events per day.
*   **Loss Severity Mean/Std Dev:** Parameters for the Normal distribution used to simulate the amount of each loss event.
*   **KRI Baseline/Volatility:** Parameters for the Normal distribution used to simulate the Key Risk Indicator (KRI).

### Data Generation Logic

The core data generation logic resides in the `generate_synthetic_data` function:

```python
@st.cache_data(show_spinner=False)
def generate_synthetic_data(start_date, end_date, business_params, loss_freq_params, loss_sev_params, kpi_params):
    # ... (implementation details) ...
    return df_simulated_operations, df_loss_events
```

<aside class="positive">
The `@st.cache_data` decorator is used to cache the results of the function. This improves performance by preventing the function from being re-executed unless the input parameters change.
</aside>

The function performs the following steps:

1.  **Generates Dates:** Creates a date range based on the provided start and end dates.
2.  **Simulates Business Volume:**  Models business growth exponentially using the provided growth rate.
3.  **Calculates Revenue:**  Computes revenue as a percentage of business volume.
4.  **Simulates Loss Events:**  Simulates loss events per day using a Poisson distribution for frequency and a Normal distribution for severity.
5.  **Simulates KRI:**  Generates KRI values using a Normal distribution with the specified baseline and volatility.

### Output

The page displays:

*   A preview of the simulated business operations data (Business Volume, Revenue, and KRI).
*   A line chart visualizing Business Volume and Revenue over time.
*   A line chart visualizing KRI over time.
*   A preview of the simulated loss events data.
*   A histogram visualizing the distribution of simulated loss amounts.

## Step 5: Page 2 - Risk Profile Monitoring
Duration: 00:20

This page allows you to define your organization's risk appetite and monitor the simulated risk profile against these thresholds.

### Risk Appetite Definition

The sidebar allows you to define the following risk appetite parameters:

*   **Max Expected Loss (EL):** The maximum average loss your organization expects to incur over the period.
*   **Max Unexpected Loss (UL):** The maximum potential loss deviation from EL.
*   **Max Severe Loss Events:** Tolerance for the number of 'severe' operational loss events.
*   **KRI Limit:** A threshold for the Key Risk Indicator.
*   **Risk Capacity:** Total capital buffer available for losses (for illustrative purposes).

### Risk Profile Calculation

The `calculate_risk_profile` function calculates the risk profile based on the simulated data and the defined risk appetite parameters:

```python
@st.cache_data(show_spinner=False)
def calculate_risk_profile(df_simulated_operations, df_loss_events, user_parameters):
    # ... (implementation details) ...
    return df_risk_profile.fillna(0)
```

The function calculates:

*   **Expected Loss (EL):**  The average of the loss amounts.
    $$
    EL = \frac{1}{n} \sum_{i=1}^n L_i
    $$
*   **Unexpected Loss (UL):**  The standard deviation of the loss amounts.
    $$
    UL = \sqrt{\frac{1}{n-1} \sum_{i=1}^n (L_i - EL)^2}
    $$
*   **KRI Exceeded:**  A boolean flag indicating whether the KRI exceeds the defined limit.

### Risk Appetite Monitoring

The `monitor_risk_appetite` function monitors the risk profile against the defined risk appetite:

```python
@st.cache_data(show_spinner=False)
def monitor_risk_appetite(df_risk_profile, risk_appetite_params):
    # ... (implementation details) ...
    return df_breaches, df_kri_status
```

The function generates two dataframes:

*   `df_breaches`:  Indicates whether Expected Loss and Unexpected Loss are within the defined appetite.
*   `df_kri_status`:  Indicates whether the KRI is within the defined limit.

### Output

The page displays:

*   A table showing the calculated risk profile (EL, UL, KRI, KRI Exceeded).
*   Tables showing the breach status for EL and UL.
*   A table showing the KRI status.
*   A line chart visualizing EL and UL over time, with horizontal lines indicating the risk appetite thresholds.
*   A line chart visualizing KRI over time, with a horizontal line indicating the KRI limit and markers indicating breaches.

## Step 6: Page 3 - KRI Dashboard & References
Duration: 00:10

This page provides a summary of the KRI performance and includes references to relevant resources.

### KRI Performance Dashboard

The KRI Performance Dashboard summarizes the KRI status against the defined KRI Limit. It calculates and displays:

*   Total simulation days.
*   Number of days the KRI was above the limit.
*   Percentage of days the KRI was above the limit.

These metrics provide a quick overview of the frequency and severity of KRI breaches, enabling stakeholders to assess the overall effectiveness of risk controls and mitigation strategies.

### Visualizations

The page includes the following visualizations:

*   A table displaying the daily KRI status.
*   A bar chart visualizing the distribution of KRI status (Within Limit vs. Above Limit).

### References

The References section provides links to relevant resources, including the "Operational Risk Manager Handbook" and a GitHub repository with lab exercises.

```
References:

*   [1] **Chapter 3: The Risk Management Framework, Chapter 5: Risk Information**, Operational Risk Manager Handbook, [Provided Document]. These sections discuss risk capacity, risk appetite, risk profile, and key risk indicators.
*   [2] dalmirPereira/module6_labWork: Lab Exercises from Module 6 - GitHub, https://github.com/dalmirPereira/module6_labWork.
```

## Step 7: Key Takeaways and Further Exploration
Duration: 00:03

This codelab provided a step-by-step guide to understanding and utilizing the "QuLab: Risk Appetite Framework Explorer" Streamlit application.  You have learned how to simulate data, define risk appetite, monitor risk profiles, and analyze KRI performance.

To further explore the application, consider the following:

*   Experiment with different simulation parameters to observe their impact on the risk profile.
*   Define different risk appetite thresholds and assess the sensitivity of the breach status.
*   Extend the application by adding new features, such as stress testing or scenario analysis.

<aside class="positive">
This application provides a valuable tool for understanding and managing operational risk. By combining simulation, visualization, and interactive controls, it empowers risk professionals to make informed decisions and effectively manage their organization's risk exposure.
</aside>

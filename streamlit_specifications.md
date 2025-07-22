
# Streamlit Application Requirements Specification: Risk Appetite Framework Explorer

## 1. Application Overview

The Streamlit application, "Risk Appetite Framework Explorer," aims to provide an interactive simulation environment for understanding and managing operational risk within an organization. It allows users to define risk tolerance levels and observe their implications on a simulated organization's risk profile and capital management.

**Purpose and Objectives:**
*   **Simulate Operational Risk Management:** Dynamically illustrate the core concepts of a Risk Appetite Framework, including Risk Capacity, Risk Appetite, Risk Profile, and Key Risk Indicators (KRIs).
*   **Facilitate Informed Decision-Making:** Provide a dynamic and interactive tool for risk managers and stakeholders to understand how different risk appetite settings impact an organization's risk profile, fostering better decisions on risk-taking and capital allocation.
*   **Educational Tool:** Serve as a learning aid to clarify abstract risk management concepts, showing the relationship between defined risk parameters and simulated risk outcomes.

**Key Features:**
*   **Synthetic Data Generation:** On-demand generation of time-series data for business operations, financial performance, and simulated operational loss events.
*   **Interactive Risk Appetite Definition:** User-configurable quantitative risk appetite statements via intuitive controls.
*   **Risk Profile Visualization:** Display of the simulated 'Risk Capacity' and evolving 'Risk Profile' compared against defined thresholds.
*   **Breach Monitoring:** Tracking and visualization of instances where the simulated risk profile exceeds defined risk appetite thresholds.
*   **KRI Dashboard:** Presentation of simulated Key Risk Indicators and their status relative to pre-set limits.

## 2. User Interface Requirements

The application will feature a clear, intuitive layout designed for ease of use and immediate feedback.

**Layout and Navigation Structure:**
*   **Sidebar:** Will host global configuration parameters, including data generation settings and risk appetite definitions. This ensures core controls are always accessible.
*   **Main Content Area:** Will display the generated data, calculated risk profile metrics, and various visualizations, structured logically with distinct sections for each stage of the analysis (Data, Risk Appetite, Risk Profile, Monitoring).

**Input Widgets and Controls:**
Users will interact with the application primarily through sidebar widgets:
*   **Data Generation Parameters (under a `st.expander` or dedicated section):**
    *   **Date Range:** `st.date_input` for `start_date` and `end_date`.
    *   **Business Parameters:** `st.number_input` or `st.slider` for `growth_rate` (e.g., 0.01 to 0.05).
    *   **Loss Frequency Parameters:** `st.number_input` or `st.slider` for `mean` loss events per period (e.g., 1 to 10).
    *   **Loss Severity Parameters:** `st.number_input` or `st.slider` for `mean` loss amount (e.g., 500 to 5000) and `std` deviation (e.g., 100 to 1000).
    *   **KRI Parameters:** `st.number_input` or `st.slider` for `baseline` KRI value (e.g., 40 to 60) and `volatility` (e.g., 1 to 10).
*   **Risk Appetite Definition Parameters (under a `st.expander` or dedicated section):**
    *   **Max Expected Loss:** `st.slider` or `st.number_input` for a float value (e.g., 500 to 2000), with tooltip: "The average loss an organization expects to incur over a given time horizon."
    *   **Max Unexpected Loss:** `st.slider` or `st.number_input` for a float value (e.g., 100 to 500), with tooltip: "The potential for losses exceeding the expected loss, typically quantified using Value at Risk (VaR)."
    *   **Max Severe Loss Events:** `st.slider` or `st.number_input` for an integer value (e.g., 0 to 5), with tooltip: "Maximum number of significant operational loss events tolerated."
    *   **KRI Limit:** `st.slider` or `st.number_input` for a float value (e.g., 50 to 80), with tooltip: "The threshold for the Key Risk Indicator, beyond which risk appetite is challenged."
    *   **Risk Capacity:** `st.slider` or `st.number_input` for a float value (e.g., 1000 to 10000), with tooltip: "The total capital buffer available to absorb unexpected losses."

**Visualization Components:**
The main content area will display interactive charts and tables:
*   **Simulated Operations and KRI Trend:**
    *   A multi-line chart showing `BusinessVolume`, `Revenue`, and `KRI` over time.
    *   The `KRI` line will be accompanied by a horizontal line indicating the `KRI Limit` defined by the user.
    *   Color-blind-friendly palette and font size $\ge$ 12pt.
*   **Operational Loss Events:**
    *   A table displaying `df_loss_events.head()` to show raw loss data.
    *   A histogram of `LossAmount` to show distribution of losses.
*   **Risk Profile Trends:**
    *   A line chart for `ExpectedLoss` over time, with a horizontal line for `Max Expected Loss` threshold.
    *   A line chart for `UnexpectedLoss` over time, with a horizontal line for `Max Unexpected Loss` threshold.
*   **Breach and KRI Status Dashboards:**
    *   Tables (`df_breaches`, `df_kri_status`) showing per-period status (e.g., "Breached" / "Within Appetite", "Above Limit" / "Within Limit").
    *   Summary bar charts or pie charts indicating the count or proportion of periods where breaches or KRI limits were exceeded.

**Interactive Elements and Feedback Mechanisms:**
*   All charts will be interactive, allowing for zoom, pan, and hover (tooltips).
*   Input changes in the sidebar will immediately trigger re-calculation and re-rendering of all dependent charts and tables in the main content area.
*   Informative `st.info` or `st.success` messages will confirm successful data generation or parameter updates.

## 3. Additional Requirements

**Real-time Updates and Responsiveness:**
*   The Streamlit application will inherently support real-time updates. Any change to an input widget (sliders, date inputs, number inputs) will automatically trigger a re-execution of the relevant Python code, updating all derived visualizations and tables responsively. This ensures an immediate feedback loop for the user.

**Annotation and Tooltip Specifications:**
*   **Input Control Tooltips:** As described in "Input Widgets and Controls," all interactive input elements will include descriptive tooltips (using the `help` parameter in Streamlit widgets) to explain their purpose and impact on the simulation.
*   **Chart Annotations:**
    *   Threshold lines (e.g., `Max Expected Loss`, `Max Unexpected Loss`, `KRI Limit`) will be explicitly drawn on relevant time-series charts using distinct colors and labels to clearly indicate the user-defined risk appetite boundaries.
    *   Breach points on the `ExpectedLoss` and `UnexpectedLoss` trend plots can be highlighted with markers or shaded regions to visually emphasize periods where risk appetite was exceeded.
*   **Chart Legends and Labels:** All visualizations will adhere to best practices for data visualization, including clear titles, properly labeled axes (with units where applicable), and legends to distinguish different data series.

## 4. Notebook Content and Code Requirements

This section details the specific Python code from the Jupyter Notebook that will be integrated into the Streamlit application, along with how it maps to interactive components.

**4.1. Application Setup and Environment Configuration**

*   **Description:** While `!pip install` is for environment setup and not part of the Streamlit app code itself, the `configure_notebook_environment` function contains useful settings for pandas display and basic logging which can be adapted for Streamlit.
*   **Streamlit Implementation:**
    *   The `pd.set_option` calls can be placed at the very top of the Streamlit script to ensure consistent DataFrame display.
    *   Basic logging can be handled by Streamlit's built-in `st.info`, `st.warning`, `st.error` for user feedback, or a more robust logging configuration if detailed server-side logs are needed.
*   **Code Reference (Modified for Streamlit):**
    ```python
    import pandas as pd
    import numpy as np
    from datetime import datetime, timedelta
    import streamlit as st
    import plotly.express as px

    # --- Configuration (equivalent to configure_notebook_environment) ---
    pd.set_option("display.max_columns", None)
    pd.set_option("display.expand_frame_repr", False)
    pd.set_option("display.max_rows", 200)
    # Logging in Streamlit is typically handled via st.write/info/warning/error
    # or by configuring standard Python logging to output to console/file.
    ```

**4.2. Synthetic Data Generation**

*   **Description:** This function generates the core time-series data for business operations, revenue, operational loss events, and a Key Risk Indicator (KRI). It's crucial for the simulation's dynamic nature.
*   **Streamlit Implementation:**
    *   Inputs for `start_date`, `end_date`, `business_params`, `loss_freq_params`, `loss_sev_params`, and `kpi_params` will be gathered from `st.date_input`, `st.number_input`, and `st.slider` widgets in the sidebar.
    *   The function will be called whenever these input parameters change.
    *   The output DataFrames (`df_simulated_operations`, `df_loss_events`) will be stored, potentially using `st.session_state` or passed explicitly.
    *   Initial display: `st.dataframe` for `df_simulated_operations.head()` and `df_loss_events.head()`.
    *   Visualizations: Plot `BusinessVolume`, `Revenue`, and `KRI` over time.
*   **Code Reference:**
    ```python
    def generate_synthetic_data(start_date, end_date, business_params, loss_freq_params, loss_sev_params, kpi_params):
        """Generates synthetic time-series data."""

        if not isinstance(start_date, datetime) or not isinstance(end_date, datetime):
            raise TypeError("start_date and end_date must be datetime objects.")

        if start_date > end_date:
            raise ValueError("start_date must be before end_date.")

        dates = pd.date_range(start_date, end_date)
        df_simulated_operations = pd.DataFrame({'Date': dates})

        # Business Volume
        growth_rate = business_params.get('growth_rate', 0.01)  # Default to 1% growth
        df_simulated_operations['BusinessVolume'] = 100.0  # Initialize as float to allow for growth
        for i in range(1, len(df_simulated_operations)):
            df_simulated_operations.loc[i, 'BusinessVolume'] = df_simulated_operations.loc[i-1, 'BusinessVolume'] * (1 + growth_rate)
        df_simulated_operations['BusinessVolume'] = df_simulated_operations['BusinessVolume'].astype(int) # Cast to int after calculation


        # Revenue
        df_simulated_operations['Revenue'] = df_simulated_operations['BusinessVolume'] * 0.1

        # Loss Events
        loss_mean = loss_freq_params.get('mean', 2)
        # Note: Poisson distribution intrinsically has mean=variance, so 'std' param from notebook is unusual for direct Poisson.
        # It's likely intended as a modifier or for normal distribution of number of losses.
        # For direct Poisson, std is sqrt(mean). Will use mean for Poisson param.
        loss_sev_mean = loss_sev_params.get('mean', 1000)
        loss_sev_std = loss_sev_params.get('std', 200)

        loss_dfs = [] # Initialize an empty list to collect loss event DataFrames

        for date in dates:
            num_losses = np.random.poisson(loss_mean) # Using loss_mean for Poisson lambda
            if num_losses > 0:
                loss_amounts = np.random.normal(loss_sev_mean, loss_sev_std, num_losses)
                temp_df = pd.DataFrame({'Date': [date] * num_losses, 'LossAmount': loss_amounts})
                loss_dfs.append(temp_df) # Append non-empty DataFrames to the list

        if loss_dfs: # Concatenate only if the list is not empty
            df_loss_events = pd.concat(loss_dfs, ignore_index=True)
        else:
            df_loss_events = pd.DataFrame(columns=['Date', 'LossAmount']) # Create an empty DataFrame if no losses

        df_loss_events['LossAmount'] = df_loss_events['LossAmount'].abs() #Making sure LossAmount is positive


        # Key Risk Indicator
        baseline = kpi_params.get('baseline', 50)
        volatility = kpi_params.get('volatility', 5)
        df_simulated_operations['KRI'] = np.random.normal(baseline, volatility, len(df_simulated_operations))

        return df_simulated_operations, df_loss_events
    ```

**4.3. Risk Appetite Parameter Definition**

*   **Description:** This section defines the quantitative thresholds for risk appetite. The original notebook used `ipywidgets`; for Streamlit, these will be replaced with native Streamlit input widgets in the sidebar.
*   **Streamlit Implementation:**
    *   Create `st.slider` or `st.number_input` widgets for each parameter within the sidebar.
    *   Collect their values into a dictionary (`risk_appetite_params`) to be passed to subsequent functions.
*   **Code Reference (Conceptual - using Streamlit widgets):**
    ```python
    # In Streamlit sidebar:
    st.sidebar.subheader("Define Risk Appetite Parameters")
    max_expected_loss_threshold = st.sidebar.slider(
        "Max Expected Loss ($EL$):",
        min_value=0.0, max_value=5000.0, value=1300.0, step=10.0,
        help="The average loss an organization expects to incur over a given time horizon."
    )
    max_unexpected_loss_threshold = st.sidebar.slider(
        "Max Unexpected Loss ($UL$):",
        min_value=0.0, max_value=1000.0, value=380.0, step=10.0,
        help="The potential for losses exceeding the expected loss, typically quantified using Value at Risk (VaR)."
    )
    max_severe_loss_events = st.sidebar.slider(
        "Max Severe Loss Events:",
        min_value=0, max_value=10, value=2, step=1,
        help="Maximum number of significant operational loss events tolerated."
    )
    kri_limit_threshold = st.sidebar.slider(
        "KRI Limit:",
        min_value=0.0, max_value=100.0, value=55.0, step=1.0,
        help="The threshold for the Key Risk Indicator, beyond which risk appetite is challenged."
    )
    risk_capacity = st.sidebar.slider(
        "Risk Capacity:",
        min_value=0.0, max_value=20000.0, value=10000.0, step=100.0,
        help="The total capital buffer available to absorb unexpected losses."
    )

    user_risk_appetite_params = {
        'MaxExpectedLoss_Threshold': max_expected_loss_threshold,
        'MaxUnexpectedLoss_Threshold': max_unexpected_loss_threshold,
        'MaxSevereLossEvents_Threshold': max_severe_loss_events, # Although not used in monitor_risk_appetite, included for completeness
        'KRI_Limit': kri_limit_threshold,
        'Risk_Capacity': risk_capacity # Although not used in monitor_risk_appetite, included for completeness
    }
    ```

**4.4. Risk Profile Calculation**

*   **Description:** This function computes key risk metrics ($EL$ and $UL$) from the simulated data and evaluates KRI status.
*   **Mathematical Formulas:**
    *   **Expected Loss (EL):**
        $$EL = \frac{1}{n} \sum_{i=1}^{n} L_i$$
        where $L_i$ is the $i$-th loss amount and $n$ is the total number of losses.
    *   **Unexpected Loss (UL):**
        $$UL = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (L_i - EL)^2}$$
        where $L_i$ is the $i$-th loss amount, $EL$ is the Expected Loss, and $n$ is the total number of losses.
*   **Streamlit Implementation:**
    *   Call this function after `generate_synthetic_data` and after `risk_appetite_params` are defined.
    *   Display `df_risk_profile.head()` using `st.dataframe`.
    *   Use Plotly to visualize `ExpectedLoss` and `UnexpectedLoss` trends, overlaying user-defined thresholds.
*   **Code Reference:**
    ```python
    def calculate_risk_profile(df_simulated_operations, df_loss_events, user_parameters):
        """Computes the organization's simulated risk profile over time."""

        if df_simulated_operations.empty and df_loss_events.empty:
            return pd.DataFrame()

        try:
            df_simulated_operations['Date'] = pd.to_datetime(df_simulated_operations['Date'])
            df_loss_events['Date'] = pd.to_datetime(df_loss_events['Date'])
        except Exception as e:
            # For Streamlit, consider st.error for user-facing errors
            raise ValueError(f"Date conversion error: {e}")

        df_risk_profile = df_simulated_operations.copy()

        # Calculate Expected Loss (EL)
        df_risk_profile['ExpectedLoss'] = df_loss_events['LossAmount'].mean() if not df_loss_events.empty else 0

        # Calculate Unexpected Loss (UL) - Simple example: standard deviation
        df_risk_profile['UnexpectedLoss'] = df_loss_events['LossAmount'].std() if not df_loss_events.empty else 0

        # Incorporate KRI values (example: flag if KRI exceeds limit)
        # Ensure 'KRI_Limit' key exists in user_parameters
        if 'KRI' in df_risk_profile.columns and 'KRI_Limit' in user_parameters:
            df_risk_profile.loc[:, 'KRI_Exceeded'] = df_risk_profile['KRI'] > user_parameters['KRI_Limit']
        else:
            # Handle case where KRI_Exceeded might not be set due to missing KRI or KRI_Limit
            df_risk_profile.loc[:, 'KRI_Exceeded'] = False

        return df_risk_profile
    ```

**4.5. Monitor Risk Appetite and Identify Breaches**

*   **Description:** This function compares the calculated risk profile against the defined risk appetite thresholds, identifying breaches and evaluating KRI status.
*   **Streamlit Implementation:**
    *   Call this function with `df_risk_profile` and the `user_risk_appetite_params`.
    *   Display `df_breaches.head()` and `df_kri_status.head()` using `st.dataframe`.
    *   Visualize breach occurrences on time-series plots (e.g., using different colors or markers for breached periods).
    *   Present summary statistics of breaches (e.g., total count, percentage of time breached) using `st.metric` or `st.bar_chart`.
*   **Code Reference:**
    ```python
    def monitor_risk_appetite(df_risk_profile, risk_appetite_params):
        """Compares risk profile against risk appetite, identifies breaches and evaluates KRI status."""

        if not isinstance(df_risk_profile, pd.DataFrame):
            raise TypeError("df_risk_profile must be a Pandas DataFrame.")
        if not isinstance(risk_appetite_params, dict):
            raise TypeError("risk_appetite_params must be a dictionary.")

        df_breaches = pd.DataFrame()
        df_kri_status = pd.DataFrame()

        if df_risk_profile.empty:
            return df_breaches, df_kri_status

        breach_data = []
        kri_status_data = []

        # Ensure 'Date' column is present for merging later if needed, or iterate
        # Assuming df_risk_profile has 'Date' column for context.
        # Original notebook iterates through rows, which is fine for small DFs.
        # For larger DFs, vectorized operations are preferred.

        # Prepare columns for vectorized checks
        df_risk_profile_copy = df_risk_profile.copy()
        df_risk_profile_copy['ExpectedLoss_Breached'] = 'N/A'
        df_risk_profile_copy['UnexpectedLoss_Breached'] = 'N/A'
        df_risk_profile_copy['KRI_Status'] = 'N/A'


        # Expected Loss Breaches
        if 'ExpectedLoss' in df_risk_profile_copy.columns and 'MaxExpectedLoss_Threshold' in risk_appetite_params:
            threshold = risk_appetite_params['MaxExpectedLoss_Threshold']
            df_risk_profile_copy.loc[df_risk_profile_copy['ExpectedLoss'] > threshold, 'ExpectedLoss_Breached'] = 'Breached'
            df_risk_profile_copy.loc[df_risk_profile_copy['ExpectedLoss'] <= threshold, 'ExpectedLoss_Breached'] = 'Within Appetite'
            # Also handle if ExpectedLoss is 0 (e.g. no losses generated)
            if not df_risk_profile_copy['ExpectedLoss'].any(): # If all ExpectedLoss are 0
                 df_risk_profile_copy.loc[:, 'ExpectedLoss_Breached'] = 'No Losses'


        # Unexpected Loss Breaches
        if 'UnexpectedLoss' in df_risk_profile_copy.columns and 'MaxUnexpectedLoss_Threshold' in risk_appetite_params:
            threshold = risk_appetite_params['MaxUnexpectedLoss_Threshold']
            df_risk_profile_copy.loc[df_risk_profile_copy['UnexpectedLoss'] > threshold, 'UnexpectedLoss_Breached'] = 'Breached'
            df_risk_profile_copy.loc[df_risk_profile_copy['UnexpectedLoss'] <= threshold, 'UnexpectedLoss_Breached'] = 'Within Appetite'
            # Also handle if UnexpectedLoss is 0 (e.g. no losses generated, std dev is 0/NaN)
            if not df_risk_profile_copy['UnexpectedLoss'].any() and not df_risk_profile_copy['UnexpectedLoss'].isna().all():
                 df_risk_profile_copy.loc[:, 'UnexpectedLoss_Breached'] = 'No Losses'


        # KRI Status
        if 'KRI' in df_risk_profile_copy.columns and 'KRI_Limit' in risk_appetite_params:
            threshold = risk_appetite_params['KRI_Limit']
            df_risk_profile_copy.loc[df_risk_profile_copy['KRI'] > threshold, 'KRI_Status'] = 'Above Limit'
            df_risk_profile_copy.loc[df_risk_profile_copy['KRI'] <= threshold, 'KRI_Status'] = 'Within Limit'

        # Construct df_breaches and df_kri_status from the processed df_risk_profile_copy
        df_breaches = df_risk_profile_copy[['Date', 'ExpectedLoss_Breached', 'UnexpectedLoss_Breached']].copy()
        df_kri_status = df_risk_profile_copy[['Date', 'KRI_Status']].copy()

        return df_breaches, df_kri_status
    ```

**4.6. References**

The application draws upon the following foundational concepts and external resources:
*   [1] Chapter 3: The Risk Management Framework, Chapter 5: Risk Information, Operational Risk Manager Handbook. These sections discuss risk capacity, risk appetite, risk profile, and key risk indicators.
*   [2] dalmirPereira/module6_labWork: Lab Exercises from Module 6 - GitHub, https://github.com/dalmirPereira/module6_labWork.

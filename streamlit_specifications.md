
# Streamlit Application Requirements Specification

## 1. Application Overview

The Streamlit application, "Risk Appetite Framework Explorer," aims to provide an interactive and dynamic environment for understanding and managing operational risk within an organization. It simulates key elements of an operational risk appetite framework, allowing users to define risk tolerance levels and observe their implications on a simulated organization's risk profile and capital management.

**Purpose and Objectives:**
*   **Simulate Operational Risk:** Generate synthetic time-series data for business operations, financial performance, and simulated operational loss events.
*   **Define Risk Appetite:** Enable users to set quantitative risk appetite statements (e.g., maximum acceptable Expected Loss, Unexpected Loss, tolerance for severe loss events, KRI limits).
*   **Visualize Risk Profile & Capacity:** Display the simulated 'Risk Capacity' and evolving 'Risk Profile' over time, comparing them against defined risk appetite thresholds.
*   **Monitor Breaches:** Track and visualize instances where the simulated risk profile exceeds the defined risk appetite.
*   **KRI Dashboard:** Present a dashboard of simulated Key Risk Indicators (KRIs) and their status relative to pre-set thresholds.
*   **Educational Value:** Help users understand core risk management concepts such as Risk Capacity, Risk Appetite, Expected Loss ($EL$), Unexpected Loss ($UL$), and Key Risk Indicators (KRIs), as outlined in the 'Operational Risk Manager Handbook' [1].

## 2. User Interface Requirements

The application will feature a clear, intuitive layout designed for ease of use and effective data exploration.

**Layout and Navigation Structure:**
*   **Sidebar:** All user input controls (sliders, date pickers, number inputs) will be placed in a Streamlit sidebar (`st.sidebar`) for easy access and parameter adjustment.
*   **Main Content Area:** The primary display area will showcase the generated data, calculated risk profile metrics, and various interactive visualizations (plots, tables), along with narrative explanations.
*   **Section Headers:** Clear `st.header` and `st.subheader` elements will be used to logically separate different parts of the application (e.g., "Data Generation Parameters," "Risk Appetite Definition," "Risk Profile & Breaches").

**Input Widgets and Controls:**
Users will interact with the application through various Streamlit widgets to configure the simulation and risk appetite:
*   **Date Inputs:**
    *   `Start Date`: `st.date_input` for the beginning of the simulation period.
    *   `End Date`: `st.date_input` for the end of the simulation period.
*   **Synthetic Data Parameters (Sliders/Number Inputs in sidebar):**
    *   `Business Growth Rate`: `st.slider` or `st.number_input` for `business_params['growth_rate']`.
    *   `Loss Frequency Mean`: `st.slider` or `st.number_input` for `loss_freq_params['mean']`.
    *   `Loss Frequency Standard Deviation`: `st.slider` or `st.number_input` for `loss_freq_params['std']`.
    *   `Loss Severity Mean`: `st.slider` or `st.number_input` for `loss_sev_params['mean']`.
    *   `Loss Severity Standard Deviation`: `st.slider` or `st.number_input` for `loss_sev_params['std']`.
    *   `KRI Baseline`: `st.slider` or `st.number_input` for `kpi_params['baseline']`.
    *   `KRI Volatility`: `st.slider` or `st.number_input` for `kpi_params['volatility']`.
*   **Risk Appetite Definition (Sliders/Number Inputs in sidebar):**
    *   `Max Expected Loss`: `st.slider` or `st.number_input` for `MaxExpectedLoss_Threshold`.
    *   `Max Unexpected Loss`: `st.slider` or `st.number_input` for `MaxUnexpectedLoss_Threshold`.
    *   `Max Severe Loss Events`: `st.slider` or `st.number_input` (currently not explicitly used in `monitor_risk_appetite` but specified in notebook features).
    *   `KRI Limit`: `st.slider` or `st.number_input` for `KRI_Limit`.
    *   `Risk Capacity`: `st.slider` or `st.number_input` (currently not explicitly used in calculations but specified in notebook features).

**Visualization Components:**
The main content area will display:
*   **Trend Plots:**
    *   Line or Area plots showing `BusinessVolume`, `Revenue`, and `KRI` over time from `df_simulated_operations`.
    *   Line plots showing `ExpectedLoss` and `UnexpectedLoss` over time from `df_risk_profile`, with horizontal lines indicating the user-defined `Max Expected Loss` and `Max Unexpected Loss` thresholds.
    *   Visualization of `KRI` against `KRI_Limit`, potentially with highlighted breaches.
*   **Relationship Plots:**
    *   A scatter plot showing `LossAmount` distribution or `LossAmount` vs. `BusinessVolume` (or `Revenue`) from `df_loss_events`.
*   **Aggregated Comparisons:**
    *   Histograms of `LossAmount` distribution.
    *   A bar chart or summary table indicating the count of `KRI_Exceeded` days or other breach counts.
*   **Tabular Data Displays:**
    *   `df_simulated_operations.head()`, `df_loss_events.head()` for initial data inspection.
    *   `df_risk_profile.head()` for calculated risk metrics.
    *   `df_breaches` table showing `ExpectedLoss` and `UnexpectedLoss` status over time.
    *   `df_kri_status` table showing `KRI` status over time.

**Interactive Elements and Feedback Mechanisms:**
*   **Real-time Updates:** Changes to input parameters will automatically re-run the relevant calculations and update visualizations immediately.
*   **Tooltips and Help Text:** Inline help text or tooltips (`st.help` or `help=`) will be provided for all input controls to describe their purpose.
*   **Visual Feedback:** Clear titles, labeled axes, and legends will be used for all charts. Breaches will be visually highlighted (e.g., using different colors or annotations on plots).

## 3. Additional Requirements

**Real-time Updates and Responsiveness:**
*   The Streamlit architecture inherently supports real-time updates. The application will leverage `st.cache_data` or `st.cache_resource` decorator for functions where appropriate (e.g., `generate_synthetic_data` if parameters don't change frequently, or for data loading) to ensure responsiveness and avoid unnecessary re-computation.
*   The application should respond promptly to user interactions with input widgets, redrawing plots and updating tables without significant lag, adhering to the "fewer than 5 minutes" execution time on mid-spec hardware.

**Annotation and Tooltip Specifications:**
*   All `st.slider`, `st.number_input`, `st.date_input` widgets will include a `help` argument to provide descriptive tooltips.
*   Charts will feature clear titles (`chart.properties(title=...)`), axis labels (`chart.encode(x=alt.X(...), y=alt.Y(...))`), and legends where applicable, following the color-blind-friendly palette.
*   Numerical thresholds (e.g., Max Expected Loss) will be annotated on relevant trend plots to clearly show the boundaries.

**General Style and Usability:**
*   Adopt a color-blind-friendly palette for all visualizations (e.g., using Altair's built-in schemes or custom color scales).
*   Ensure font size is readable, generally equivalent to $\geq 12 \text{ pt}$ for text and labels within visualizations.
*   Charts will be interactive where possible (e.g., zooming, panning, tooltips on hover).

## 4. Notebook Content and Code Requirements

This section details how the Jupyter notebook's content and code will be integrated into the Streamlit application, serving as the blueprint for development.

**4.1. Application Setup and Environment Configuration**
*   **Purpose:** Configure basic environment settings, primarily Pandas display options and logging. This ensures consistency and aids in debugging.
*   **Integration:** This function will be called once at the start of the Streamlit script execution.
*   **Code:**
    ```python
    import pandas as pd
    import numpy as np
    import logging
    import streamlit as st
    import altair as alt
    from datetime import datetime, timedelta

    # Configure logging at the module level or within a function called once
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def configure_notebook_environment():
        """Sets up display options for pandas (not directly applicable for Streamlit's display but good practice)."""
        pd.set_option("display.max_columns", None)
        pd.set_option("display.expand_frame_repr", False)
        pd.set_option("display.max_rows", 200)

    configure_notebook_environment() # Call this once when the script runs
    ```

**4.2. Synthetic Data Generation**
*   **Purpose:** Generate realistic synthetic time-series data for business operations, revenues, and simulated operational loss events, as well as Key Risk Indicators (KRIs). This provides a reproducible testbed for the risk framework.
*   **Integration:** This function will be called based on user-defined parameters in the sidebar. It can be cached using `@st.cache_data` to optimize performance if input parameters remain constant.
*   **Inputs (from Streamlit UI):**
    *   `start_date` (datetime object from `st.date_input`)
    *   `end_date` (datetime object from `st.date_input`)
    *   `business_params` (dictionary from `st.slider`/`st.number_input` for `growth_rate`)
    *   `loss_freq_params` (dictionary from `st.slider`/`st.number_input` for `mean`, `std`)
    *   `loss_sev_params` (dictionary from `st.slider`/`st.number_input` for `mean`, `std`)
    *   `kpi_params` (dictionary from `st.slider`/`st.number_input` for `baseline`, `volatility`)
*   **Outputs:** `df_simulated_operations` (Pandas DataFrame), `df_loss_events` (Pandas DataFrame).
*   **Data Validation and Handling:** The function includes basic date validation. For the Streamlit application, it's also important to confirm expected column names (`Date`, `BusinessVolume`, `Revenue`, `LossAmount`, `KRI`) and data types (e.g., `Date` as datetime, numeric columns as appropriate types) after generation, potentially logging summary statistics for numeric columns. While not explicitly in the provided `generate_synthetic_data` function, a separate validation step could be added as per user requirements.
*   **Code (incorporating Streamlit inputs):**
    ```python
    @st.cache_data(show_spinner=False)
    def generate_synthetic_data(start_date, end_date, business_params, loss_freq_params, loss_sev_params, kpi_params):
        """Generates synthetic time-series data for the Streamlit app."""
        if not isinstance(start_date, datetime) or not isinstance(end_date, datetime):
            raise TypeError("start_date and end_date must be datetime objects.")
        if start_date > end_date:
            raise ValueError("start_date must be before end_date.")

        dates = pd.date_range(start_date, end_date)
        df_simulated_operations = pd.DataFrame({'Date': dates})

        # Business Volume
        growth_rate = business_params.get('growth_rate', 0.01)
        df_simulated_operations['BusinessVolume'] = 100.0
        for i in range(1, len(df_simulated_operations)):
            df_simulated_operations.loc[i, 'BusinessVolume'] = df_simulated_operations.loc[i-1, 'BusinessVolume'] * (1 + growth_rate)
        df_simulated_operations['BusinessVolume'] = df_simulated_operations['BusinessVolume'].astype(int)

        # Revenue
        df_simulated_operations['Revenue'] = df_simulated_operations['BusinessVolume'] * 0.1

        # Loss Events
        loss_mean = loss_freq_params.get('mean', 2)
        loss_std = loss_freq_params.get('std', 1)
        loss_dfs = []
        for date in dates:
            num_losses = np.random.poisson(loss_mean) # Poisson for counts
            if num_losses > 0:
                loss_amounts = np.random.normal(loss_sev_params.get('mean', 1000), loss_sev_params.get('std', 200), num_losses)
                temp_df = pd.DataFrame({'Date': [date] * num_losses, 'LossAmount': loss_amounts})
                loss_dfs.append(temp_df)

        if loss_dfs:
            df_loss_events = pd.concat(loss_dfs, ignore_index=True)
            df_loss_events['LossAmount'] = df_loss_events['LossAmount'].abs() # Ensure positive loss amounts
        else:
            df_loss_events = pd.DataFrame(columns=['Date', 'LossAmount']) # Create an empty DataFrame if no losses

        # Key Risk Indicator
        baseline = kpi_params.get('baseline', 50)
        volatility = kpi_params.get('volatility', 5)
        df_simulated_operations['KRI'] = np.random.normal(baseline, volatility, len(df_simulated_operations))

        return df_simulated_operations, df_loss_events

    # Streamlit UI for data generation parameters (in sidebar)
    with st.sidebar:
        st.subheader("1. Data Generation Parameters")
        col_start, col_end = st.columns(2)
        with col_start:
            sim_start_date = st.date_input("Simulation Start Date", value=datetime(2022, 1, 1), help="Start date for synthetic data generation.")
        with col_end:
            sim_end_date = st.date_input("Simulation End Date", value=datetime(2022, 1, 31), help="End date for synthetic data generation.")

        st.markdown("**Business Parameters**")
        growth_rate = st.slider("Growth Rate", min_value=0.0, max_value=0.1, value=0.02, step=0.005, format="%.3f", help="Annual growth rate for business volume.")

        st.markdown("**Loss Frequency Parameters (Poisson)**")
        loss_freq_mean = st.slider("Loss Frequency Mean", min_value=0.5, max_value=10.0, value=2.0, step=0.1, format="%.1f", help="Average number of loss events per period.")
        loss_freq_std = st.slider("Loss Frequency Std Dev", min_value=0.1, max_value=5.0, value=1.0, step=0.1, format="%.1f", help="Standard deviation for loss event frequency.")


        st.markdown("**Loss Severity Parameters (Normal)**")
        loss_sev_mean = st.slider("Loss Severity Mean", min_value=100.0, max_value=5000.0, value=1200.0, step=50.0, help="Average amount of each loss event.")
        loss_sev_std = st.slider("Loss Severity Std Dev", min_value=10.0, max_value=1000.0, value=300.0, step=10.0, help="Standard deviation of loss event amounts.")

        st.markdown("**KRI Parameters**")
        kri_baseline = st.slider("KRI Baseline", min_value=10.0, max_value=100.0, value=50.0, step=1.0, help="Average level of the Key Risk Indicator.")
        kri_volatility = st.slider("KRI Volatility", min_value=1.0, max_value=20.0, value=5.0, step=0.5, help="Variability of the Key Risk Indicator.")

        # Trigger data generation
        df_ops, df_losses = generate_synthetic_data(
            sim_start_date, sim_end_date,
            {'growth_rate': growth_rate},
            {'mean': loss_freq_mean, 'std': loss_freq_std},
            {'mean': loss_sev_mean, 'std': loss_sev_std},
            {'baseline': kri_baseline, 'volatility': kri_volatility}
        )

    st.subheader("Simulated Business Operations Data")
    st.write("This table shows the generated time-series data for business volume, revenue, and KRI.")
    st.dataframe(df_ops.head())

    st.subheader("Simulated Loss Events Data")
    st.write("This table displays the individual simulated operational loss events.")
    st.dataframe(df_losses.head())
    ```

**4.3. Risk Appetite Parameter Definition**
*   **Purpose:** Allow users to set explicit, quantitative risk tolerances that guide the simulated risk framework.
*   **Integration:** These parameters will be directly collected from Streamlit input widgets in the sidebar. The `ipywidgets` code is replaced by native Streamlit widgets.
*   **Inputs (from Streamlit UI):**
    *   `max_expected_loss_input` (Float from `st.slider`/`st.number_input`)
    *   `max_unexpected_loss_input` (Float from `st.slider`/`st.number_input`)
    *   `max_severe_loss_events_input` (Integer from `st.slider`/`st.number_input`)
    *   `kri_limit_input` (Float from `st.slider`/`st.number_input`)
    *   `risk_capacity_input` (Float from `st.slider`/`st.number_input`)
*   **Code (incorporating Streamlit inputs):**
    ```python
    # Streamlit UI for risk appetite parameters (in sidebar)
    with st.sidebar:
        st.subheader("2. Define Risk Appetite")
        max_expected_loss_input = st.slider("Max Expected Loss ($EL$)", min_value=0, max_value=5000, value=1300, step=10, help="Maximum average loss an organization expects to incur.")
        max_unexpected_loss_input = st.slider("Max Unexpected Loss ($UL$)", min_value=0, max_value=1000, value=380, step=10, help="Potential for losses exceeding expected loss (e.g., VaR at 99% confidence).")
        max_severe_loss_events_input = st.slider("Max Severe Loss Events", min_value=0, max_value=20, value=5, step=1, help="Tolerance for the number of 'severe' operational loss events.")
        kri_limit_input = st.slider("KRI Limit", min_value=0.0, max_value=100.0, value=55.0, step=0.5, help="Threshold for the Key Risk Indicator.")
        risk_capacity_input = st.slider("Risk Capacity", min_value=0, max_value=100000, value=50000, step=1000, help="Total capital buffer available for losses.")

    # Consolidate user parameters into a dictionary for downstream functions
    user_risk_appetite_params = {
        'MaxExpectedLoss_Threshold': float(max_expected_loss_input),
        'MaxUnexpectedLoss_Threshold': float(max_unexpected_loss_input),
        'MaxSevereLossEvents_Threshold': int(max_severe_loss_events_input),
        'KRI_Limit': float(kri_limit_input),
        'RiskCapacity': float(risk_capacity_input)
    }
    ```

**4.4. Risk Profile Calculation**
*   **Purpose:** Quantify the organization's risk exposure by calculating key metrics like Expected Loss ($EL$) and Unexpected Loss ($UL$) from the simulated data.
*   **Mathematical Formulas:**
    *   Expected Loss ($EL$): This is the average loss the organization can expect to incur over time. If $L_i$ is the $i$-th loss amount, and there are $n$ losses, then:
        $$EL = \frac{1}{n} \sum_{i=1}^{n} L_i$$
    *   Unexpected Loss ($UL$): This represents the potential for losses to deviate from the expected average, typically quantified using the standard deviation of loss amounts.
        $$UL = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (L_i - EL)^2}$$
*   **Integration:** This function will be called after data generation and risk appetite parameters are set. It can be cached if its inputs are cached.
*   **Inputs:**
    *   `df_simulated_operations` (from `generate_synthetic_data`)
    *   `df_loss_events` (from `generate_synthetic_data`)
    *   `user_parameters` (dictionary containing `KRI_Limit` from user inputs)
*   **Output:** `df_risk_profile` (Pandas DataFrame).
*   **Code:**
    ```python
    @st.cache_data(show_spinner=False)
    def calculate_risk_profile(df_simulated_operations, df_loss_events, user_parameters):
        """Computes the organization's simulated risk profile over time."""
        if df_simulated_operations.empty and df_loss_events.empty:
            return pd.DataFrame()

        try:
            df_simulated_operations['Date'] = pd.to_datetime(df_simulated_operations['Date'])
            if not df_loss_events.empty:
                df_loss_events['Date'] = pd.to_datetime(df_loss_events['Date'])
        except Exception as e:
            st.error(f"Error converting dates: {e}")
            raise e

        # Create a copy for the risk profile to avoid modifying original df_simulated_operations
        df_risk_profile = df_simulated_operations.copy()

        # Calculate Expected Loss (EL)
        # EL is constant over the period for this simulation, based on overall mean loss
        df_risk_profile['ExpectedLoss'] = df_loss_events['LossAmount'].mean() if not df_loss_events.empty else 0

        # Calculate Unexpected Loss (UL) - Simple example: standard deviation
        # UL is constant over the period for this simulation, based on overall std dev of loss
        df_risk_profile['UnexpectedLoss'] = df_loss_events['LossAmount'].std() if not df_loss_events.empty else 0

        # Incorporate KRI values (flag if KRI exceeds limit)
        if 'KRI' in df_risk_profile.columns and 'KRI_Limit' in user_parameters:
            df_risk_profile.loc[:, 'KRI_Exceeded'] = df_risk_profile['KRI'] > user_parameters['KRI_Limit']

        return df_risk_profile

    # Call the function with actual parameters
    df_risk_profile = calculate_risk_profile(df_ops, df_losses, user_risk_appetite_params)

    st.subheader("Calculated Risk Profile")
    st.write("This table shows the daily Expected Loss ($EL$), Unexpected Loss ($UL$), and KRI status calculated from the simulated data.")
    st.dataframe(df_risk_profile.head())
    ```

**4.5. Risk Appetite Monitoring and Breach Identification**
*   **Purpose:** Compare the calculated risk profile against the defined risk appetite thresholds to identify and monitor breaches and KRI performance.
*   **Integration:** This function will be called after `calculate_risk_profile`. The results (`df_breaches`, `df_kri_status`) will be displayed in tables and used to annotate plots.
*   **Inputs:**
    *   `df_risk_profile` (from `calculate_risk_profile`)
    *   `risk_appetite_params` (dictionary from user inputs)
*   **Outputs:** `df_breaches` (Pandas DataFrame), `df_kri_status` (Pandas DataFrame).
*   **Code:**
    ```python
    @st.cache_data(show_spinner=False)
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

        # Ensure 'Date' column is present for merging later
        if 'Date' not in df_risk_profile.columns:
            st.warning("Date column not found in df_risk_profile. Breach monitoring might be inaccurate.")
            return pd.DataFrame(), pd.DataFrame() # Return empty if essential column is missing

        for index, row in df_risk_profile.iterrows():
            breaches = {'Date': row['Date']}
            kri_status = {'Date': row['Date']}

            # Expected Loss breach
            if 'ExpectedLoss' in df_risk_profile.columns and 'MaxExpectedLoss_Threshold' in risk_appetite_params:
                if row['ExpectedLoss'] > risk_appetite_params['MaxExpectedLoss_Threshold']:
                    breaches['ExpectedLoss_Status'] = 'Breached'
                else:
                    breaches['ExpectedLoss_Status'] = 'Within Appetite'

            # Unexpected Loss breach
            if 'UnexpectedLoss' in df_risk_profile.columns and 'MaxUnexpectedLoss_Threshold' in risk_appetite_params:
                if row['UnexpectedLoss'] > risk_appetite_params['MaxUnexpectedLoss_Threshold']:
                    breaches['UnexpectedLoss_Status'] = 'Breached'
                else:
                    breaches['UnexpectedLoss_Status'] = 'Within Appetite'

            # KRI Status
            if 'KRI' in df_risk_profile.columns and 'KRI_Limit' in risk_appetite_params:
                if row['KRI'] > risk_appetite_params['KRI_Limit']:
                    kri_status['KRI_Status'] = 'Above Limit'
                else:
                    kri_status['KRI_Status'] = 'Within Limit'
            else:
                kri_status['KRI_Status'] = 'N/A' # Handle cases where KRI or KRI_Limit might be missing

            breach_data.append(breaches)
            kri_status_data.append(kri_status)

        df_breaches = pd.DataFrame(breach_data)
        df_kri_status = pd.DataFrame(kri_status_data)

        return df_breaches, df_kri_status

    # Call the function
    df_breaches, df_kri_status = monitor_risk_appetite(df_risk_profile, user_risk_appetite_params)

    st.subheader("Risk Appetite Monitoring")
    st.write("These tables show whether Expected Loss, Unexpected Loss, and the KRI are within the defined appetite.")

    st.markdown("**Breach Status:**")
    st.dataframe(df_breaches.head())

    st.markdown("**KRI Status:**")
    st.dataframe(df_kri_status.head())
    ```

**4.6. Visualization Implementation (using Altair)**
*   **Purpose:** Provide interactive and clear visual representations of the simulated data, risk profile, and breach status.
*   **Integration:** Altair charts will be used.
*   **Example Charts:**
    *   **Operational Metrics Trend:** Line chart of `BusinessVolume`, `Revenue`, `KRI` from `df_ops`.
    *   **Loss Event Distribution:** Histogram of `LossAmount` from `df_losses`.
    *   **Risk Profile Trend with Appetite:** Line charts of `ExpectedLoss` and `UnexpectedLoss` from `df_risk_profile`, with reference lines for `MaxExpectedLoss_Threshold` and `MaxUnexpectedLoss_Threshold`.
    *   **KRI Trend with Limit:** Line chart of `KRI` from `df_risk_profile` with a reference line for `KRI_Limit` and potential highlighting for breaches.
*   **Code Snippets for Visualizations:**
    ```python
    # Ensure df_ops 'Date' column is datetime for Altair
    df_ops['Date'] = pd.to_datetime(df_ops['Date'])

    st.subheader("Operational Metrics Over Time")
    st.write("Visualizing the trend of business volume, revenue, and the Key Risk Indicator.")

    # Business Volume and Revenue Trend
    chart_ops = alt.Chart(df_ops).transform_fold(
        ['BusinessVolume', 'Revenue'],
        as_=['Metric', 'Value']
    ).mark_line().encode(
        x=alt.X('Date:T', title='Date'),
        y=alt.Y('Value:Q', title='Amount'),
        color=alt.Color('Metric:N', title='Metric', scale=alt.Scale(range=['#1f77b4', '#ff7f0e'])) # Color-blind friendly
    ).properties(
        title='Simulated Business Volume and Revenue Over Time'
    ).interactive()
    st.altair_chart(chart_ops, use_container_width=True)

    # KRI Trend
    chart_kri = alt.Chart(df_ops).mark_line(color='#2ca02c').encode(
        x=alt.X('Date:T', title='Date'),
        y=alt.Y('KRI:Q', title='KRI Value')
    ).properties(
        title='Key Risk Indicator (KRI) Over Time'
    )

    # Add KRI Limit line
    kri_limit_line = alt.Chart(pd.DataFrame({'KRI_Limit': [user_risk_appetite_params['KRI_Limit']]} )).mark_rule(color='#d62728', strokeDash=[5,5]).encode(
        y='KRI_Limit'
    )
    st.altair_chart(chart_kri + kri_limit_line, use_container_width=True)

    st.subheader("Operational Loss Event Distribution")
    st.write("Histogram showing the distribution of simulated loss amounts.")
    if not df_losses.empty:
        chart_loss_hist = alt.Chart(df_losses).mark_bar(bin=True, color='#9467bd').encode(
            x=alt.X('LossAmount:Q', bin=alt.Bin(maxbins=30), title='Loss Amount ($)'),
            y=alt.Y('count()', title='Number of Losses'),
            tooltip=['count()']
        ).properties(
            title='Distribution of Simulated Loss Amounts'
        )
        st.altair_chart(chart_loss_hist, use_container_width=True)
    else:
        st.info("No loss events simulated based on current parameters.")

    st.subheader("Risk Profile vs. Risk Appetite")
    st.write("Comparing calculated Expected Loss ($EL$) and Unexpected Loss ($UL$) against defined thresholds.")

    # EL and UL Trend with Thresholds
    if not df_risk_profile.empty:
        df_risk_profile_melted = df_risk_profile.melt(id_vars=['Date'], value_vars=['ExpectedLoss', 'UnexpectedLoss'], var_name='RiskMetric', value_name='Value')

        # Add thresholds as separate data for plotting
        threshold_data = pd.DataFrame({
            'RiskMetric': ['ExpectedLoss', 'UnexpectedLoss'],
            'Threshold': [user_risk_appetite_params['MaxExpectedLoss_Threshold'], user_risk_appetite_params['MaxUnexpectedLoss_Threshold']]
        })

        chart_risk_profile = alt.Chart(df_risk_profile_melted).mark_line().encode(
            x=alt.X('Date:T', title='Date'),
            y=alt.Y('Value:Q', title='Loss Amount ($)'),
            color=alt.Color('RiskMetric:N', title='Risk Metric', scale=alt.Scale(range=['#17becf', '#e377c2']))
        ).properties(
            title='Expected and Unexpected Loss Over Time'
        )

        # Add threshold lines
        threshold_lines = alt.Chart(threshold_data).mark_rule(strokeDash=[3, 3]).encode(
            y='Threshold:Q',
            color=alt.Color('RiskMetric:N', title='Threshold For', scale=alt.Scale(range=['#17becf', '#e377c2'])),
            tooltip=[alt.Tooltip('Threshold:Q', title='Threshold')]
        )
        st.altair_chart(chart_risk_profile + threshold_lines, use_container_width=True)
    else:
        st.info("Risk profile could not be calculated. Please check data generation parameters.")

    # Combine df_risk_profile and df_breaches for a single KRI status plot if desired
    if not df_risk_profile.empty and not df_kri_status.empty:
        df_combined_kri = df_risk_profile.merge(df_kri_status, on='Date', how='left')

        kri_chart = alt.Chart(df_combined_kri).mark_line().encode(
            x=alt.X('Date:T', title='Date'),
            y=alt.Y('KRI:Q', title='KRI Value'),
            color=alt.Color('KRI_Status:N', title='KRI Status',
                            scale=alt.Scale(domain=['Within Limit', 'Above Limit'], range=['#2ca02c', '#d62728']))
        ).properties(
            title='KRI Performance Against Limit'
        )

        kri_limit_rule = alt.Chart(pd.DataFrame({'limit': [user_risk_appetite_params['KRI_Limit']]} )).mark_rule(strokeDash=[5,5], color='#d62728').encode(
            y=alt.Y('limit', title='KRI Limit')
        )
        st.altair_chart(kri_chart + kri_limit_rule, use_container_width=True)
    ```

**4.7. References**
*   **Purpose:** Credit external datasets and libraries and provide academic context.
*   **Integration:** Displayed as a static markdown section at the end of the application.
*   **Code:**
    ```python
    st.subheader("References")
    st.markdown("""
    [1] Chapter 3: The Risk Management Framework, Chapter 5: Risk Information, Operational Risk Manager Handbook, [Provided Document]. These sections discuss risk capacity, risk appetite, risk profile, and key risk indicators.  
    [2] dalmirPereira/module6_labWork: Lab Exercises from Module 6 - GitHub, https://github.com/dalmirPereira/module6_labWork.  
    """)
    ```

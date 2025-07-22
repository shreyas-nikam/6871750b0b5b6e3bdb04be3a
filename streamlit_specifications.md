
# Streamlit Application Requirements Specification

## 1. Application Overview

The **Risk Appetite Framework Explorer** Streamlit application aims to simulate elements of an operational risk appetite framework. Its primary purpose is to allow users to define various risk tolerance levels and immediately observe their implications on a simulated organization's risk profile and capital management. This interactive tool will provide a dynamic way to understand abstract risk concepts.

**Key Objectives:**
*   Enable users to understand the core insights within operational risk management.
*   Educate users on the components of an operational risk appetite framework.
*   Facilitate exploration of the relationship between risk appetite, risk capacity, and actual risk outcomes through simulation.
*   Demonstrate the practical application of Key Risk Indicators (KRIs) in monitoring risk against appetite thresholds.
*   Emphasize the critical importance of aligning risk appetite with business strategy and capital allocation.

**Core Features:**
*   **Synthetic Data Generation**: Generate simulated time-series data for business operations (revenue, expenses, profit), operational loss events, and Key Risk Indicators (KRIs).
*   **Risk Appetite Definition**: Provide interactive controls for users to set quantitative risk appetite statements.
*   **Risk Profile Visualization**: Display the simulated 'Risk Capacity' and the evolving 'Risk Profile' of the organization over time, benchmarked against defined risk appetite thresholds.
*   **Breach Monitoring**: Track and visualize instances where the simulated risk profile exceeds the defined risk appetite, presenting these as trend plots.
*   **KRI Dashboard**: Present a dynamic dashboard of simulated KRIs, highlighting their status relative to pre-set thresholds and indicating potential challenges to the defined risk appetite.

## 2. User Interface Requirements

The application will feature a clear and intuitive layout, prioritizing user interaction and data visualization.

**Layout and Navigation Structure:**
*   **Sidebar (`st.sidebar`):** All input widgets and controls will be located in a collapsible sidebar for easy access and configuration. This allows the main content area to be dedicated to visualizations and explanatory text.
*   **Main Content Area:** This area will display:
    *   An introductory overview.
    *   Sections for displaying generated data (e.g., `st.dataframe` for raw samples).
    *   Interactive plots and charts illustrating business performance, operational losses, KRI trends, risk profile, and appetite breaches.
    *   Explanatory text for each section and visualization.

**Input Widgets and Controls:**
Users will interact with the application primarily through sliders, number inputs, and date pickers in the sidebar. Each input will have clear labels and inline help text.

*   **Simulation Date Range:**
    *   `start_date` (Date Input): Start date for data generation.
    *   `end_date` (Date Input): End date for data generation.
*   **Synthetic Business Data Parameters:**
    *   `avg_revenue` (Number Input/Slider): Average daily revenue (e.g., `$10000$`).
    *   `revenue_volatility` (Number Input/Slider): Volatility factor for revenue (e.g., `$0.1$`, representing $10\%$).
    *   `baseline_expenses` (Number Input/Slider): Baseline daily expenses (e.g., `$6000$`).
*   **Operational Loss Simulation Parameters:**
    *   `avg_daily_losses` (Number Input/Slider): Average number of loss events per day (e.g., `$0.5$`).
    *   `severity_mu` (Number Input/Slider): Mean ($\mu$) parameter for the log-normal severity distribution (e.g., `$5$`).
    *   `severity_sigma` (Number Input/Slider): Standard deviation ($\sigma$) parameter for the log-normal severity distribution (e.g., `$2$`).
    *   `severe_loss_threshold` (Number Input/Slider): Monetary threshold above which a loss is considered "severe" (e.g., `$1000$`).
*   **Key Risk Indicator (KRI) Generation Parameters:**
    *   `num_kris` (Number Input): Number of KRIs to generate (e.g., `$2$`). Dynamic creation of KRI specific inputs based on this.
    *   For each KRI (e.g., KRI 1, KRI 2):
        *   `kri_baseline_X` (Number Input/Slider): Baseline value for KRI X.
        *   `kri_volatility_X` (Number Input/Slider): Volatility factor for KRI X.
*   **Risk Appetite Definition Parameters:** These will be crucial for the application's core functionality.
    *   `max_expected_loss_threshold` (Number Input/Slider): Maximum acceptable Expected Loss ($EL$) over the simulation period (e.g., `$50000$`).
    *   `max_unexpected_loss_threshold` (Number Input/Slider): Maximum acceptable Unexpected Loss ($UL$) (e.g., `$150000$`).
    *   `severe_loss_event_tolerance` (Number Input/Slider): Maximum acceptable number of 'severe' operational loss events (e.g., `$5$`).
    *   For each KRI (e.g., KRI 1, KRI 2, assuming a configurable number up to `num_kris`):
        *   `kri_limit_X` (Number Input/Slider): Upper or lower limit for KRI X.

**Visualization Components:**
*   **Time-based Trend Plots:**
    *   Line/Area charts for simulated daily Revenue, Expenses, and Profit.
    *   Line charts for individual KRI trends over time, with appetite thresholds clearly marked.
    *   Area chart for total daily/aggregated operational losses.
*   **Relationship Plots:**
    *   Scatter plots (e.g., Profit vs. Total Daily Loss) to examine correlations.
    *   Histogram of operational loss amounts to show severity distribution.
*   **Aggregated Comparison/Dashboards:**
    *   Bar chart showing the count of severe versus non-severe loss events.
    *   Summary tables for aggregated financial metrics (total revenue, total profit, total losses).
    *   KRI Dashboard: A table or series of gauge/status indicators showing current KRI values and their status (e.g., "Within Appetite," "Near Limit," "Breached") against defined thresholds.
*   **Risk Profile vs. Appetite Visualization:**
    *   A composite plot illustrating the simulated aggregated risk profile (e.g., total losses or a risk score derived from KRIs) against the defined risk appetite thresholds (e.g., $EL$, $UL$). Breaches should be visually highlighted.

**Style and Usability:**
*   **Color Palette:** Adopt a color-blind-friendly palette.
*   **Font Size:** Ensure all text, labels, and plot elements have a font size $\ge 12$ pt for readability.
*   **Titles and Labels:** Supply clear and concise titles for all plots and sections, along with properly labeled axes and legends.
*   **Interactivity:** Enable interactive features for plots (e.g., zoom, pan, tooltips) where the environment supports it (e.g., using Plotly or Altair).
*   **Static Fallback:** While Streamlit natively supports interactive plots, ensure visualizations built with Matplotlib/Seaborn also meet the style requirements for clarity.

**Interactive Elements and Feedback Mechanisms:**
*   All input widgets will trigger re-execution and updates of the application's calculations and visualizations in real-time.
*   Inline help text or tooltips (`help` argument in Streamlit widgets) will be provided for all interactive controls to describe their function and impact.
*   Error messages (e.g., if start date is after end date) will be displayed clearly to the user.

## 3. Additional Requirements

*   **Real-time Updates and Responsiveness:** The application should be highly responsive, with all calculations and visualizations updating dynamically as users interact with input widgets. This is inherent to Streamlit's design.
*   **Annotation and Tooltip Specifications:**
    *   For plots, tooltips should display relevant data points on hover (e.g., date, value, loss amount, KRI status).
    *   Explanatory text will be provided near each visualization to interpret the results and link them back to risk appetite concepts.
    *   Each input control in the sidebar will have a concise tooltip or help text explaining its purpose and range.

## 4. Notebook Content and Code Requirements

This section outlines the specific Python functions from the Jupyter notebook that will be integrated into the Streamlit application, along with their expected usage.

**4.1. Synthetic Business Data Generation**
*   **Purpose:** Generates a time series of daily revenue, expenses, and profit to simulate the operational environment.
*   **Code:**
    ```python
    import pandas as pd
    import numpy as np
    from datetime import timedelta

    def generate_business_data(start_date, end_date, avg_revenue, revenue_volatility, baseline_expenses):
        """Generates business data time series."""
        if start_date > end_date:
            return None

        dates = [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]
        num_days = len(dates)

        revenue = np.random.normal(avg_revenue, avg_revenue * revenue_volatility, num_days)
        revenue = np.maximum(revenue, 0)  # Ensure revenue is not negative
        expenses = np.full(num_days, baseline_expenses)
        profit = revenue - expenses

        df = pd.DataFrame({'Revenue': revenue, 'Expenses': expenses, 'Profit': profit}, index=dates)
        return df
    ```
*   **Streamlit Integration:**
    *   `start_date`, `end_date` will come from `st.date_input`.
    *   `avg_revenue`, `revenue_volatility`, `baseline_expenses` will come from `st.number_input` or `st.slider` widgets in the sidebar.
    *   The returned `business_df` will be used for displaying raw data (`st.dataframe`) and for plotting time series of `Revenue`, `Expenses`, and `Profit` using a line chart.

**4.2. Simulate Operational Losses**
*   **Purpose:** Simulates daily operational losses using a frequency-severity approach, essential for understanding potential financial impacts.
*   **Code:**
    ```python
    import pandas as pd
    import numpy as np

    def simulate_operational_losses(start_date, end_date, avg_daily_losses, severity_params, severe_loss_threshold):
        """Simulates operational loss events using a frequency-severity approach."""

        # Validate inputs
        if pd.to_datetime(start_date) > pd.to_datetime(end_date):
            raise ValueError("Start date must be before end date.")

        if not isinstance(avg_daily_losses, (int, float)):
            raise TypeError("Average daily losses must be a number.")

        if not isinstance(severe_loss_threshold, (int, float)):
            raise TypeError("Severe loss threshold must be a number.")

        # Generate date range
        date_range = pd.date_range(start=start_date, end=end_date)

        # Simulate losses for each day
        all_losses = []
        for date in date_range:
            # Simulate number of loss events for the day
            num_losses = np.random.poisson(avg_daily_losses)

            # Simulate loss amounts for each event
            if num_losses > 0:
                loss_amounts = np.random.lognormal(mean=severity_params['mu'], sigma=severity_params['sigma'], size=num_losses)
                # Create a DataFrame for the day's losses
                day_losses = pd.DataFrame({'Date': [date] * num_losses, 'Loss_Amount': loss_amounts})
                all_losses.append(day_losses)

        # Concatenate all daily losses into a single DataFrame
        if all_losses:
            losses_df = pd.concat(all_losses, ignore_index=True)
        else:
            return pd.DataFrame({'Date': [], 'Loss_Amount': [], 'Is_Severe': []}) # Return empty DataFrame with columns

        # Identify severe loss events
        losses_df['Is_Severe'] = losses_df['Loss_Amount'] > severe_loss_threshold

        return losses_df
    ```
*   **Streamlit Integration:**
    *   `start_date`, `end_date` will come from `st.date_input`.
    *   `avg_daily_losses`, `severe_loss_threshold` will come from `st.number_input` or `st.slider`.
    *   `severity_params` dictionary will be constructed from two `st.number_input` or `st.slider` widgets for `mu` ($\mu$) and `sigma` ($\sigma$).
    *   The returned `losses_df` will be used for displaying raw data (`st.dataframe`), for plotting a histogram of `Loss_Amount`, and a bar chart of `Is_Severe` counts. It will also be used to calculate total losses over time for trend plots and to monitor breaches against appetite thresholds.

**4.3. Generate Key Risk Indicators (KRI) Data**
*   **Purpose:** Creates time-series data for multiple KRIs to provide early signals of increasing risk exposures.
*   **Code:**
    ```python
    import pandas as pd
    import numpy as np

    def generate_kri_data(start_date, end_date, num_kris, baseline_values, volatility_factors, link_to_losses):
        """Generates time-series data for multiple KRIs."""

        date_range = pd.date_range(start=start_date, end=end_date)
        df = pd.DataFrame({'Date': date_range})

        for i in range(num_kris):
            kri_name = f'KRI_{i+1}'
            
            baseline = baseline_values[i] if i < len(baseline_values) else 100
            volatility = volatility_factors[i] if i < len(volatility_factors) else 0.05
            
            kri_values = [baseline]
            for _ in range(len(date_range) - 1):
                change = np.random.normal(0, volatility * baseline)
                new_value = kri_values[-1] + change
                kri_values.append(new_value)

            df[kri_name] = kri_values

        return df
    ```
*   **Streamlit Integration:**
    *   `start_date`, `end_date` will come from `st.date_input`.
    *   `num_kris` will come from `st.number_input`. Loop through `num_kris` to create corresponding `st.number_input` or `st.slider` widgets for `baseline_values` and `volatility_factors` for each KRI.
    *   `link_to_losses` is not used in the current notebook example but can be omitted or set to `None`.
    *   The returned `kri_df` will be used for displaying raw data (`st.dataframe`) and for plotting individual KRI trends with line charts. This data will also form the basis of the KRI dashboard, comparing KRI values against user-defined limits.

**4.4. Combine Synthetic Data**
*   **Purpose:** Merges the generated business, operational loss, and KRI data into a single DataFrame for comprehensive analysis.
*   **Code:**
    ```python
    import pandas as pd

    def combine_synthetic_data(business_df, losses_df, kri_df):
        """Merges all generated data into a single DataFrame."""
        # Align dates and merge on index or 'Date' column if present and consistent
        # For simplicity based on notebook, assuming concatenation; for robust merging, actual merge logic is better
        # Let's refine for a more proper merge if dates are aligned
        # Assuming Date is the index for business_df, and 'Date' column for losses_df and kri_df
        
        # Ensure 'Date' column for losses_df and kri_df is datetime and set as index
        if not losses_df.empty:
            losses_df['Date'] = pd.to_datetime(losses_df['Date'])
            losses_df = losses_df.set_index('Date')
            
        kri_df['Date'] = pd.to_datetime(kri_df['Date'])
        kri_df = kri_df.set_index('Date')

        combined_df = business_df.join(losses_df.groupby(level=0).sum(numeric_only=True), how='outer', rsuffix='_losses')
        combined_df = combined_df.join(kri_df, how='outer', rsuffix='_kri')

        # Add daily severe loss count
        if not losses_df.empty:
            severe_losses_daily = losses_df[losses_df['Is_Severe']].groupby(level=0)['Loss_Amount'].count().rename('Severe_Loss_Count')
            combined_df = combined_df.join(severe_losses_daily, how='left')
        
        combined_df.fillna(0, inplace=True) # Fill NaNs where data types might not align daily
        combined_df.index.name = 'Date'
        combined_df = combined_df.reset_index() # Convert index back to column for plotting flexibility
        return combined_df
    ```
*   **Streamlit Integration:**
    *   Call this function after `generate_business_data`, `simulate_operational_losses`, and `generate_kri_data` have produced their respective DataFrames.
    *   The returned `combined_df` will be the primary DataFrame for most advanced analyses and visualizations within the application, allowing for correlation analysis and integrated risk monitoring.

**4.5. Risk Appetite Logic and Visualization (Translation from `ipywidgets` and concepts)**
*   **Purpose:** To define, display, and monitor risk appetite thresholds, comparing them against simulated outcomes. The original `display_risk_appetite_inputs` from the notebook was `ipywidgets` specific, but the *concept* of interactive risk appetite definition is critical.
*   **Streamlit Integration:**
    *   **Input Definition:** Use `st.slider` or `st.number_input` in the sidebar for `max_expected_loss_threshold`, `max_unexpected_loss_threshold`, `severe_loss_event_tolerance`, and individual `kri_limit_X` values as described in Section 2.
    *   **Calculation of Actuals:**
        *   Calculate the total Expected Loss ($EL$) from simulated `Loss_Amount` over the period.
        *   Calculate the total Unexpected Loss ($UL$) from simulated `Loss_Amount` (e.g., as a high percentile like $95^{th}$ or $99^{th}$ VaR of aggregated losses, or using the formula from the reference document related to $PD_A$). For this application, a simplified $UL$ could be the total losses minus the average total losses, or a high percentile of the daily/aggregated loss distribution.
        *   Count the number of `Is_Severe` events.
    *   **Formulas from Reference Document [1]:**
        *   Expected Loss ($EL$) and Unexpected Loss ($UL$) are fundamental concepts. The document mentions:
            $$EL = PD_A L$$
            where $PD_A$ is the default probability associated with the A rating, and $L$ is the insured limit.
            $$UL = 3 \sigma$$
            $$UL = 3 PD_A (1 - PD_A)L$$
            These formulas would be explained in the application's narrative and potentially used to derive a 'Risk Capacity' value based on capital, which is then compared to appetite. For this simulation, we will primarily compare *actual simulated total losses* against the *user-defined $EL$ and $UL$ thresholds*.
        *   The aggregate risk ($S_{net}$) after insurance mitigation:
            $$S_{net} = \sum_{i=1}^{N}X_i - \sum_{i=1}^{N}L_{d,c}(X_i)$$
            where $X_i$ is a random draw of $X$ (loss event), and $L_{d,c}$ is the operator for payout:
            $$L_{d,c}(X_i) = \min(\max(X_i - d, 0), c)$$
            Here, $d$ is the deductible and $c$ is the cover per loss event. While the core simulation doesn't *implement* insurance, the application should *explain* these concepts as part of the overall risk appetite framework, drawing from the provided document.
    *   **Breach Monitoring:**
        *   Logic will compare calculated total $EL$, $UL$, `Severe_Loss_Count`, and daily KRI values against the user-defined `max_expected_loss_threshold`, `max_unexpected_loss_threshold`, `severe_loss_event_tolerance`, and `kri_limit_X` respectively.
        *   Visualizations (e.g., trend plots for total losses over time, KRI trends) will include horizontal lines representing the appetite thresholds, with color changes or markers indicating breaches.
        *   A summary section will list current status (e.g., "Expected Loss: Within Appetite," "KRI_1: Breached").


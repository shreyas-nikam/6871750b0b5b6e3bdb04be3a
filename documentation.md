id: 6871750b0b5b6e3bdb04be3a_documentation
summary: Module 6 Lab 1 Documentation
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# Building a Risk Appetite Framework Application with Streamlit

## Introduction to the Risk Appetite Framework Application
Duration: 0:08:00

In this codelab, you will learn how to build and understand a Streamlit application that simulates and visualizes a **Risk Appetite Framework (RAF)**. This application is a powerful tool for financial institutions and businesses to define, monitor, and manage their operational risk exposure.

Operational risk management is crucial for an organization's stability and success. The Risk Appetite Framework provides a structured approach to articulate the level of risk an organization is willing to accept in pursuit of its strategic objectives.

<aside class="positive">
Understanding and implementing a robust RAF is a best practice in modern risk management, enabling proactive decision-making and better resource allocation.
</aside>

**Key Concepts Explored in this Application:**

*   **Risk Capacity:** The maximum level of risk an organization can absorb without jeopardizing its solvency or ability to meet its objectives. It's often determined by financial resources, regulatory capital, or liquidity.
*   **Risk Appetite:** The aggregate level and types of risk an organization is willing to assume to achieve its strategic objectives. It reflects the organization's risk culture and strategic priorities.
*   **Risk Profile:** The current view of the organization's risks at any given time, reflecting its actual risk exposure compared to its desired risk appetite.
*   **Expected Loss ($EL$):** The average loss an organization expects to incur over a given period, often calculated as the sum of individual losses divided by the number of events.
    $$EL = \frac{1}{n} \sum_{i=1}^{n} L_i$$
    Where $L_i$ represents an individual loss amount and $n$ is the total number of loss events.
*   **Unexpected Loss ($UL$):** The potential for actual losses to exceed the expected loss. It quantifies the volatility or dispersion of losses and is often represented by a statistical measure like the standard deviation of losses or Value at Risk (VaR).
    $$UL = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (L_i - EL)^2}$$
    Where $L_i$ is an individual loss amount, $EL$ is the Expected Loss, and $n$ is the number of loss events.
*   **Key Risk Indicators (KRIs):** Metrics that provide insights into an organization's risk exposure. They are used to monitor and track specific risks, often providing early warnings of potential issues.

This application provides a dynamic environment to:

1.  **Simulate Data:** Generate synthetic time-series data for business operations, financial performance, and simulated operational loss events.
2.  **Define Risk Appetite:** Enable users to set quantitative risk appetite statements (e.g., maximum acceptable Expected Loss, Unexpected Loss, KRI limits).
3.  **Visualize Risk Profile & Capacity:** Display the simulated 'Risk Capacity' and evolving 'Risk Profile' over time, comparing them against defined risk appetite thresholds.
4.  **Monitor Breaches:** Track and visualize instances where the simulated risk profile exceeds the defined risk appetite.
5.  **KRI Dashboard:** Present a dashboard of simulated Key Risk Indicators (KRIs) and their status relative to pre-set thresholds.

By the end of this codelab, you will have a clear understanding of the application's architecture, its core functionalities, and how it helps in visualizing and managing operational risk within the framework of risk appetite.

## Application Architecture and Workflow
Duration: 0:10:00

The Streamlit application is structured into three main components: `app.py` (the main entry point) and two sub-modules within the `application_pages` directory (`page1.py` and `page2.py`, with a `page3.py` for references). This modular design enhances readability, maintainability, and scalability.

### Overall Structure

```
├── app.py
└── application_pages/
    ├── __init__.py
    ├── page1.py
    ├── page2.py
    └── page3.py
```

### Data Flow and Interaction

The core of the application's interaction involves generating synthetic data on `page1.py` and then using that data for risk profile calculations and monitoring on `page2.py`. This cross-page data sharing is achieved using Streamlit's `st.session_state`.

Here's a simplified architectural diagram illustrating the application's flow:

```mermaid
graph TD
    A[User Interaction] --> B(app.py - Main Navigation)
    B -- Select Page --> C{Data Generation & Visualization (page1.py)}
    B -- Select Page --> D{Risk Profile & Monitoring (page2.py)}
    B -- Select Page --> E{References (page3.py)}

    C -- Generates synthetic data --> F[df_ops, df_losses DataFrames]
    F -- Stores in st.session_state --> G(Streamlit Session State)
    G -- Retrieves for calculations --> D

    D -- User defines Risk Appetite --> H[Risk Appetite Parameters]
    D -- Calculates Risk Profile --> I[df_risk_profile]
    D -- Monitors Breaches --> J[df_breaches, df_kri_status]
    D -- Visualizes Data --> K[Interactive Charts]

    E -- Displays Static References --> L[Reference Text]

    subgraph User Interface
        C
        D
        E
        K
        L
    end
    subgraph Backend Logic
        F
        G
        H
        I
        J
    end
```

**Explanation of Modules:**

*   **`app.py`**:
    *   Serves as the main entry point for the Streamlit application.
    *   Sets basic page configurations (title, layout).
    *   Displays the application title and a divider.
    *   Includes an introductory markdown explaining the RAF concepts and the application's purpose.
    *   Manages navigation using a `st.sidebar.selectbox` to switch between `page1.py`, `page2.py`, and `page3.py`.
    *   Dynamically imports and calls the `run_pageX()` function for the selected page.

*   **`application_pages/page1.py` (Data Generation & Visualization)**:
    *   Handles the generation of synthetic time-series data for business operations, revenue, operational loss events, and Key Risk Indicators (KRIs).
    *   Provides interactive Streamlit sliders in the sidebar for users to customize data generation parameters (e.g., growth rate, loss frequency/severity, KRI volatility).
    *   Uses the `@st.cache_data` decorator for the `generate_synthetic_data` function to optimize performance by caching the generated data, preventing re-computation on every minor parameter change.
    *   Displays the generated data in `st.dataframe` tables.
    *   Visualizes trends and distributions using `altair` charts (e.g., Business Volume & Revenue, KRI over time, Loss Amount Distribution).
    *   Crucially, it stores the generated `df_ops` and `df_losses` DataFrames in `st.session_state` so they can be accessed by `page2.py`.

*   **`application_pages/page2.py` (Risk Profile & Monitoring)**:
    *   Focuses on defining risk appetite thresholds and monitoring the simulated risk profile against them.
    *   Provides Streamlit sliders in the sidebar for users to input their desired risk appetite parameters (e.g., Max Expected Loss, Max Unexpected Loss, KRI Limit, Risk Capacity).
    *   Retrieves the simulated data (`df_ops`, `df_losses`) from `st.session_state`.
    *   Calculates the `ExpectedLoss` and `UnexpectedLoss` (simplified as mean and standard deviation of all simulated loss events) and determines the KRI status.
    *   Uses `@st.cache_data` for `calculate_risk_profile` and `monitor_risk_appetite` functions for performance.
    *   Compares the calculated risk profile components against the user-defined risk appetite thresholds to identify and report breaches.
    *   Displays the calculated risk profile and breach statuses in `st.dataframe` tables.
    *   Visualizes the risk profile and thresholds using `altair` charts, clearly showing when `EL`, `UL`, or `KRI` exceed their defined limits.

*   **`application_pages/page3.py` (References)**:
    *   A simple page that provides references and acknowledgments for the concepts and resources used in the application.

This modular structure, combined with `st.session_state` for data persistence, allows for a clear separation of concerns and a seamless user experience across different sections of the application.

## Setting Up Your Environment
Duration: 0:03:00

Before you can run the Streamlit application, you need to set up your Python environment and install the necessary libraries.

### 1. Create a Virtual Environment (Recommended)

It's a good practice to use a virtual environment to manage dependencies for your project, preventing conflicts with other Python projects.

```bash
python -m venv venv
```

### 2. Activate the Virtual Environment

*   **On Windows:**
    ```bash
    .\venv\Scripts\activate
    ```
*   **On macOS/Linux:**
    ```bash
    source venv/bin/activate
    ```

### 3. Install Required Libraries

Install Streamlit, Pandas, NumPy, and Altair using pip:

```bash
pip install streamlit pandas numpy altair
```

### 4. Organize Your Files

Make sure your `app.py` and the `application_pages` directory (containing `page1.py`, `page2.py`, and `page3.py`) are structured as shown in the "Application Architecture" section.

### 5. Run the Streamlit Application

Navigate to the directory containing `app.py` in your terminal and run the command:

```bash
streamlit run app.py
```

This command will open the application in your default web browser, usually at `http://localhost:8501`.

<aside class="positive">
Always ensure your virtual environment is activated before installing packages or running the application to keep your dependencies isolated and manageable.
</aside>

## Step 1: Data Generation and Visualization
Duration: 0:15:00

This step focuses on `application_pages/page1.py`, where synthetic data is generated and visualized. This data forms the foundation for calculating and monitoring the risk profile in the next step.

### Purpose of `page1.py`

The primary goal of `page1.py` is to create realistic, yet simulated, time-series data for various business metrics and operational loss events. This simulation allows users to experiment with different scenarios and observe their impact on risk metrics without needing real-world sensitive data.

### 1. Data Generation Parameters

The left sidebar in the Streamlit application, when on the "Data Generation & Visualization" page, provides sliders and date inputs to control the synthetic data generation.

```python
# From application_pages/page1.py
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
```

**Parameters Explained:**

*   **Simulation Dates:** Define the period for which data is generated.
*   **Growth Rate:** Simulates the growth of business volume over time.
*   **Loss Frequency (Poisson Distribution):** Determines how many loss events occur within a period. The Poisson distribution is often used for count data (number of events).
    *   `loss_freq_mean`: Average number of events.
*   **Loss Severity (Normal Distribution):** Determines the financial impact of each loss event.
    *   `loss_sev_mean`: Average loss amount per event.
    *   `loss_sev_std`: Variability of loss amounts.
*   **KRI Parameters:** Control the behavior of a Key Risk Indicator.
    *   `kri_baseline`: Average value of the KRI.
    *   `kri_volatility`: How much the KRI fluctuates around its baseline.

### 2. The `generate_synthetic_data` Function

This function is the core of the data generation process. It creates two primary DataFrames: `df_simulated_operations` (for business volume, revenue, and KRI) and `df_loss_events` (for individual loss occurrences).

```python
# From application_pages/page1.py
@st.cache_data(show_spinner=False)
def generate_synthetic_data(start_date, end_date, business_params, loss_freq_params, loss_sev_params, kpi_params):
    """Generates synthetic time-series data for the Streamlit app."""
    # ... (date validation) ...

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
        df_loss_events = pd.DataFrame(columns=['Date', 'LossAmount'])

    # Key Risk Indicator
    baseline = kpi_params.get('baseline', 50)
    volatility = kpi_params.get('volatility', 5)
    df_simulated_operations['KRI'] = np.random.normal(baseline, volatility, len(df_simulated_operations))

    return df_simulated_operations, df_loss_events
```

<aside class="positive">
The `@st.cache_data` decorator is crucial here. It tells Streamlit to cache the results of the `generate_synthetic_data` function. If the input parameters to this function don't change, Streamlit will serve the cached result instead of re-running the function, significantly improving performance and responsiveness.
</aside>

### 3. Displaying and Visualizing Data

After generating the data, `page1.py` displays the head of the DataFrames and then renders several interactive Altair charts.

```python
# From application_pages/page1.py
st.subheader("Simulated Business Operations Data")
st.dataframe(df_ops.head())

st.subheader("Simulated Loss Events Data")
st.dataframe(df_losses.head())

st.subheader("Operational Metrics Over Time")
# Business Volume and Revenue Trend
chart_ops = alt.Chart(df_ops).transform_fold(
    ['BusinessVolume', 'Revenue'],
    as_=['Metric', 'Value']
).mark_line().encode(
    x=alt.X('Date:T', title='Date'),
    y=alt.Y('Value:Q', title='Amount'),
    color=alt.Color('Metric:N', title='Metric', scale=alt.Scale(range=['#1f77b4', '#ff7f0e']))
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
st.altair_chart(chart_kri, use_container_width=True)

st.subheader("Operational Loss Event Distribution")
# Loss Amount Distribution
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
```

These visualizations provide immediate feedback on how parameter adjustments impact the simulated data, helping users understand the underlying distributions and trends.

### 4. Passing Data to Other Pages

Crucially, `page1.py` stores the generated `df_ops` and `df_losses` into Streamlit's `st.session_state`. This allows `page2.py` to access this data without re-running the generation process.

```python
# From application_pages/page1.py (within the sidebar context after generation)
# Trigger data generation
df_ops, df_losses = generate_synthetic_data(
    sim_start_date, sim_end_date,
    {'growth_rate': growth_rate},
    {'mean': loss_freq_mean, 'std': loss_freq_std},
    {'mean': loss_sev_mean, 'std': loss_sev_std},
    {'baseline': kri_baseline, 'volatility': kri_volatility}
)

# Store in session state for access by other pages
st.session_state['df_ops'] = df_ops
st.session_state['df_losses'] = df_losses
```

By completing this step, you've successfully generated a robust dataset that mimics real-world operational scenarios, ready to be used for risk appetite definition and monitoring.

## Step 2: Risk Profile and Monitoring
Duration: 0:18:00

This step delves into `application_pages/page2.py`, which is the core of the Risk Appetite Framework application. Here, users define their risk appetite, and the application calculates and monitors the simulated risk profile against these thresholds.

### Purpose of `page2.py`

`page2.py` takes the simulated data from `page1.py` and applies the concepts of Expected Loss ($EL$), Unexpected Loss ($UL$), and Key Risk Indicators (KRIs) to determine the organization's current risk profile. It then compares this profile against user-defined risk appetite limits to identify and visualize potential breaches.

### 1. Defining Risk Appetite Parameters

Similar to `page1.py`, `page2.py` presents a set of sliders in the sidebar, allowing users to define their organization's risk appetite thresholds.

```python
# From application_pages/page2.py
with st.sidebar:
    st.subheader("2. Define Risk Appetite")
    max_expected_loss_input = st.slider("Max Expected Loss ($EL$)", min_value=0, max_value=5000, value=1300, step=10, help="Maximum average loss an organization expects to incur.")
    max_unexpected_loss_input = st.slider("Max Unexpected Loss ($UL$)", min_value=0, max_value=1000, value=380, step=10, help="Potential for losses exceeding expected loss (e.g., VaR at 99% confidence).")
    max_severe_loss_events_input = st.slider("Max Severe Loss Events", min_value=0, max_value=20, value=5, step=1, help="Tolerance for the number of 'severe' operational loss events.")
    kri_limit_input = st.slider("KRI Limit", min_value=0.0, max_value=100.0, value=55.0, step=0.5, help="Threshold for the Key Risk Indicator.")
    risk_capacity_input = st.slider("Risk Capacity", min_value=0, max_value=100000, value=50000, step=1000, help="Total capital buffer available for losses.")
```

**Parameters Explained:**

*   **Max Expected Loss ($EL$):** The maximum average loss the organization is willing to accept over the simulation period.
*   **Max Unexpected Loss ($UL$):** The maximum potential deviation from the expected loss the organization is willing to tolerate.
*   **Max Severe Loss Events:** The maximum number of "severe" events (though the current code does not explicitly define or monitor "severe" events, it's a placeholder for future enhancement).
*   **KRI Limit:** The threshold for the Key Risk Indicator, above which it's considered out of appetite.
*   **Risk Capacity:** The total financial buffer available for absorbing losses. (Note: While defined, this parameter is not explicitly used in calculations or visualizations in the provided code, serving more as a conceptual input).

<aside class="negative">
The current implementation of `page2.py` defines `max_severe_loss_events_input` and `risk_capacity_input` in the UI, but their values are not actively used in the `calculate_risk_profile` or `monitor_risk_appetite` functions. This is an area for future enhancement where the application could incorporate more sophisticated monitoring logic.
</aside>

### 2. Calculating the Risk Profile

The `calculate_risk_profile` function computes the $EL$, $UL$, and KRI status based on the simulated data.

```python
# From application_pages/page2.py
@st.cache_data(show_spinner=False)
def calculate_risk_profile(df_simulated_operations, df_loss_events, user_parameters):
    """Computes the organization's simulated risk profile over time."""
    # ... (data validation and type conversion) ...

    df_risk_profile = df_simulated_operations.copy()

    # Calculate Expected Loss (EL) - based on overall mean loss
    df_risk_profile['ExpectedLoss'] = df_loss_events['LossAmount'].mean() if not df_loss_events.empty else 0

    # Calculate Unexpected Loss (UL) - based on overall standard deviation
    df_risk_profile['UnexpectedLoss'] = df_loss_events['LossAmount'].std() if not df_loss_events.empty else 0

    # Incorporate KRI values (flag if KRI exceeds limit)
    if 'KRI' in df_risk_profile.columns and 'KRI_Limit' in user_parameters:
        df_risk_profile.loc[:, 'KRI_Exceeded'] = df_risk_profile['KRI'] > user_parameters['KRI_Limit']

    return df_risk_profile
```

<aside class="positive">
In this simplified simulation, $EL$ and $UL$ are calculated as constant values over the entire simulation period, based on the mean and standard deviation of all simulated loss events. In a more advanced real-world scenario, these might be calculated using rolling windows, VaR models, or other statistical techniques to reflect dynamic risk profiles.
</aside>

### 3. Monitoring Risk Appetite

The `monitor_risk_appetite` function compares the calculated risk metrics ($EL$, $UL$, KRI) against the defined thresholds and determines if a breach has occurred.

```python
# From application_pages/page2.py
@st.cache_data(show_spinner=False)
def monitor_risk_appetite(df_risk_profile, risk_appetite_params):
    """Compares risk profile against risk appetite, identifies breaches and evaluates KRI status."""
    # ... (input validation) ...

    df_breaches = pd.DataFrame()
    df_kri_status = pd.DataFrame()

    if df_risk_profile.empty:
        return df_breaches, df_kri_status

    breach_data = []
    kri_status_data = []

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
            kri_status['KRI_Status'] = 'N/A'

        breach_data.append(breaches)
        kri_status_data.append(kri_status)

    df_breaches = pd.DataFrame(breach_data)
    df_kri_status = pd.DataFrame(kri_status_data)

    return df_breaches, df_kri_status
```

This function iterates through the daily risk profile and assigns a 'Breached' or 'Within Appetite' status for each metric based on the defined thresholds.

### 4. Retrieving Data from Session State

`page2.py` retrieves the `df_ops` and `df_losses` DataFrames generated in `page1.py` using `st.session_state`:

```python
# From application_pages/page2.py
# Load data from page 1 (simulated data)
if 'df_ops' in st.session_state and 'df_losses' in st.session_state:
    df_ops = st.session_state['df_ops']
    df_losses = st.session_state['df_losses']
    # ... rest of the page logic ...
else:
    st.info("Please generate data on the 'Data Generation & Visualization' page first.")
```

This mechanism ensures that the risk profile calculations are always based on the most recently generated or cached data.

### 5. Visualizing Risk Profile and Breaches

The page displays the calculated risk profile and breach statuses in dataframes, followed by insightful Altair charts.

```python
# From application_pages/page2.py
st.subheader("Calculated Risk Profile")
st.dataframe(df_risk_profile.head())

st.subheader("Risk Appetite Monitoring")
st.markdown("**Breach Status:**")
st.dataframe(df_breaches.head())
st.markdown("**KRI Status:**")
st.dataframe(df_kri_status.head())

st.subheader("Risk Profile vs. Risk Appetite")
# EL and UL Trend with Thresholds
if not df_risk_profile.empty:
    df_risk_profile['Date'] = pd.to_datetime(df_risk_profile['Date'])
    df_risk_profile_melted = df_risk_profile.melt(id_vars=['Date'], value_vars=['ExpectedLoss', 'UnexpectedLoss'], var_name='RiskMetric', value_name='Value')

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

    threshold_lines = alt.Chart(threshold_data).mark_rule(strokeDash=[3, 3]).encode(
        y='Threshold:Q',
        color=alt.Color('RiskMetric:N', title='Threshold For', scale=alt.Scale(range=['#17becf', '#e377c2'])),
        tooltip=[alt.Tooltip('Threshold:Q', title='Threshold')]
    )
    st.altair_chart(chart_risk_profile + threshold_lines, use_container_width=True)

# KRI Status Plot
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

These charts dynamically update as users adjust the risk appetite parameters, providing a visual representation of the organization's adherence to its risk appetite.

## Step 3: Understanding the References Page
Duration: 0:02:00

The `application_pages/page3.py` module is a straightforward but important component of the application, serving as a resource hub for users who want to delve deeper into the concepts and theoretical underpinnings of the Risk Appetite Framework.

### Purpose of `page3.py`

This page provides:
*   **Contextual Information:** Directs users to the primary theoretical source for the concepts implemented in the application, specifically the "Operational Risk Manager Handbook." This reinforces the credibility and educational value of the application.
*   **Further Exploration:** Links to the GitHub repository where the application's source code might be hosted or related lab exercises are available. This is invaluable for developers who want to review, fork, or contribute to the project.

### Code Snippet

```python
# From application_pages/page3.py
import streamlit as st

def run_page3():
    st.header("References")
    st.markdown("""
    [1] Chapter 3: The Risk Management Framework, Chapter 5: Risk Information, Operational Risk Manager Handbook, [Provided Document]. These sections discuss risk capacity, risk appetite, risk profile, and key risk indicators.
    [2] dalmirPereira/module6_labWork: Lab Exercises from Module 6 - GitHub, https://github.com/dalmirPereira/module6_labWork.
    """)
```

This page highlights the importance of grounding practical applications in sound theoretical knowledge, as well as acknowledging the resources that inspired or contributed to the project. It completes the overall structure by offering pathways for both business understanding and technical exploration.

## Conclusion
Duration: 0:05:00

Congratulations! You have successfully explored the architecture, functionalities, and underlying concepts of the Streamlit Risk Appetite Framework application.

Throughout this codelab, you've learned how to:

*   **Set up** a Streamlit development environment.
*   **Understand the modular design** of a multi-page Streamlit application using `app.py` as an orchestrator and dedicated pages for different functionalities.
*   **Simulate synthetic data** for business operations, revenue, operational loss events, and Key Risk Indicators (KRIs) using configurable parameters and statistical distributions (Poisson, Normal).
*   **Visualize complex time-series data** and distributions effectively using Altair charts.
*   **Define and apply quantitative risk appetite thresholds** for Expected Loss ($EL$), Unexpected Loss ($UL$), and KRIs.
*   **Calculate and monitor** a simulated risk profile against these thresholds.
*   **Identify and visualize breaches** of the defined risk appetite.
*   **Utilize `st.session_state`** for seamless data transfer between different pages of the Streamlit application.
*   **Leverage `st.cache_data`** for optimizing performance by caching computationally intensive functions.

This application serves as an excellent starting point for understanding how operational risk management principles, particularly the Risk Appetite Framework, can be translated into an interactive and visual tool. It demonstrates the power of Streamlit for rapid prototyping and deployment of data-driven applications.

**Importance of the Application:**

The ability to dynamically simulate scenarios and visualize their impact on risk metrics is invaluable for:

*   **Risk Education:** Helping stakeholders understand complex risk concepts.
*   **Strategy Formulation:** Informing business decisions by assessing the impact of different risk tolerances.
*   **Compliance:** Demonstrating a structured approach to risk management.
*   **Early Warning:** Providing a framework to monitor KRIs for potential future issues.

**Potential Enhancements and Next Steps:**

This application can be further extended to incorporate more sophisticated features:

*   **Advanced Loss Modeling:** Implement other loss distributions (e.g., Log-Normal, Gamma) or compound loss models.
*   **Scenario Analysis:** Allow users to define specific stress scenarios and observe their impact.
*   **Dynamic EL/UL:** Calculate Expected and Unexpected Loss using rolling windows or more advanced time-series methods rather than static, overall values.
*   **VaR Calculation:** Integrate Value at Risk (VaR) or Conditional Value at Risk (CVaR) as measures for Unexpected Loss.
*   **Multiple KRIs:** Allow the definition and monitoring of multiple distinct KRIs.
*   **Actual vs. Simulated Data:** Integrate functionality to upload and analyze real operational loss data alongside simulated data.
*   **Actionable Insights:** Add a module for recommending actions when risk appetite breaches occur.
*   **User Authentication:** For a production environment, implement user login and role-based access.

We encourage you to experiment with the code, modify parameters, and consider how you might expand this application to meet more complex risk management needs.

<button>
  [Download Application Code (if available)](https://github.com/your-repo-link/qu_lab_raf)
</button>
(Note: Replace the above link with the actual GitHub repository if you choose to publish this application.)

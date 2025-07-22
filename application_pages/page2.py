
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go

# Import the data generation function from page1
# Streamlit's caching mechanism ensures this won't re-run if inputs haven't changed.
from application_pages.page1 import generate_synthetic_data

st.markdown(r\"\"
# 2️⃣ Risk Profile & Monitoring

This section allows you to **define your organization's risk appetite** and observe how the simulated risk profile performs against these thresholds.

---
## Risk Appetite Definition

Your organization's risk appetite sets the boundaries for acceptable risk exposure. Here, you define quantitative limits for:

*   **Maximum Expected Loss ($EL$):** The highest average loss your organization anticipates.
*   **Maximum Unexpected Loss ($UL$):** The maximum potential loss deviation from $EL$ (often a measure like VaR).
*   **Maximum Severe Loss Events:** Tolerance for high-impact, low-frequency events.
*   **KRI Limit:** A threshold for the Key Risk Indicator that, if breached, signals increased risk.
*   **Risk Capacity:** The total capital or resources available to absorb losses.

Adjust these parameters in the sidebar to simulate different risk stances.

### Formulae Recap:
- Expected Loss ($EL$): Average historical loss.
- Unexpected Loss ($UL$): Standard deviation of historical losses (a simplified measure of volatility).

---
\"\"\")

# ------------ Sidebar Risk Appetite Definition Inputs -------------
with st.sidebar:
    st.subheader("2. Define Risk Appetite")
    max_expected_loss_input = st.slider(
        "Max Expected Loss ($EL$)",
        min_value=0, max_value=5000, value=1300, step=10,
        help="Maximum average loss an organization expects to incur over the period."
    )
    max_unexpected_loss_input = st.slider(
        "Max Unexpected Loss ($UL$)",
        min_value=0, max_value=1000, value=380, step=10,
        help="Potential for losses exceeding expected loss (e.g., standard deviation of losses)."
    )
    max_severe_loss_events_input = st.slider(
        "Max Severe Loss Events",
        min_value=0, max_value=20, value=5, step=1,
        help="Tolerance for the number of 'severe' operational loss events."
    )
    kri_limit_input = st.slider(
        "KRI Limit",
        min_value=0.0, max_value=100.0, value=55.0, step=0.5,
        help="Threshold for the Key Risk Indicator. If KRI goes above this, it's a concern."
    )
    risk_capacity_input = st.slider(
        "Risk Capacity",
        min_value=0, max_value=100000, value=50000, step=1000,
        help="Total capital buffer available for losses. (For illustrative purposes here)."
    )

# Consolidate user parameters into a dictionary for downstream functions
user_risk_appetite_params = {
    'MaxExpectedLoss_Threshold': float(max_expected_loss_input),
    'MaxUnexpectedLoss_Threshold': float(max_unexpected_loss_input),
    'MaxSevereLossEvents_Threshold': int(max_severe_loss_events_input),
    'KRI_Limit': float(kri_limit_input),
    'RiskCapacity': float(risk_capacity_input)
}

# Dummy variables to hold simulation parameters from page1 for regeneration
# In a real app, these would be passed via session state
# For now, we'll re-call generate_synthetic_data with fixed default values to get data for this page
# This is a simplification given the strict file structure; in a multi-page app,
# Streamlit.session_state would be used to share these between pages.
# For the purpose of meeting the requirements (calling the functions with parameters),
# we default them here.
sim_start_date_default = datetime(2022, 1, 1)
sim_end_date_default = datetime(2022, 1, 31)
business_params_default = {'growth_rate': 0.02}
loss_freq_params_default = {'mean': 2.0, 'std': 1.0}
loss_sev_params_default = {'mean': 1200.0, 'std': 300.0}
kpi_params_default = {'baseline': 50.0, 'volatility': 5.0}

df_ops, df_losses = generate_synthetic_data(
    sim_start_date_default, sim_end_date_default,
    business_params_default, loss_freq_params_default, loss_sev_params_default, kpi_params_default
)

# ------------- Risk Profile Calculation Function -------------
@st.cache_data(show_spinner=False)
def calculate_risk_profile(df_simulated_operations, df_loss_events, user_parameters):
    if df_simulated_operations.empty:
        # If operations data is empty, return empty risk profile
        return pd.DataFrame(columns=['Date', 'ExpectedLoss', 'UnexpectedLoss', 'KRI', 'KRI_Exceeded'])

    df_risk_profile = df_simulated_operations[['Date', 'KRI']].copy() # Start with Date and KRI

    # Daily Expected Loss: Average of losses up to that day (rolling mean) or overall mean.
    # For this simulation, we take overall mean of loss events.
    # We must ensure losses are aligned by date.
    if not df_loss_events.empty:
        df_loss_events_daily = df_loss_events.groupby('Date')['LossAmount'].sum().reset_index()
        df_risk_profile = pd.merge(df_risk_profile, df_loss_events_daily, on='Date', how='left')
        df_risk_profile['DailyLoss'] = df_risk_profile['LossAmount'].fillna(0) # Fill days with no losses with 0

        # Calculate Expected Loss (EL) and Unexpected Loss (UL) based on *daily* sums
        # For simplicity, we calculate EL and UL over the entire simulated period here,
        # rather than a rolling window, which would make more sense for dynamic risk profile.
        # This matches the provided notebook's simplified calculation.
        overall_expected_loss = df_loss_events['LossAmount'].mean() if not df_loss_events.empty else 0
        overall_unexpected_loss = df_loss_events['LossAmount'].std() if not df_loss_events.empty else 0

        df_risk_profile['ExpectedLoss'] = overall_expected_loss
        df_risk_profile['UnexpectedLoss'] = overall_unexpected_loss
    else:
        df_risk_profile['ExpectedLoss'] = 0
        df_risk_profile['UnexpectedLoss'] = 0
        df_risk_profile['DailyLoss'] = 0

    # Incorporate KRI values (flag if KRI exceeds limit)
    if 'KRI' in df_risk_profile.columns and 'KRI_Limit' in user_parameters:
        df_risk_profile.loc[:, 'KRI_Exceeded'] = df_risk_profile['KRI'] > user_parameters['KRI_Limit']
    else:
        df_risk_profile['KRI_Exceeded'] = False # Default to False if KRI or KRI_Limit is missing

    return df_risk_profile.fillna(0) # Fill any remaining NaNs, e.g. from merge

# Call the function with actual parameters
df_risk_profile = calculate_risk_profile(df_ops, df_losses, user_risk_appetite_params)

st.subheader("Calculated Risk Profile")
st.write(r"This table shows the daily Expected Loss ($EL$), Unexpected Loss ($UL$), KRI, and its status calculated from the simulated data.")
if not df_risk_profile.empty:
    st.dataframe(df_risk_profile.head())
else:
    st.info("Risk profile could not be calculated. Please ensure synthetic data is generated.")

# ------------- Risk Appetite Monitoring Function -------------
@st.cache_data(show_spinner=False)
def monitor_risk_appetite(df_risk_profile, risk_appetite_params):
    if not isinstance(df_risk_profile, pd.DataFrame) or df_risk_profile.empty:
        return pd.DataFrame(), pd.DataFrame() # Return empty if no data

    df_breaches = pd.DataFrame({'Date': df_risk_profile['Date']})
    df_kri_status = pd.DataFrame({'Date': df_risk_profile['Date']})

    # Expected Loss breach
    if 'ExpectedLoss' in df_risk_profile.columns and 'MaxExpectedLoss_Threshold' in risk_appetite_params:
        df_breaches['ExpectedLoss_Status'] = np.where(
            df_risk_profile['ExpectedLoss'] > risk_appetite_params['MaxExpectedLoss_Threshold'],
            'Breached', 'Within Appetite'
        )

    # Unexpected Loss breach
    if 'UnexpectedLoss' in df_risk_profile.columns and 'MaxUnexpectedLoss_Threshold' in risk_appetite_params:
        df_breaches['UnexpectedLoss_Status'] = np.where(
            df_risk_profile['UnexpectedLoss'] > risk_appetite_params['MaxUnexpectedLoss_Threshold'],
            'Breached', 'Within Appetite'
        )

    # KRI Status
    if 'KRI_Exceeded' in df_risk_profile.columns:
        df_kri_status['KRI_Status'] = np.where(
            df_risk_profile['KRI_Exceeded'],
            'Above Limit', 'Within Limit'
        )
    else:
        df_kri_status['KRI_Status'] = 'N/A' # Default if KRI_Exceeded is missing

    return df_breaches, df_kri_status

# Call the monitoring function
df_breaches, df_kri_status = monitor_risk_appetite(df_risk_profile, user_risk_appetite_params)

st.subheader("Risk Appetite Monitoring")
st.write(r"These tables show whether Expected Loss ($EL$), Unexpected Loss ($UL$), and the KRI are within the defined appetite on each simulated day.")

st.markdown("**Breach Status:**")
if not df_breaches.empty:
    st.dataframe(df_breaches.head())
else:
    st.info("No breach data available. Please ensure risk profile is calculated.")

st.markdown("**KRI Status:**")
if not df_kri_status.empty:
    st.dataframe(df_kri_status.head())
else:
    st.info("No KRI status data available. Please ensure risk profile is calculated.")


# ------------- Visualizations for Risk Profile and Breaches -------------
st.subheader("Risk Profile vs. Risk Appetite Visualizations")
st.write("Comparing calculated Expected Loss ($EL$) and Unexpected Loss ($UL$) against defined thresholds.")

if not df_risk_profile.empty:
    # EL and UL Trend with Thresholds
    fig_el_ul = go.Figure()

    # Expected Loss
    fig_el_ul.add_trace(go.Scatter(x=df_risk_profile['Date'], y=df_risk_profile['ExpectedLoss'],
                                   mode='lines+markers', name='Calculated Expected Loss',
                                   line=dict(color='#17becf')))
    fig_el_ul.add_hline(y=user_risk_appetite_params['MaxExpectedLoss_Threshold'],
                        line_dash="dash", line_color="#17becf",
                        annotation_text=f"Max EL: {user_risk_appetite_params['MaxExpectedLoss_Threshold']}",
                        annotation_position="top right")

    # Unexpected Loss
    fig_el_ul.add_trace(go.Scatter(x=df_risk_profile['Date'], y=df_risk_profile['UnexpectedLoss'],
                                   mode='lines+markers', name='Calculated Unexpected Loss',
                                   line=dict(color='#e377c2')))
    fig_el_ul.add_hline(y=user_risk_appetite_params['MaxUnexpectedLoss_Threshold'],
                        line_dash="dash", line_color="#e377c2",
                        annotation_text=f"Max UL: {user_risk_appetite_params['MaxUnexpectedLoss_Threshold']}",
                        annotation_position="bottom right")

    fig_el_ul.update_layout(
        title="Expected and Unexpected Loss Over Time vs. Appetite",
        xaxis_title="Date",
        yaxis_title="Loss Amount ($)",
        legend=dict(x=0.01, y=0.99, bordercolor="gray", borderwidth=0.5),
        template="plotly_white"
    )
    st.plotly_chart(fig_el_ul, use_container_width=True)

    # KRI Trend with Limit and Status
    # Merge df_risk_profile and df_kri_status for combined plot
    df_combined_kri = df_risk_profile.merge(df_kri_status, on='Date', how='left')

    fig_kri_monitor = go.Figure()
    fig_kri_monitor.add_trace(
        go.Scatter(x=df_combined_kri['Date'], y=df_combined_kri['KRI'],
                   mode='lines+markers', name='KRI Value',
                   line=dict(color='#2ca02c'))
    )
    fig_kri_monitor.add_hline(y=user_risk_appetite_params['KRI_Limit'],
                              line_dash="dash", line_color="#d62728",
                              annotation_text=f"KRI Limit: {user_risk_appetite_params['KRI_Limit']}",
                              annotation_position="top right")

    # Add points for breaches
    breached_kri_dates = df_combined_kri[df_combined_kri['KRI_Exceeded']]['Date']
    breached_kri_values = df_combined_kri[df_combined_kri['KRI_Exceeded']]['KRI']

    fig_kri_monitor.add_trace(
        go.Scatter(x=breached_kri_dates, y=breached_kri_values,
                   mode='markers', name='KRI Above Limit',
                   marker=dict(color='#d62728', size=10, symbol='circle'),
                   hoverinfo='text',
                   hovertext=[f"Date: {d.strftime('%Y-%m-%d')}<br>KRI: {v:.2f}<br>Status: Above Limit" for d,v in zip(breached_kri_dates, breached_kri_values)])
    )

    fig_kri_monitor.update_layout(
        title="KRI Performance Against Limit",
        xaxis_title="Date",
        yaxis_title="KRI Value",
        legend=dict(x=0.01, y=0.99, bordercolor="gray", borderwidth=0.5),
        template="plotly_white"
    )
    st.plotly_chart(fig_kri_monitor, use_container_width=True)

else:
    st.info("No risk profile data available to generate visualizations. Adjust simulation parameters.")

st.markdown(r\"\"
---
> 📊 *Observe how your chosen risk appetite thresholds affect the 'breach' status. A robust framework adapts to changing risk profiles.*
\"\"\")

def run_page2():
    # This function acts as the entry point for this page
    # All logic and UI elements are directly in the script, so calling it runs them.
    pass # No explicit function call needed here as the code runs top-down

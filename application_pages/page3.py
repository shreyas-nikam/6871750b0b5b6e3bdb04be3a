
import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go

# Import necessary functions from other pages to access data
from application_pages.page1 import generate_synthetic_data
# We will define dummy inputs for page2 functions, as we cannot use session_state for sharing
# state between pages due to the task constraints (no execution, just file writing).
# In a real Streamlit app, session_state would pass parameters.
# For this task, we re-run with defaults for demonstration and file creation.

# Default simulation parameters to generate data for this page
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

# Default risk appetite parameters to calculate risk profile for this page
user_risk_appetite_params_default = {
    'MaxExpectedLoss_Threshold': 1300.0,
    'MaxUnexpectedLoss_Threshold': 380.0,
    'MaxSevereLossEvents_Threshold': 5,
    'KRI_Limit': 55.0,
    'RiskCapacity': 50000.0
}

# Import calculate_risk_profile from page2
# (Defining it here again for independent file, as per requirement, but conceptually from page2 logic)
@st.cache_data(show_spinner=False)
def calculate_risk_profile(df_simulated_operations, df_loss_events, user_parameters):
    if df_simulated_operations.empty:
        return pd.DataFrame(columns=['Date', 'ExpectedLoss', 'UnexpectedLoss', 'KRI', 'KRI_Exceeded'])

    df_risk_profile = df_simulated_operations[['Date', 'KRI']].copy()

    if not df_loss_events.empty:
        df_loss_events_daily = df_loss_events.groupby('Date')['LossAmount'].sum().reset_index()
        df_risk_profile = pd.merge(df_risk_profile, df_loss_events_daily, on='Date', how='left')
        df_risk_profile['DailyLoss'] = df_risk_profile['LossAmount'].fillna(0)

        overall_expected_loss = df_loss_events['LossAmount'].mean() if not df_loss_events.empty else 0
        overall_unexpected_loss = df_loss_events['LossAmount'].std() if not df_loss_events.empty else 0

        df_risk_profile['ExpectedLoss'] = overall_expected_loss
        df_risk_profile['UnexpectedLoss'] = overall_unexpected_loss
    else:
        df_risk_profile['ExpectedLoss'] = 0
        df_risk_profile['UnexpectedLoss'] = 0
        df_risk_profile['DailyLoss'] = 0

    if 'KRI' in df_risk_profile.columns and 'KRI_Limit' in user_parameters:
        df_risk_profile.loc[:, 'KRI_Exceeded'] = df_risk_profile['KRI'] > user_parameters['KRI_Limit']
    else:
        df_risk_profile['KRI_Exceeded'] = False

    return df_risk_profile.fillna(0)

df_risk_profile = calculate_risk_profile(df_ops, df_losses, user_risk_appetite_params_default)

# Import monitor_risk_appetite from page2
# (Defining it here again for independent file, as per requirement, but conceptually from page2 logic)
@st.cache_data(show_spinner=False)
def monitor_risk_appetite(df_risk_profile, risk_appetite_params):
    if not isinstance(df_risk_profile, pd.DataFrame) or df_risk_profile.empty:
        return pd.DataFrame(), pd.DataFrame()

    df_breaches = pd.DataFrame({'Date': df_risk_profile['Date']})
    df_kri_status = pd.DataFrame({'Date': df_risk_profile['Date']})

    if 'ExpectedLoss' in df_risk_profile.columns and 'MaxExpectedLoss_Threshold' in risk_appetite_params:
        df_breaches['ExpectedLoss_Status'] = np.where(
            df_risk_profile['ExpectedLoss'] > risk_appetite_params['MaxExpectedLoss_Threshold'],
            'Breached', 'Within Appetite'
        )

    if 'UnexpectedLoss' in df_risk_profile.columns and 'MaxUnexpectedLoss_Threshold' in risk_appetite_params:
        df_breaches['UnexpectedLoss_Status'] = np.where(
            df_risk_profile['UnexpectedLoss'] > risk_appetite_params['MaxUnexpectedLoss_Threshold'],
            'Breached', 'Within Appetite'
        )

    if 'KRI_Exceeded' in df_risk_profile.columns:
        df_kri_status['KRI_Status'] = np.where(
            df_risk_profile['KRI_Exceeded'],
            'Above Limit', 'Within Limit'
        )
    else:
        df_kri_status['KRI_Status'] = 'N/A'

    return df_breaches, df_kri_status

df_breaches, df_kri_status = monitor_risk_appetite(df_risk_profile, user_risk_appetite_params_default)

st.markdown(r\"\"
# 3️⃣ KRI Dashboard & References

This section provides a summary of the Key Risk Indicator (KRI) performance and includes important references.

---
## KRI Performance Dashboard

The **Key Risk Indicator (KRI)** is a forward-looking measure that provides insight into an organization's operational risk exposure. Monitoring KRIs helps identify potential issues before they escalate into actual losses.

Here, we summarize the KRI status against the defined `KRI Limit`.

### KRI Status Summary:
\"\"\")

if not df_kri_status.empty:
    kri_breach_count = df_kri_status[df_kri_status['KRI_Status'] == 'Above Limit'].shape[0]
    total_days = df_kri_status.shape[0]
    kri_summary = "- **Total Simulation Days:** " + str(total_days) + "\n"                   "- **Days KRI was Above Limit:** " + str(kri_breach_count) + "\n"                   "- **Percentage of Days Above Limit:** $" + str(kri_breach_count / total_days * 100) + "%$"

    st.markdown(kri_summary)

    st.subheader("Daily KRI Status Table")
    st.write("A detailed breakdown of KRI status for each day:")
    st.dataframe(df_kri_status)

    st.subheader("KRI Distribution by Status")
    fig_kri_dist = px.bar(df_kri_status['KRI_Status'].value_counts().reset_index(),
                          x='index', y='KRI_Status',
                          title="Count of Days by KRI Status",
                          labels={'index': 'KRI Status', 'KRI_Status': 'Number of Days'},
                          color='index',
                          color_discrete_map={'Within Limit': '#2ca02c', 'Above Limit': '#d62728'})
    st.plotly_chart(fig_kri_dist, use_container_width=True)

else:
    st.info("KRI data not available. Please ensure synthetic data generation parameters are set on Page 1.")


st.markdown(r\"\"
---
## References

This application is inspired by concepts in operational risk management.

*   [1] **Chapter 3: The Risk Management Framework, Chapter 5: Risk Information**, Operational Risk Manager Handbook, [Provided Document]. These sections discuss risk capacity, risk appetite, risk profile, and key risk indicators.
*   [2] dalmirPereira/module6_labWork: Lab Exercises from Module 6 - GitHub, https://github.com/dalmirPereira/module6_labWork.
\"\"\")

def run_page3():
    pass # All logic and UI elements are directly in the script, so calling it runs them.

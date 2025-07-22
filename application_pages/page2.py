
import streamlit as st
import pandas as pd
import altair as alt

def run_page2():
    st.header("Risk Profile and Monitoring")
    st.markdown("This page allows you to define your risk appetite and monitor your risk profile against these defined thresholds. The risk profile is calculated based on the data generated on the previous page.")

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

    # Load data from page 1 (simulated data)
    if 'df_ops' in st.session_state and 'df_losses' in st.session_state:
        df_ops = st.session_state['df_ops']
        df_losses = st.session_state['df_losses']

        # Call the functions
        df_risk_profile = calculate_risk_profile(df_ops, df_losses, user_risk_appetite_params)
        df_breaches, df_kri_status = monitor_risk_appetite(df_risk_profile, user_risk_appetite_params)

        st.subheader("Calculated Risk Profile")
        st.write("This table shows the daily Expected Loss ($EL$), Unexpected Loss ($UL$), and KRI status calculated from the simulated data.")
        st.dataframe(df_risk_profile.head())

        st.subheader("Risk Appetite Monitoring")
        st.write("These tables show whether Expected Loss, Unexpected Loss, and the KRI are within the defined appetite.")

        st.markdown("**Breach Status:**")
        st.dataframe(df_breaches.head())

        st.markdown("**KRI Status:**")
        st.dataframe(df_kri_status.head())

        st.subheader("Risk Profile vs. Risk Appetite")
        st.write("Comparing calculated Expected Loss ($EL$) and Unexpected Loss ($UL$) against defined thresholds.")

        # EL and UL Trend with Thresholds
        if not df_risk_profile.empty:
            df_risk_profile['Date'] = pd.to_datetime(df_risk_profile['Date'])
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
    else:
        st.info("Please generate data on the 'Data Generation & Visualization' page first.")

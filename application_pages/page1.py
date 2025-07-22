
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from datetime import datetime

def run_page1():
    st.header("Data Generation and Visualization")
    st.markdown("This page allows you to generate synthetic data for business operations, loss events, and key risk indicators (KRIs). You can adjust the parameters in the sidebar to see how they affect the generated data and visualizations.")

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
    st.altair_chart(chart_kri, use_container_width=True)

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


import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
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

def simulate_operational_losses(start_date, end_date, avg_daily_losses, severity_mu, severity_sigma, severe_loss_threshold):
    """Simulates operational loss events using a frequency-severity approach."""
    if pd.to_datetime(start_date) > pd.to_datetime(end_date):
        raise ValueError("Start date must be before end date.")

    date_range = pd.date_range(start=start_date, end=end_date)
    all_losses = []

    for date in date_range:
        num_losses = np.random.poisson(avg_daily_losses)
        if num_losses > 0:
            loss_amounts = np.random.lognormal(mean=severity_mu, sigma=severity_sigma, size=num_losses)
            day_losses = pd.DataFrame({'Date': [date] * num_losses, 'Loss_Amount': loss_amounts})
            all_losses.append(day_losses)

    if all_losses:
        losses_df = pd.concat(all_losses, ignore_index=True)
        losses_df['Date'] = pd.to_datetime(losses_df['Date'])
    else:
        losses_df = pd.DataFrame({'Date': [], 'Loss_Amount': []})

    losses_df['Is_Severe'] = losses_df['Loss_Amount'] > severe_loss_threshold
    return losses_df

def run_page1():
    st.header("Data Generation")

    start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2023-01-01"))
    end_date = st.sidebar.date_input("End Date", value=pd.to_datetime("2023-12-31"))

    avg_revenue = st.sidebar.number_input("Average Daily Revenue", value=10000.0)
    revenue_volatility = st.sidebar.slider("Revenue Volatility", min_value=0.0, max_value=1.0, value=0.1, step=0.01)
    baseline_expenses = st.sidebar.number_input("Baseline Daily Expenses", value=6000.0)

    avg_daily_losses = st.sidebar.number_input("Average Daily Losses", value=0.5)
    severity_mu = st.sidebar.number_input("Severity Mu", value=5.0)
    severity_sigma = st.sidebar.number_input("Severity Sigma", value=2.0)
    severe_loss_threshold = st.sidebar.number_input("Severe Loss Threshold", value=1000.0)

    business_data = generate_business_data(start_date, end_date, avg_revenue, revenue_volatility, baseline_expenses)
    losses_data = simulate_operational_losses(start_date, end_date, avg_daily_losses, severity_mu, severity_sigma, severe_loss_threshold)

    if business_data is not None:
        st.subheader("Business Data")
        st.dataframe(business_data)

        fig_business = px.line(business_data, x=business_data.index, y=['Revenue', 'Expenses', 'Profit'], title="Business Performance")
        st.plotly_chart(fig_business, use_container_width=True)

    if not losses_data.empty:
        st.subheader("Operational Losses Data")
        st.dataframe(losses_data)

        fig_losses = px.histogram(losses_data, x="Loss_Amount", title="Loss Amount Distribution")
        st.plotly_chart(fig_losses, use_container_width=True)

        severe_loss_counts = losses_data['Is_Severe'].value_counts().reset_index()
        severe_loss_counts.columns = ['Is_Severe', 'Count']
        fig_severe = px.bar(severe_loss_counts, x='Is_Severe', y='Count', title='Severe vs Non-Severe Losses')
        st.plotly_chart(fig_severe, use_container_width=True)

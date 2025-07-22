import pandas as pd
import logging

def configure_notebook_environment():
    """Sets up display options for pandas, configures logging, and imports necessary libraries."""

    # Pandas display options
    pd.set_option("display.max_columns", None)
    pd.set_option("display.expand_frame_repr", False)
    pd.set_option("display.max_rows", 200)

    # Configure logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

import pandas as pd
import numpy as np
from datetime import timedelta

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
    df_simulated_operations['BusinessVolume'] = 100
    for i in range(1, len(df_simulated_operations)):
        df_simulated_operations['BusinessVolume'][i] = df_simulated_operations['BusinessVolume'][i-1] * (1 + growth_rate)
    df_simulated_operations['BusinessVolume'] = df_simulated_operations['BusinessVolume'].astype(int)

    # Revenue
    df_simulated_operations['Revenue'] = df_simulated_operations['BusinessVolume'] * 0.1

    # Loss Events
    loss_mean = loss_freq_params.get('mean', 2)
    loss_std = loss_freq_params.get('std', 1) if 'std' in loss_freq_params else 0 # Added std for poisson
    df_loss_events = pd.DataFrame(columns=['Date', 'LossAmount'])
    
    for date in dates:
        num_losses = np.random.poisson(loss_mean)
        if num_losses > 0:
            loss_amounts = np.random.normal(loss_sev_params.get('mean', 1000), loss_sev_params.get('std', 200), num_losses)
            temp_df = pd.DataFrame({'Date': [date] * num_losses, 'LossAmount': loss_amounts})
            df_loss_events = pd.concat([df_loss_events, temp_df], ignore_index=True)
    
    df_loss_events['LossAmount'] = df_loss_events['LossAmount'].abs() #Making sure LossAmount is positive

    # Key Risk Indicator
    baseline = kpi_params.get('baseline', 50)
    volatility = kpi_params.get('volatility', 5)
    df_simulated_operations['KRI'] = np.random.normal(baseline, volatility, len(df_simulated_operations))

    return df_simulated_operations, df_loss_events

import ipywidgets as widgets
from IPython.display import display

def define_risk_appetite_parameters():
    """Allows users to set risk appetite interactively."""

    max_expected_loss = widgets.FloatSlider(description="Max Expected Loss:")
    max_unexpected_loss = widgets.FloatSlider(description="Max Unexpected Loss:")
    max_severe_loss_events = widgets.IntSlider(description="Max Severe Loss Events:")
    kri_limit = widgets.FloatSlider(description="KRI Limit:")
    risk_capacity = widgets.FloatSlider(description="Risk Capacity:")

    display(max_expected_loss, max_unexpected_loss, max_severe_loss_events, kri_limit, risk_capacity)

    # You can access the values using max_expected_loss.value, etc.
    # In a real application, you would likely have a button to "save" these values
    # and then store them in a configuration or database.
    return None

import pandas as pd

def calculate_risk_profile(df_simulated_operations, df_loss_events, user_parameters):
    """Computes the organization's simulated risk profile over time."""

    if df_simulated_operations.empty and df_loss_events.empty:
        return pd.DataFrame()

    try:
        df_simulated_operations['Date'] = pd.to_datetime(df_simulated_operations['Date'])
        df_loss_events['Date'] = pd.to_datetime(df_loss_events['Date'])
    except Exception as e:
        raise e

    df_risk_profile = df_simulated_operations.copy()
    
    # Calculate Expected Loss (EL)
    df_risk_profile['ExpectedLoss'] = df_loss_events['LossAmount'].mean() if not df_loss_events.empty else 0
    
    # Calculate Unexpected Loss (UL) - Simple example: standard deviation
    df_risk_profile['UnexpectedLoss'] = df_loss_events['LossAmount'].std() if not df_loss_events.empty else 0

    # Incorporate KRI values (example: flag if KRI exceeds limit)
    if 'KRI_1' in df_risk_profile.columns and 'KRI_1_Limit' in user_parameters:
        df_risk_profile['KRI_1_Exceeded'] = df_risk_profile['KRI_1'] > user_parameters['KRI_1_Limit']

    return df_risk_profile

import pandas as pd

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

    for index, row in df_risk_profile.iterrows():
        breaches = {}
        kri_status = {}

        # Check for breaches
        if 'AggregatedLoss' in df_risk_profile.columns and 'MaxExpectedLoss_Threshold' in risk_appetite_params:
            if row['AggregatedLoss'] > risk_appetite_params['MaxExpectedLoss_Threshold']:
                breaches['AggregatedLoss'] = 'Breached'
            else:
                breaches['AggregatedLoss'] = 'Within Appetite'

        if 'UnexpectedLoss' in df_risk_profile.columns and 'MaxUnexpectedLoss_Threshold' in risk_appetite_params:
            if row['UnexpectedLoss'] > risk_appetite_params['MaxUnexpectedLoss_Threshold']:
                breaches['UnexpectedLoss'] = 'Breached'
            else:
                breaches['UnexpectedLoss'] = 'Within Appetite'

        if 'NumSevereLossEvents' in df_risk_profile.columns and 'MaxSevereLossEvents_Threshold' in risk_appetite_params:
            if row['NumSevereLossEvents'] > risk_appetite_params['MaxSevereLossEvents_Threshold']:
                breaches['NumSevereLossEvents'] = 'Breached'
            else:
                breaches['NumSevereLossEvents'] = 'Within Appetite'

        # Check KRI Status
        if 'KRI_1' in df_risk_profile.columns and 'KRI_1_Limit' in risk_appetite_params:
            if row['KRI_1'] > risk_appetite_params['KRI_1_Limit']:
                kri_status['KRI_1'] = 'Above Limit'
            else:
                kri_status['KRI_1'] = 'Within Limit'

        if 'KRI_2' in df_risk_profile.columns and 'KRI_2_Limit' in risk_appetite_params:
            if row['KRI_2'] > risk_appetite_params['KRI_2_Limit']:
                kri_status['KRI_2'] = 'Above Limit'
            else:
                kri_status['KRI_2'] = 'Within Limit'

        breach_data.append(breaches)
        kri_status_data.append(kri_status)

    df_breaches = pd.DataFrame(breach_data)
    df_kri_status = pd.DataFrame(kri_status_data)

    return df_breaches, df_kri_status
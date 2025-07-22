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
        return pd.DataFrame()

    # Identify severe loss events
    losses_df['Is_Severe'] = losses_df['Loss_Amount'] > severe_loss_threshold

    return losses_df

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

import pandas as pd

def combine_synthetic_data(business_df, losses_df, kri_df):
    """Merges all generated data into a single DataFrame."""
    combined_df = pd.concat([business_df, losses_df, kri_df], ignore_index=True)
    return combined_df

import ipywidgets as widgets
from IPython.display import display

def display_risk_appetite_inputs():
    """Displays interactive widgets for risk appetite parameters."""
    try:
        # Define widgets
        investment_horizon = widgets.IntSlider(
            value=5,
            min=1,
            max=20,
            step=1,
            description='Investment Horizon (years):',
            continuous_update=False
        )

        risk_tolerance = widgets.FloatSlider(
            value=0.5,
            min=0.0,
            max=1.0,
            step=0.05,
            description='Risk Tolerance:',
            continuous_update=False
        )

        # Display widgets
        display(investment_horizon)
        display(risk_tolerance)

    except ImportError:
        print("ipywidgets is not installed. Please install it to use this functionality.")
    except Exception as e:
        print(f"An error occurred while displaying the widgets: {e}")

import pandas as pd

def calculate_risk_capacity(financial_data, capital_multiple):
    """Calculates risk capacity based on financial data and a capital multiple."""
    if not isinstance(financial_data, pd.DataFrame):
        raise TypeError("financial_data must be a pandas DataFrame")

    if financial_data.empty:
        return 0

    profit_mean = financial_data['Profit'].mean()
    risk_capacity = profit_mean * capital_multiple
    return risk_capacity

import pandas as pd

def calculate_risk_profile(daily_losses, daily_kris):
    """Aggregates daily operational losses and KRI statuses.

    Arguments:
        daily_losses: DataFrame containing daily operational losses.
        daily_kris: DataFrame containing daily KRI data.

    Output:
        A DataFrame representing the risk profile.
    """
    if daily_losses.empty and daily_kris.empty:
        return pd.DataFrame()

    if daily_losses.empty or daily_kris.empty:
        if daily_losses.empty:
            losses = pd.DataFrame({'Date': [], 'Loss_Amount': []})
        else:
            losses = daily_losses
        if daily_kris.empty:
            kris = pd.DataFrame({'Date': [], 'KRI_Status': []})
        else:
            kris = daily_kris
    else:
        losses = daily_losses
        kris = daily_kris

    try:
        losses['Loss_Amount'] = pd.to_numeric(losses['Loss_Amount'])
    except KeyError:
        raise KeyError("Loss_Amount column missing in daily_losses DataFrame")
    except ValueError:
        raise TypeError("Loss_Amount column contains non-numeric values")

    if 'Date' not in losses.columns or 'Date' not in kris.columns:
          raise KeyError("Date column missing")


    # Aggregate losses (example: sum of losses)
    total_loss = losses['Loss_Amount'].sum()

    # Aggregate KRI statuses (example: count of each status)
    kri_counts = kris['KRI_Status'].value_counts()

    # Combine into a risk profile DataFrame
    risk_profile = pd.DataFrame({
        'Total_Loss': [total_loss],
        'KRI_Green_Count': [kri_counts.get('Green', 0)],
        'KRI_Amber_Count': [kri_counts.get('Amber', 0)],
        'KRI_Red_Count': [kri_counts.get('Red', 0)]
    })

    return risk_profile

def apply_insurance_mitigation(loss_series, deductible, cover_limit):
                """Calculates the transferred loss for each event."""
                transferred_loss = [min(max(x - deductible, 0), cover_limit) for x in loss_series]
                return transferred_loss

import pandas as pd

def monitor_breaches(risk_profile_df, risk_appetite_params):
    """
    Compares risk profile metrics against risk appetite thresholds and flags breaches.
    """
    if risk_profile_df.empty:
        return pd.DataFrame()

    breaches = []
    for index, row in risk_profile_df.iterrows():
        breach = {}
        if row['EL'] > risk_appetite_params['max_EL']:
            breach['EL'] = row['EL']
        if row['UL'] > risk_appetite_params['max_UL']:
            breach['UL'] = row['UL']
        if row['SevereEvents'] > risk_appetite_params['max_SevereEvents']:
            breach['SevereEvents'] = row['SevereEvents']
        if row['KRI1'] > risk_appetite_params['KRI1_threshold']:
            breach['KRI1'] = row['KRI1']
        if row['KRI2'] > risk_appetite_params['KRI2_threshold']:
            breach['KRI2'] = row['KRI2']

        if breach:
            breach['index'] = index
            breaches.append(breach)

    if not breaches:
        return None

    breaches_df = pd.DataFrame(breaches)
    breaches_df = breaches_df.set_index('index')
    return breaches_df

import pandas as pd
import matplotlib.pyplot as plt

def plot_time_series_metrics(df, metrics, title, y_label):
    """Generates a time-series plot of specified metrics.
    Args:
        df: DataFrame containing the data.
        metrics: List of metrics to plot.
        title: Title of the plot.
        y_label: Label for the y-axis.
    Output:
        None. Displays the time series plot.
    """
    if df.empty:
        print("DataFrame is empty. No plot will be generated.")
        return

    if not isinstance(df.index, pd.DatetimeIndex):
        if 'Date' in df.columns:
            df = df.set_index('Date')
        else:
            raise TypeError("DataFrame index must be DatetimeIndex or have a 'Date' column to be used as index.")

    plt.figure(figsize=(10, 6))
    for metric in metrics:
        if metric not in df.columns:
            raise KeyError(f"Metric '{metric}' not found in DataFrame.")
        plt.plot(df.index, df[metric], label=metric)

    plt.xlabel('Time')
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_loss_distribution_and_kri_correlation(losses_df, kri_df):
    """Generates loss distribution and KRI correlation plot."""

    if losses_df.empty or kri_df.empty:
        print("Warning: Input DataFrames are empty. No plots will be generated.")
        return

    try:
        losses_df['Loss_Amount'] = pd.to_numeric(losses_df['Loss_Amount'])
        kri_df['KRI_Value'] = pd.to_numeric(kri_df['KRI_Value'])
        losses_df['Date'] = pd.to_datetime(losses_df['Date'])
        kri_df['Date'] = pd.to_datetime(kri_df['Date'])
    except KeyError as e:
        print(f"Error: Missing required column. {e}")
        return
    except ValueError as e:
        print(f"Error: Non-numeric data found. {e}")
        return

    plt.figure(figsize=(14, 6))

    # Loss Distribution
    plt.subplot(1, 2, 1)
    sns.histplot(losses_df['Loss_Amount'], kde=True)
    plt.title('Loss Amount Distribution')
    plt.xlabel('Loss Amount')
    plt.ylabel('Frequency')

    # KRI Correlation (Aggregated Monthly)
    losses_monthly = losses_df.groupby(pd.Grouper(key='Date', freq='M'))['Loss_Amount'].sum()
    kri_monthly = kri_df.groupby(pd.Grouper(key='Date', freq='M'))['KRI_Value'].mean()

    merged_data = pd.merge(losses_monthly, kri_monthly, left_index=True, right_index=True, how='inner')

    if not merged_data.empty:
        plt.subplot(1, 2, 2)
        plt.scatter(merged_data['KRI_Value'], merged_data['Loss_Amount'])
        plt.title('Monthly Loss vs. KRI')
        plt.xlabel('Average Monthly KRI Value')
        plt.ylabel('Total Monthly Loss Amount')
        plt.tight_layout()  # Adjust layout to prevent labels from overlapping
        plt.show()
    else:
        print("Warning: No common dates between losses and KRI data. No correlation plot generated.")
    plt.show()

import pandas as pd

def display_breach_summary_table(breach_df):
    """Presents a table summarizing identified breaches."""
    if not breach_df.empty:
        print(breach_df.to_string())
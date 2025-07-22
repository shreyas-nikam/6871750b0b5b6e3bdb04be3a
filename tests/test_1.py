import pytest
import pandas as pd
import numpy as np
from definition_f00ce62bf960446492aacec86245a5b0 import simulate_operational_losses

@pytest.fixture
def sample_severity_params():
    return {'mu': 5, 'sigma': 2}

def test_simulate_operational_losses_empty(sample_severity_params):
    start_date = '2023-01-01'
    end_date = '2023-01-01'
    avg_daily_losses = 0
    severe_loss_threshold = 1000

    df = simulate_operational_losses(start_date, end_date, avg_daily_losses, sample_severity_params, severe_loss_threshold)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 0 if df is not None else True

def test_simulate_operational_losses_valid(sample_severity_params):
    start_date = '2023-01-01'
    end_date = '2023-01-10'
    avg_daily_losses = 5
    severe_loss_threshold = 1000

    df = simulate_operational_losses(start_date, end_date, avg_daily_losses, sample_severity_params, severe_loss_threshold)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert 'Loss_Amount' in df.columns
    assert 'Is_Severe' in df.columns
    assert len(df) <= (int((pd.to_datetime(end_date) - pd.to_datetime(start_date)).days) + 1) * 20, "Check the poisson simulation"

def test_simulate_operational_losses_date_order(sample_severity_params):
    start_date = '2023-01-10'
    end_date = '2023-01-01'
    avg_daily_losses = 5
    severe_loss_threshold = 1000

    with pytest.raises(ValueError):
        simulate_operational_losses(start_date, end_date, avg_daily_losses, sample_severity_params, severe_loss_threshold)

def test_simulate_operational_losses_avg_losses_type(sample_severity_params):
    start_date = '2023-01-01'
    end_date = '2023-01-10'
    avg_daily_losses = 'a'
    severe_loss_threshold = 1000

    with pytest.raises(TypeError):
        simulate_operational_losses(start_date, end_date, avg_daily_losses, sample_severity_params, severe_loss_threshold)

def test_simulate_operational_losses_severe_loss_threshold_type(sample_severity_params):
    start_date = '2023-01-01'
    end_date = '2023-01-10'
    avg_daily_losses = 5
    severe_loss_threshold = 'a'

    with pytest.raises(TypeError):
        simulate_operational_losses(start_date, end_date, avg_daily_losses, sample_severity_params, severe_loss_threshold)

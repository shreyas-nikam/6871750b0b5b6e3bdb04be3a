import pytest
from definition_4552b33391a64867bf5fbc78e5ee191b import generate_synthetic_data
import pandas as pd
from datetime import datetime

@pytest.fixture
def default_params():
    return {
        'start_date': datetime(2023, 1, 1),
        'end_date': datetime(2023, 1, 31),
        'business_params': {'growth_rate': 0.01},
        'loss_freq_params': {'mean': 2},
        'loss_sev_params': {'mean': 1000, 'std': 200},
        'kpi_params': {'baseline': 50, 'volatility': 5}
    }

def test_generate_synthetic_data_valid_dates(default_params):
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 1, 10)
    default_params['start_date'] = start_date
    default_params['end_date'] = end_date
    df_simulated_operations, df_loss_events = generate_synthetic_data(**default_params)
    assert isinstance(df_simulated_operations, pd.DataFrame)
    assert isinstance(df_loss_events, pd.DataFrame)

def test_generate_synthetic_data_empty_params(default_params):
    df_simulated_operations, df_loss_events = generate_synthetic_data(datetime(2023,1,1), datetime(2023,1,31), {}, {}, {}, {})
    assert isinstance(df_simulated_operations, pd.DataFrame)
    assert isinstance(df_loss_events, pd.DataFrame)

def test_generate_synthetic_data_start_after_end(default_params):
    with pytest.raises(ValueError):
        generate_synthetic_data(datetime(2023, 1, 10), datetime(2023, 1, 1), default_params['business_params'], default_params['loss_freq_params'], default_params['loss_sev_params'], default_params['kpi_params'])

def test_generate_synthetic_data_invalid_date_type(default_params):
    with pytest.raises(TypeError):
        generate_synthetic_data("2023-01-01", "2023-01-31", default_params['business_params'], default_params['loss_freq_params'], default_params['loss_sev_params'], default_params['kpi_params'])

def test_generate_synthetic_data_returns_dataframes(default_params):
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 1, 31)
    df_simulated_operations, df_loss_events = generate_synthetic_data(start_date, end_date, default_params['business_params'], default_params['loss_freq_params'], default_params['loss_sev_params'], default_params['kpi_params'])
    assert isinstance(df_simulated_operations, pd.DataFrame)
    assert isinstance(df_loss_events, pd.DataFrame)

import pytest
from definition_f1b9936863474368ae3cc24535e029c8 import validate_and_preprocess_data
import pandas as pd
import numpy as np

@pytest.fixture
def sample_data():
    df_simulated_operations = pd.DataFrame({
        'Date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03']),
        'BusinessVolume': [100, 110, 120],
        'Revenue': [10, 11, 12],
        'KRI_1': [1, 2, 3],
        'KRI_2': [4, 5, 6]
    })
    df_loss_events = pd.DataFrame({
        'Date': pd.to_datetime(['2023-01-01', '2023-01-02']),
        'LossAmount': [5, 10],
        'Type': ['Operational', 'Fraud']
    })
    return df_simulated_operations, df_loss_events

def test_validate_and_preprocess_data_success(sample_data):
    df_simulated_operations, df_loss_events = sample_data
    try:
        validate_and_preprocess_data(df_simulated_operations, df_loss_events)
    except Exception as e:
        assert False, f"Unexpected exception: {e}"

def test_validate_and_preprocess_data_missing_column(sample_data):
    df_simulated_operations, df_loss_events = sample_data
    del df_simulated_operations['BusinessVolume']
    with pytest.raises(KeyError):
         validate_and_preprocess_data(df_simulated_operations, df_loss_events)

def test_validate_and_preprocess_data_missing_values(sample_data):
    df_simulated_operations, df_loss_events = sample_data
    df_loss_events.loc[0, 'LossAmount'] = np.nan
    with pytest.raises(ValueError):
        validate_and_preprocess_data(df_simulated_operations, df_loss_events)
        
def test_validate_and_preprocess_data_empty_dataframe():
    df_simulated_operations = pd.DataFrame()
    df_loss_events = pd.DataFrame()
    try:
        validate_and_preprocess_data(df_simulated_operations, df_loss_events)
    except Exception as e:
        assert False, f"Unexpected exception: {e}"

def test_validate_and_preprocess_data_incorrect_date_format(sample_data):
    df_simulated_operations, df_loss_events = sample_data
    df_simulated_operations['Date'] = df_simulated_operations['Date'].astype(str)
    with pytest.raises(TypeError):
         validate_and_preprocess_data(df_simulated_operations, df_loss_events)

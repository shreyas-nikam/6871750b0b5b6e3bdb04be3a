import pytest
import pandas as pd
from definition_16e91d73bf5e401583ef8f2eb2f47890 import generate_kri_data

@pytest.fixture
def sample_dates():
    start_date = pd.to_datetime('2023-01-01')
    end_date = pd.to_datetime('2023-01-10')
    return start_date, end_date

def test_generate_kri_data_basic(sample_dates):
    start_date, end_date = sample_dates
    num_kris = 2
    baseline_values = [100, 50]
    volatility_factors = [0.05, 0.1]
    link_to_losses = False
    
    df = generate_kri_data(start_date, end_date, num_kris, baseline_values, volatility_factors, link_to_losses)
    
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 10 # 10 days of data
    assert len(df.columns) == num_kris + 1 # Date column + num_kris columns
    assert 'Date' in df.columns
    for i in range(num_kris):
        assert f'KRI_{i+1}' in df.columns

def test_generate_kri_data_empty_baseline_volatility(sample_dates):
    start_date, end_date = sample_dates
    num_kris = 2
    baseline_values = []
    volatility_factors = []
    link_to_losses = False
    
    df = generate_kri_data(start_date, end_date, num_kris, baseline_values, volatility_factors, link_to_losses)
    
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 10 # 10 days of data
    assert len(df.columns) == num_kris + 1 # Date column + num_kris columns
    assert 'Date' in df.columns
    for i in range(num_kris):
        assert f'KRI_{i+1}' in df.columns

def test_generate_kri_data_num_kris_zero(sample_dates):
    start_date, end_date = sample_dates
    num_kris = 0
    baseline_values = []
    volatility_factors = []
    link_to_losses = False
    
    df = generate_kri_data(start_date, end_date, num_kris, baseline_values, volatility_factors, link_to_losses)
    
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 10
    assert len(df.columns) == 1
    assert 'Date' in df.columns
    
def test_generate_kri_data_invalid_date_format():
    start_date = '2023-01-01'
    end_date = 123
    num_kris = 1
    baseline_values = [100]
    volatility_factors = [0.05]
    link_to_losses = False
    with pytest.raises(Exception): #Catching generic exception as we do not know what kind of exception will be raised by pandas.
        generate_kri_data(start_date, end_date, num_kris, baseline_values, volatility_factors, link_to_losses)

def test_generate_kri_data_unequal_baseline_volatility_length(sample_dates):
    start_date, end_date = sample_dates
    num_kris = 2
    baseline_values = [100]
    volatility_factors = [0.05, 0.1]
    link_to_losses = False

    df = generate_kri_data(start_date, end_date, num_kris, baseline_values, volatility_factors, link_to_losses)
    
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 10 # 10 days of data
    assert len(df.columns) == num_kris + 1 # Date column + num_kris columns
    assert 'Date' in df.columns
    for i in range(num_kris):
        assert f'KRI_{i+1}' in df.columns

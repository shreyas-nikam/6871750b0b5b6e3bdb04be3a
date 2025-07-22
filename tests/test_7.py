import pytest
import pandas as pd
from definition_ce2f3baa8ca1459098dc4a4f23ae2ec3 import calculate_risk_profile

@pytest.fixture
def mock_daily_data():
    # Create a basic DataFrame for testing
    data = {'Date': pd.to_datetime(['2024-01-01', '2024-01-02', '2024-01-03']),
            'Loss_Amount': [100, 200, 150],
            'KRI_Status': ['Green', 'Amber', 'Red']}
    return pd.DataFrame(data)

def test_calculate_risk_profile_basic(mock_daily_data):
    # Test with some data - check a dataframe is returned
    result = calculate_risk_profile(mock_daily_data[['Date', 'Loss_Amount']], mock_daily_data[['Date', 'KRI_Status']])
    assert isinstance(result, pd.DataFrame)

def test_calculate_risk_profile_empty_data():
    # Test with empty DataFrames
    empty_df = pd.DataFrame()
    result = calculate_risk_profile(empty_df, empty_df)
    assert isinstance(result, pd.DataFrame)  # Should still return a DataFrame

def test_calculate_risk_profile_missing_columns(mock_daily_data):
    # Test when Loss_Amount is missing
    with pytest.raises(KeyError):
        calculate_risk_profile(mock_daily_data[['Date']], mock_daily_data[['Date', 'KRI_Status']])

def test_calculate_risk_profile_non_numeric_losses(mock_daily_data):
     # Modify the dataframe to include non-numeric loss data
    mock_daily_data.loc[0, 'Loss_Amount'] = 'invalid'  # Introduce a string value

    with pytest.raises(TypeError):  # Expect a TypeError since calculation will fail
        calculate_risk_profile(mock_daily_data[['Date', 'Loss_Amount']], mock_daily_data[['Date', 'KRI_Status']])

def test_calculate_risk_profile_different_date_ranges():
    # Create two dataframes with different date ranges
    losses_data = {'Date': pd.to_datetime(['2024-01-01', '2024-01-02']), 'Loss_Amount': [100, 200]}
    kri_data = {'Date': pd.to_datetime(['2024-01-01', '2024-01-03']), 'KRI_Status': ['Green', 'Red']}
    losses_df = pd.DataFrame(losses_data)
    kri_df = pd.DataFrame(kri_data)

    result = calculate_risk_profile(losses_df, kri_df)
    assert isinstance(result, pd.DataFrame) # Check if result is returned despite date differences


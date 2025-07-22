import pytest
import pandas as pd
from definition_1dcdf7e0b0dd43bea76b6da169d81a01 import calculate_risk_capacity

@pytest.fixture
def mock_financial_data():
    return pd.DataFrame({
        'Revenue': [100, 110, 120],
        'Expenses': [80, 85, 90],
        'Profit': [20, 25, 30]
    })

def test_calculate_risk_capacity_nominal(mock_financial_data):
    capital_multiple = 0.15
    expected_capacity = mock_financial_data['Profit'].mean() * capital_multiple
    assert calculate_risk_capacity(mock_financial_data, capital_multiple) == expected_capacity

def test_calculate_risk_capacity_zero_multiple(mock_financial_data):
    capital_multiple = 0
    expected_capacity = mock_financial_data['Profit'].mean() * capital_multiple
    assert calculate_risk_capacity(mock_financial_data, capital_multiple) == expected_capacity

def test_calculate_risk_capacity_negative_multiple(mock_financial_data):
    capital_multiple = -0.1
    expected_capacity = mock_financial_data['Profit'].mean() * capital_multiple
    assert calculate_risk_capacity(mock_financial_data, capital_multiple) == expected_capacity

def test_calculate_risk_capacity_empty_dataframe():
    financial_data = pd.DataFrame({'Revenue': [], 'Expenses': [], 'Profit': []})
    capital_multiple = 0.15
    assert calculate_risk_capacity(financial_data, capital_multiple) == 0  # Assuming it returns 0 for empty data

def test_calculate_risk_capacity_non_dataframe():
    with pytest.raises(TypeError):
        calculate_risk_capacity([1, 2, 3], 0.15)

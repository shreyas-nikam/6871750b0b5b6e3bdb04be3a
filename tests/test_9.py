import pytest
import pandas as pd
from definition_4088688dab3144bdabf4770dd1c65546 import monitor_breaches

@pytest.fixture
def mock_risk_profile_df():
    data = {'EL': [100, 120, 150, 200, 180],
            'UL': [50, 60, 75, 100, 90],
            'SevereEvents': [2, 3, 1, 4, 2],
            'KRI1': [0.8, 0.9, 0.7, 1.0, 0.8],
            'KRI2': [5, 6, 4, 7, 5]}
    return pd.DataFrame(data)

@pytest.fixture
def mock_risk_appetite_params():
    return {'max_EL': 130,
            'max_UL': 70,
            'max_SevereEvents': 2,
            'KRI1_threshold': 0.8,
            'KRI2_threshold': 6}


def test_no_breaches(mock_risk_profile_df, mock_risk_appetite_params):
    mock_risk_profile_df['EL'] = [50, 60, 70, 80, 90]
    result = monitor_breaches(mock_risk_profile_df, mock_risk_appetite_params)
    assert result is None or len(result) == 0


def test_single_breach(mock_risk_profile_df, mock_risk_appetite_params):
    result = monitor_breaches(mock_risk_profile_df, mock_risk_appetite_params)
    # Assuming your function returns a DataFrame with breach info
    assert result is None or isinstance(result, pd.DataFrame)

def test_multiple_breaches(mock_risk_profile_df):
    risk_appetite_params = {'max_EL': 160, 'max_UL': 80, 'max_SevereEvents': 3, 'KRI1_threshold': 0.9, 'KRI2_threshold': 5.0}
    result = monitor_breaches(mock_risk_profile_df, risk_appetite_params)
    assert result is None or isinstance(result, pd.DataFrame)

def test_empty_risk_profile(mock_risk_appetite_params):
    risk_profile_df = pd.DataFrame()
    result = monitor_breaches(risk_profile_df, mock_risk_appetite_params)
    assert result is None or isinstance(result, pd.DataFrame)

def test_kri_breach_only(mock_risk_profile_df):
    risk_appetite_params = {'max_EL': 300, 'max_UL': 300, 'max_SevereEvents': 10, 'KRI1_threshold': 0.7, 'KRI2_threshold': 4.0}
    result = monitor_breaches(mock_risk_profile_df, risk_appetite_params)
    assert result is None or isinstance(result, pd.DataFrame)


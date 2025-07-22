import pytest
import pandas as pd
from definition_5ad2271421724e75bf416673d0f08b9f import monitor_risk_appetite


@pytest.fixture
def mock_df_risk_profile():
    # Create a sample risk profile DataFrame for testing
    data = {'AggregatedLoss': [100, 200, 300, 400, 500],
            'UnexpectedLoss': [50, 100, 150, 200, 250],
            'NumSevereLossEvents': [1, 2, 3, 4, 5],
            'KRI_1': [70, 80, 90, 100, 110],
            'KRI_2': [30, 40, 50, 60, 70]}
    return pd.DataFrame(data)

@pytest.fixture
def mock_risk_appetite_params():
    # Create a sample risk appetite parameter dictionary for testing
    return {
        'MaxExpectedLoss_Threshold': 350,
        'MaxUnexpectedLoss_Threshold': 175,
        'MaxSevereLossEvents_Threshold': 3,
        'KRI_1_Limit': 95,
        'KRI_2_Limit': 55,
        'RiskCapacity_Value': 600
    }

def test_monitor_risk_appetite_no_breaches(mock_df_risk_profile, mock_risk_appetite_params):
    # Modify data so that no breaches occur
    mock_df_risk_profile['AggregatedLoss'] = [50, 100, 150, 200, 250]
    mock_df_risk_profile['UnexpectedLoss'] = [25, 50, 75, 100, 125]
    mock_df_risk_profile['NumSevereLossEvents'] = [0, 1, 1, 2, 2]
    mock_df_risk_profile['KRI_1'] = [50, 60, 70, 80, 90]
    mock_df_risk_profile['KRI_2'] = [10, 20, 30, 40, 50]
    df_breaches, df_kri_status = monitor_risk_appetite(mock_df_risk_profile, mock_risk_appetite_params)
    assert isinstance(df_breaches, pd.DataFrame)
    assert isinstance(df_kri_status, pd.DataFrame)

def test_monitor_risk_appetite_with_breaches(mock_df_risk_profile, mock_risk_appetite_params):
    df_breaches, df_kri_status = monitor_risk_appetite(mock_df_risk_profile, mock_risk_appetite_params)
    assert isinstance(df_breaches, pd.DataFrame)
    assert isinstance(df_kri_status, pd.DataFrame)


def test_monitor_risk_appetite_empty_dataframe(mock_risk_appetite_params):
    empty_df = pd.DataFrame()
    df_breaches, df_kri_status = monitor_risk_appetite(empty_df, mock_risk_appetite_params)
    assert isinstance(df_breaches, pd.DataFrame)
    assert isinstance(df_kri_status, pd.DataFrame)


def test_monitor_risk_appetite_invalid_input_types(mock_df_risk_profile):
    risk_appetite_params = "invalid"
    with pytest.raises(TypeError):
        monitor_risk_appetite(mock_df_risk_profile, risk_appetite_params)

def test_monitor_risk_appetite_missing_columns(mock_risk_appetite_params):
    data = {'KRI_1': [70, 80, 90, 100, 110],
            'KRI_2': [30, 40, 50, 60, 70]}
    incomplete_df = pd.DataFrame(data)
    df_breaches, df_kri_status = monitor_risk_appetite(incomplete_df, mock_risk_appetite_params)
    assert isinstance(df_breaches, pd.DataFrame)
    assert isinstance(df_kri_status, pd.DataFrame)


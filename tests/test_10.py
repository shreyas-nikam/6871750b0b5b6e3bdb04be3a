import pytest
from definition_8cae3321b83f4a1eb95b73cf2cf364b1 import plot_time_series_metrics
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO


def test_plot_time_series_metrics_empty_dataframe():
    df = pd.DataFrame()
    metrics = ['metric1']
    title = 'Test Plot'
    y_label = 'Value'
    try:
        plot_time_series_metrics(df, metrics, title, y_label)
    except Exception as e:
        assert False, f"Plotting with an empty dataframe raised an exception {e}"


def test_plot_time_series_metrics_single_metric():
    data = {'Date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03']),
            'metric1': [1, 2, 3]}
    df = pd.DataFrame(data)
    metrics = ['metric1']
    title = 'Test Plot'
    y_label = 'Value'
    
    plot_time_series_metrics(df, metrics, title, y_label)
    assert True


def test_plot_time_series_metrics_multiple_metrics():
    data = {'Date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03']),
            'metric1': [1, 2, 3],
            'metric2': [4, 5, 6]}
    df = pd.DataFrame(data)
    metrics = ['metric1', 'metric2']
    title = 'Test Plot'
    y_label = 'Value'
    
    plot_time_series_metrics(df, metrics, title, y_label)
    assert True

def test_plot_time_series_metrics_missing_metric():
    data = {'Date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03']),
            'metric1': [1, 2, 3]}
    df = pd.DataFrame(data)
    metrics = ['metric1', 'metric2']
    title = 'Test Plot'
    y_label = 'Value'
    
    with pytest.raises(KeyError):
        plot_time_series_metrics(df, metrics, title, y_label)
        
def test_plot_time_series_metrics_non_datetime_index():
    data = {'index': [1, 2, 3],
            'metric1': [1, 2, 3]}
    df = pd.DataFrame(data).set_index('index')
    metrics = ['metric1']
    title = 'Test Plot'
    y_label = 'Value'
    
    with pytest.raises(TypeError):
        plot_time_series_metrics(df, metrics, title, y_label)

import pytest
import pandas as pd
from definition_9af62cb992534fa89275fe8c1fc31a46 import display_breach_summary_table

def test_display_breach_summary_table_empty_df(capsys):
    df = pd.DataFrame()
    display_breach_summary_table(df)
    captured = capsys.readouterr()
    assert captured.out == ""

def test_display_breach_summary_table_typical(capsys):
    data = {'Date': ['2024-01-01', '2024-01-02'],
            'Metric': ['Revenue', 'Losses'],
            'Actual Value': [1000, 500],
            'Threshold': [800, 400],
            'Status': ['OK', 'Breached']}
    df = pd.DataFrame(data)
    display_breach_summary_table(df)
    captured = capsys.readouterr()
    expected_output = "         Date   Metric  Actual Value  Threshold    Status\n0  2024-01-01  Revenue          1000        800        OK\n1  2024-01-02   Losses           500        400  Breached\n"
    assert captured.out == expected_output

def test_display_breach_summary_table_null_values(capsys):
    data = {'Date': ['2024-01-01', '2024-01-02'],
            'Metric': ['Revenue', 'Losses'],
            'Actual Value': [1000, None],
            'Threshold': [None, 400],
            'Status': ['OK', 'Breached']}
    df = pd.DataFrame(data)
    display_breach_summary_table(df)
    captured = capsys.readouterr()
    expected_output = "         Date   Metric  Actual Value  Threshold    Status\n0  2024-01-01  Revenue        1000.0        None        OK\n1  2024-01-02   Losses           NaN       400.0  Breached\n"
    assert captured.out == expected_output

def test_display_breach_summary_table_numeric_date(capsys):
    data = {'Date': [20240101, 20240102],
            'Metric': ['Revenue', 'Losses'],
            'Actual Value': [1000, 500],
            'Threshold': [800, 400],
            'Status': ['OK', 'Breached']}
    df = pd.DataFrame(data)
    display_breach_summary_table(df)
    captured = capsys.readouterr()
    expected_output = "       Date   Metric  Actual Value  Threshold    Status\n0  20240101  Revenue          1000        800        OK\n1  20240102   Losses           500        400  Breached\n"

    assert captured.out == expected_output

def test_display_breach_summary_table_mixed_data_types(capsys):
    data = {'Date': ['2024-01-01', '2024-01-02'],
            'Metric': [123, 'Losses'],
            'Actual Value': [1000, 500],
            'Threshold': [800, 400],
            'Status': ['OK', 'Breached']}
    df = pd.DataFrame(data)
    display_breach_summary_table(df)
    captured = capsys.readouterr()
    expected_output = "         Date Metric  Actual Value  Threshold    Status\n0  2024-01-01    123          1000        800        OK\n1  2024-01-02 Losses           500        400  Breached\n"

    assert captured.out == expected_output

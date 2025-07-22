import pytest
from definition_691b0c4d22f04ecb9ebf75efaedb6908 import generate_business_data
import pandas as pd
from datetime import datetime, timedelta

def is_valid_dataframe(df):
    if not isinstance(df, pd.DataFrame):
        return False
    if df.empty:
        return False
    if 'Revenue' not in df.columns or 'Expenses' not in df.columns or 'Profit' not in df.columns:
        return False
    return True

@pytest.mark.parametrize("start_date, end_date, avg_revenue, revenue_volatility, baseline_expenses, expected", [
    (datetime(2023, 1, 1), datetime(2023, 1, 5), 1000, 0.1, 500, True),  # Basic test
    (datetime(2023, 1, 1), datetime(2023, 1, 1), 1000, 0.1, 500, True),  # Single day
    (datetime(2023, 1, 1), datetime(2022, 12, 31), 1000, 0.1, 500, False), # Invalid date range
    (datetime(2023, 1, 1), datetime(2023, 1, 5), -1000, 0.1, 500, True), # Negative avg_revenue
    (datetime(2023, 1, 1), datetime(2023, 1, 5), 1000, -0.1, 500, True)  # Negative volatility
])
def test_generate_business_data(start_date, end_date, avg_revenue, revenue_volatility, baseline_expenses, expected):
    result = generate_business_data(start_date, end_date, avg_revenue, revenue_volatility, baseline_expenses)
    if expected:
        assert is_valid_dataframe(result)
        if is_valid_dataframe(result):
            assert len(result) == (end_date - start_date).days + 1
    else:
        assert result is None or not is_valid_dataframe(result)


import pytest
import pandas as pd
from definition_f65bbb37426a49ad88f74279e120f4a8 import validate_data

def test_validate_data_successful():
    df = pd.DataFrame({'col1': [1, 2, 3], 'col2': ['a', 'b', 'c'], 'col3': [1.1, 2.2, 3.3]})
    expected_columns = ['col1', 'col2', 'col3']
    expected_dtypes = {'col1': 'int64', 'col2': 'object', 'col3': 'float64'}
    critical_fields_no_na = ['col1', 'col2']
    pk_column = 'col1'
    try:
        validate_data(df, expected_columns, expected_dtypes, critical_fields_no_na, pk_column)
        assert True  # If no exception is raised, the validation was successful
    except Exception:
        assert False

def test_validate_data_missing_column():
    df = pd.DataFrame({'col1': [1, 2, 3], 'col2': ['a', 'b', 'c']})
    expected_columns = ['col1', 'col2', 'col3']
    expected_dtypes = {'col1': 'int64', 'col2': 'object', 'col3': 'float64'}
    critical_fields_no_na = ['col1', 'col2']
    pk_column = 'col1'
    with pytest.raises(ValueError, match="Missing expected columns: \['col3'\]"):
        validate_data(df, expected_columns, expected_dtypes, critical_fields_no_na, pk_column)

def test_validate_data_incorrect_dtype():
    df = pd.DataFrame({'col1': [1, 2, 3], 'col2': ['a', 'b', 'c'], 'col3': [1.1, 2.2, 3.3]})
    expected_columns = ['col1', 'col2', 'col3']
    expected_dtypes = {'col1': 'int64', 'col2': 'object', 'col3': 'int64'}
    critical_fields_no_na = ['col1', 'col2']
    pk_column = 'col1'
    with pytest.raises(TypeError, match="Incorrect dtype for column col3: expected int64, got float64"):
        validate_data(df, expected_columns, expected_dtypes, critical_fields_no_na, pk_column)

def test_validate_data_missing_values():
    df = pd.DataFrame({'col1': [1, 2, None], 'col2': ['a', None, 'c'], 'col3': [1.1, 2.2, 3.3]})
    expected_columns = ['col1', 'col2', 'col3']
    expected_dtypes = {'col1': 'int64', 'col2': 'object', 'col3': 'float64'}
    critical_fields_no_na = ['col1', 'col2']
    pk_column = 'col1'
    with pytest.raises(ValueError, match="Missing values found in critical fields: \['col1', 'col2'\]"):
        validate_data(df, expected_columns, expected_dtypes, critical_fields_no_na, pk_column)

def test_validate_data_duplicate_pk():
    df = pd.DataFrame({'col1': [1, 2, 2], 'col2': ['a', 'b', 'c'], 'col3': [1.1, 2.2, 3.3]})
    expected_columns = ['col1', 'col2', 'col3']
    expected_dtypes = {'col1': 'int64', 'col2': 'object', 'col3': 'float64'}
    critical_fields_no_na = ['col1', 'col2']
    pk_column = 'col1'
    with pytest.raises(ValueError, match="Primary key column col1 is not unique."):
        validate_data(df, expected_columns, expected_dtypes, critical_fields_no_na, pk_column)

import pytest
from modular.tables import normalize_table

def test_empty_input():
    data = []
    result = normalize_table(data)
    assert result['data'] == []
    assert result['header'] == []

def test_list_of_dicts():
    data = [
        {'name': 'John', 'age': 30, 'salary': 50000.123},
        {'name': 'Jane', 'age': 25, 'salary': 60000.456}
    ]
    
    # Test basic usage
    result = normalize_table(data)
    assert len(result['header']) == 3
    assert all(h in result['header'] for h in ['name', 'age', 'salary'])
    assert len(result['data']) == 2
    assert result['data'][0][result['header'].index('name')] == 'John'
    
    # Test ordered columns
    result = normalize_table(data, order=['name', 'salary', 'age'])
    assert result['header'] == ['name', 'salary', 'age']
    assert result['data'][0] == ['John', 50000.123, 30]
    
    # Test formatting
    result = normalize_table(data, cell_formats=['{:s}', '{:d}', '${:.2f}'])
    assert result['data'][0][2] == '$50000.12'
    assert result['data'][0][1] == '30'

def test_list_of_lists():
    data = [
        ['John', 30, 50000.123],
        ['Jane', 25, 60000.456]
    ]
    
    # Test basic usage
    result = normalize_table(data)
    assert result['header'] == ['0', '1', '2']
    assert result['data'] == data
    
    # Test custom headers
    custom_headers = ['Name', 'Age', 'Salary']
    result = normalize_table(data, header=custom_headers)
    assert result['header'] == custom_headers
    assert result['data'] == data
    
    # Test ordering with custom headers
    result = normalize_table(data, header=custom_headers, order=['Salary', 'Name', 'Age'])
    assert result['header'] == ['Salary', 'Name', 'Age']
    assert result['data'][0] == [50000.123, 'John', 30]

def test_missing_values():
    data = [
        {'name': 'John', 'age': 30},
        {'name': 'Jane', 'age': 25, 'salary': 60000.456}
    ]
    result = normalize_table(data)
    assert len(result['header']) == 3
    assert result['data'][0][result['header'].index('salary')] == ''

def test_formatting():
    data = [
        {'name': 'John', 'age': 30, 'salary': 50000.123},
        {'name': 'Jane', 'age': 25, 'salary': 60000.456}
    ]
    
    # Test number formatting
    result = normalize_table(
        data,
        cell_formats=['{:s}', '{:d}', '${:.2f}']
    )
    assert result['data'][0][2] == '$50000.12'
    assert result['data'][0][1] == '30'
    
    # Test default number format
    result = normalize_table(
        data,
        default_number_format='{:.3f}'
    )
    assert result['data'][0][2] == '50000.123' 
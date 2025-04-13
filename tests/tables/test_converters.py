import pytest
from modular.tables import normalize_table, delimited, markdown, rst

@pytest.fixture
def sample_table():
    data = [
        {'name': 'John', 'age': 30, 'salary': 50000},
        {'name': 'Jane', 'age': 25, 'salary': 60000}
    ]
    return normalize_table(data)

@pytest.fixture
def formatted_table():
    data = [
        {'name': 'John', 'age': 30, 'salary': 50000.123},
        {'name': 'Jane', 'age': 25, 'salary': 60000.456}
    ]
    return normalize_table(
        data,
        cell_formats=['{:s}', '{:d}', '${:.2f}']
    )

class TestDelimited:
    def test_basic(self, sample_table):
        result = delimited(sample_table)
        expected = "name,age,salary\nJohn,30,50000\nJane,25,60000\n"
        assert result == expected
    
    def test_custom_delimiter(self, sample_table):
        result = delimited(sample_table, delimiter='\t')
        expected = "name\tage\tsalary\nJohn\t30\t50000\nJane\t25\t60000\n"
        assert result == expected
    
    def test_empty(self):
        result = delimited(normalize_table([]))
        assert result == ""

class TestMarkdown:
    def test_basic(self, sample_table):
        result = markdown(sample_table)
        expected = (
            "| name | age | salary |\n"
            "| --- | --- | --- |\n"
            "| John | 30 | 50000 |\n"
            "| Jane | 25 | 60000 |\n"
        )
        assert result == expected
    
    def test_formatted(self, formatted_table):
        result = markdown(formatted_table)
        assert '$50000.12' in result
        assert '$60000.46' in result
    
    def test_empty(self):
        result = markdown(normalize_table([]))
        assert result == ""

class TestRST:
    def test_basic(self, sample_table):
        result = rst(sample_table)
        expected = (
            "+------+-----+--------+\n"
            "| name | age | salary |\n"
            "+======+=====+========+\n"
            "| John | 30  | 50000  |\n"
            "| Jane | 25  | 60000  |\n"
            "+------+-----+--------+\n"
        )
        assert result == expected
    
    def test_formatted(self, formatted_table):
        result = rst(formatted_table)
        assert '$50000.12' in result
        assert '$60000.46' in result
    
    def test_empty(self):
        result = rst(normalize_table([]))
        assert result == "" 
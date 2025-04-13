import pytest
from modular.tables import table, markdown, delimited, rst

@pytest.fixture
def sample_data():
    return [
        {'name': 'John', 'age': 30, 'salary': 50000},
        {'name': 'Jane', 'age': 25, 'salary': 60000}
    ]

class TestBuiltinFormatters:
    def test_markdown(self, sample_data):
        result = table(sample_data, formatter=markdown)
        expected = (
            "| name | age | salary |\n"
            "| --- | --- | --- |\n"
            "| John | 30 | 50000 |\n"
            "| Jane | 25 | 60000 |\n"
        )
        assert result == expected

    def test_delimited(self, sample_data):
        # Test CSV
        result = table(sample_data, formatter=delimited)
        expected = "name,age,salary\nJohn,30,50000\nJane,25,60000\n"
        assert result == expected
        
        # Test TSV
        tsv = lambda t: delimited(t, delimiter='\t')
        result = table(sample_data, formatter=tsv)
        expected = "name\tage\tsalary\nJohn\t30\t50000\nJane\t25\t60000\n"
        assert result == expected

    def test_rst(self, sample_data):
        result = table(sample_data, formatter=rst)
        expected = (
            "+------+-----+--------+\n"
            "| name | age | salary |\n"
            "+======+=====+========+\n"
            "| John | 30  | 50000  |\n"
            "| Jane | 25  | 60000  |\n"
            "+------+-----+--------+\n"
        )
        assert result == expected

class TestCustomFormatters:
    def test_html_formatter(self, sample_data):
        def html_formatter(table):
            if not table['data']:
                return ""
            
            html = "<table>\n"
            # Header row
            html += "  <tr>\n"
            for header in table['header']:
                html += f"    <th>{header}</th>\n"
            html += "  </tr>\n"
            # Data rows
            for row in table['data']:
                html += "  <tr>\n"
                for cell in row:
                    html += f"    <td>{cell}</td>\n"
                html += "  </tr>\n"
            html += "</table>"
            return html
        
        result = table(sample_data, formatter=html_formatter)
        expected = (
            "<table>\n"
            "  <tr>\n"
            "    <th>name</th>\n"
            "    <th>age</th>\n"
            "    <th>salary</th>\n"
            "  </tr>\n"
            "  <tr>\n"
            "    <td>John</td>\n"
            "    <td>30</td>\n"
            "    <td>50000</td>\n"
            "  </tr>\n"
            "  <tr>\n"
            "    <td>Jane</td>\n"
            "    <td>25</td>\n"
            "    <td>60000</td>\n"
            "  </tr>\n"
            "</table>"
        )
        assert result == expected

class TestTableOptions:
    def test_ordering_and_formatting(self):
        data = [
            {'name': 'John', 'age': 30, 'salary': 50000.123},
            {'name': 'Jane', 'age': 25, 'salary': 60000.456}
        ]
        
        result = table(
            data,
            formatter=markdown,
            order=['name', 'salary', 'age'],
            cell_formats=['{:s}', '${:.2f}', '{:d}']
        )
        
        expected = (
            "| name | salary | age |\n"
            "| --- | --- | --- |\n"
            "| John | $50000.12 | 30 |\n"
            "| Jane | $60000.46 | 25 |\n"
        )
        assert result == expected

    def test_empty_data(self):
        data = []
        
        assert table(data, formatter=markdown) == ""
        assert table(data, formatter=delimited) == ""
        assert table(data, formatter=rst) == "" 
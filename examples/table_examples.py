from modular.tables import table, markdown, delimited, rst

def run_examples():
    # Example data
    dict_data = [
        {'name': 'John', 'age': 30, 'salary': 50000.123},
        {'name': 'Jane', 'age': 25, 'salary': 60000.456}
    ]
    
    list_data = [
        ['John', 30, 50000.123],
        ['Jane', 25, 60000.456]
    ]

    print("=== Basic Usage ===")
    
    print("\nMarkdown Table:")
    print(table(dict_data, formatter=markdown))
    
    print("\nCSV Table:")
    print(table(dict_data, formatter=delimited))
    
    print("\nTSV Table:")
    print(table(dict_data, formatter=lambda t: delimited(t, delimiter='\t')))
    
    print("\nRST Table:")
    print(table(dict_data, formatter=rst))

    print("\n=== Advanced Features ===")
    
    print("\nOrdered Columns:")
    print(table(
        dict_data,
        formatter=markdown,
        order=['name', 'salary', 'age']
    ))
    
    print("\nFormatted Values:")
    print(table(
        dict_data,
        formatter=markdown,
        cell_formats=['{:s}', '{:d}', '${:.2f}']
    ))
    
    print("\nCustom Headers with List Data:")
    print(table(
        list_data,
        formatter=markdown,
        header=['Name', 'Age', 'Salary']
    ))
    
    print("\nCustom HTML Formatter:")
    def html_formatter(table):
        if not table['data']:
            return ""
        
        html = "<table>\n"
        html += "  <tr>\n"
        for header in table['header']:
            html += f"    <th>{header}</th>\n"
        html += "  </tr>\n"
        for row in table['data']:
            html += "  <tr>\n"
            for cell in row:
                html += f"    <td>{cell}</td>\n"
            html += "  </tr>\n"
        html += "</table>"
        return html
    
    print(table(dict_data, formatter=html_formatter))

if __name__ == '__main__':
    run_examples() 
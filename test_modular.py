from modular.tables import to_delimited, to_markdown, to_rst

# Example data as a list of dictionaries
data_dict = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "Los Angeles"},
    {"name": "Charlie", "age": 35, "city": "Chicago"}
]

# Example data as a list of lists
data_list = [
    ["Alice", 30, "New York"],
    ["Bob", 25, "Los Angeles"],
    ["Charlie", 35, "Chicago"]
]

print("=== CSV Format ===")
print(to_delimited(data_dict))
print("\n=== TSV Format ===")
print(to_delimited(data_list, delimiter='\t'))
print("\n=== Markdown Format ===")
print(to_markdown(data_dict))
print("\n=== reStructuredText Format ===")
print(to_rst(data_list)) 
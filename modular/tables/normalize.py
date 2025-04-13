from typing import List, Dict, Union, Optional, Any
import numbers

def normalize_table(
    data: Union[List[Dict[str, Any]], List[List[Any]]],
    header: Optional[List[str]] = None,
    order: Optional[List[str]] = None,
    cell_formats: Optional[List[str]] = None,
    default_number_format: str = "{:.2f}"
) -> Dict[str, List]:
    """
    Normalize different data formats into a consistent table structure with formatting options.
    
    Args:
        data: List of dictionaries or list of lists containing the table data
        header: Optional list of column names. If None and data is list of dicts,
               will use dict keys as header
        order: Optional list of column names/keys to specify column order
        cell_formats: Optional list of format strings to apply to each column
        default_number_format: Format string to apply to numeric values when no
                             cell_formats specified
    
    Returns:
        Dictionary with keys:
            'data': List of lists containing the normalized table data
            'header': List of column names
    """
    if not data:
        return {'data': [], 'header': []}
        
    # Handle list of dictionaries
    if isinstance(data[0], dict):
        if header is None:
            # Use all unique keys from all dictionaries as header
            header = list({key for d in data for key in d.keys()})
        
        if order:
            # Reorder header based on order parameter
            # Add any missing headers at the end
            header = [h for h in order if h in header] + [
                h for h in header if h not in order
            ]
            
        # Convert dicts to lists based on header order
        table_data = [
            [row.get(col, '') for col in header]
            for row in data
        ]
            
    # Handle list of lists
    else:
        if header is None:
            # Generate numeric headers
            header = [str(i) for i in range(len(data[0]))]
            
        if order:
            # Create mapping of header to index
            header_idx = {h: i for i, h in enumerate(header)}
            # Get new column order based on specified order
            col_order = [header_idx[h] for h in order if h in header_idx]
            # Add any missing columns at the end
            col_order.extend(i for i in range(len(header)) if i not in col_order)
            
            # Reorder headers and data
            header = [header[i] for i in col_order]
            table_data = [
                [row[i] for i in col_order]
                for row in data
            ]
        else:
            table_data = data
            
    # Apply formatting
    if cell_formats:
        # Ensure cell_formats matches number of columns
        formats = (cell_formats + [default_number_format] * len(header))[:len(header)]
        
        formatted_data = []
        for row in table_data:
            formatted_row = []
            for value, fmt in zip(row, formats):
                if isinstance(value, numbers.Number):
                    try:
                        formatted_row.append(fmt.format(value))
                    except ValueError:
                        formatted_row.append(default_number_format.format(value))
                else:
                    formatted_row.append(str(value))
            formatted_data.append(formatted_row)
        table_data = formatted_data
            
    return {
        'data': table_data,
        'header': header
    } 
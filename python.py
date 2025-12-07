def validate_number(input_str):
    try:
        
        return float(input_str)
    
    except ValueError:
        
        raise ValueError(f"'{input_str}' не является числом!")
    
def get_operation_symbol(operation):
    symbols = {
        'add': '+',
        'subtract': '-',
        'multiply': '*',
        'divide': '/'
 }
    return symbols.get(operation, operation)
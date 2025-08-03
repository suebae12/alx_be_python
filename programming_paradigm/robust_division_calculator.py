# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Safely divide two numbers with comprehensive error handling.
    
    Args:
        numerator: The number to be divided
        denominator: The number to divide by
        
    Returns:
        str: Result message or error message
    """
    try:
        # Convert inputs to float to handle both numeric strings and actual numbers
        num = float(numerator)
        den = float(denominator)
        
        # Perform division
        result = num / den
        
        return f"The result of the division is {result}"
        
    except ValueError:
        # Handle non-numeric inputs
        return "Error: Please enter numeric values only."
        
    except ZeroDivisionError:
        # Handle division by zero
        return "Error: Cannot divide by zero."

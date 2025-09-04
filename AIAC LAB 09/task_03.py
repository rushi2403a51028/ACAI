def generate_calculator_script(filename):
    """
    Generates a Python script with basic calculator functions: add, subtract, multiply, divide.

    Parameters
    ----------
    filename : str
        The name of the file to write the calculator script to.

    Returns
    -------
    None
    """
    script = '''"""
Calculator Module
=================
Provides basic arithmetic operations.
"""

def add(a, b):
    """
    Add two numbers.

    Parameters
    ----------
    a : float or int
        First number.
    b : float or int
        Second number.

    Returns
    -------
    float or int
        The sum of a and b.
    """
    return a + b

def subtract(a, b):
    """
    Subtract one number from another.

    Parameters
    ----------
    a : float or int
        Number to subtract from.
    b : float or int
        Number to subtract.

    Returns
    -------
    float or int
        The result of a - b.
    """
    return a - b

def multiply(a, b):
    """
    Multiply two numbers.

    Parameters
    ----------
    a : float or int
        First number.
    b : float or int
        Second number.

    Returns
    -------
    float or int
        The product of a and b.
    """
    return a * b

def divide(a, b):
    """
    Divide one number by another.

    Parameters
    ----------
    a : float or int
        Numerator.
    b : float or int
        Denominator.

    Returns
    -------
    float
        The result of a / b.

    Raises
    ------
    ValueError
        If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
'''

    with open(filename, 'w') as f:
        f.write(script)

# Main execution block
if __name__ == "__main__":
    import importlib.util
    import sys
    import os

    filename = "calculator_module.py"
    generate_calculator_script(filename)

    spec = importlib.util.spec_from_file_location("calculator_module", filename)
    calculator = importlib.util.module_from_spec(spec)
    sys.modules["calculator_module"] = calculator
    spec.loader.exec_module(calculator)

    print("add(2, 3) =", calculator.add(2, 3))
    print("subtract(5, 2) =", calculator.subtract(5, 2))
    print("multiply(4, 6) =", calculator.multiply(4, 6))
    try:
        print("divide(10, 2) =", calculator.divide(10, 2))
    except ValueError as e:
        print("Error:", e)
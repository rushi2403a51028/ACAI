"""
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

# Example usage
if __name__ == "__main__":
    print("add(2, 3) =", add(2, 3))
    print("subtract(5, 2) =", subtract(5, 2))
    print("multiply(4, 6) =", multiply(4, 6))
    try:
        print("divide(10, 2) =", divide(10, 2))
    except ValueError as e:
        print("Error:", e)
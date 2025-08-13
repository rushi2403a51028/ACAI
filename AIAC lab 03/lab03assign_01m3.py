def factorial(n):

    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
    # INSERT_YOUR_CODE
num = int(input("Enter a number to calculate factorial: "))
try:
    print(f"Factorial of {num} is {factorial(num)}")
except ValueError as e:
    print(f"Error: {e}")

def calculate(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b
    else:
        return None

# Example usage
a, b = 5, 3
operation = "multiply"

result = calculate(a, b, operation)
print(result)

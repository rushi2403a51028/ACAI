def get_factorial():
    """
    Collects input from user and generates factorial of the number.
    
    Returns:
        int or str: The factorial result or error message
    """
    # Collect input from user
    user_input = input("Enter a number to calculate factorial: ")
    
    try:
        # Convert input to integer
        number = int(user_input)
        
        # Check for negative numbers
        if number < 0:
            return "Error: Factorial is not defined for negative numbers"
        
        # Calculate factorial
        if number == 0:
            return 1
        
        factorial_result = 1
        for i in range(1, number + 1):
            factorial_result *= i
        
        return factorial_result
        
    except ValueError:
        return "Error: Please enter a valid integer"

# Test the function
if __name__ == "__main__":
    result = get_factorial()
    print(f"Factorial result: {result}")

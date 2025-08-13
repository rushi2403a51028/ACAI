# Basic Prompt Example:
# "Write Python code to convert temperature between Celsius and Fahrenheit."

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Example usage (basic prompt):
c = float(input("Enter temperature in Celsius: "))
print(f"{c}°C is {celsius_to_fahrenheit(c):.2f}°F")

f = float(input("Enter temperature in Fahrenheit: "))
print(f"{f}°F is {fahrenheit_to_celsius(f):.2f}°C")

print("\n---\n")

# Improved Prompt Example:
# "Write a Python program that allows the user to choose whether to convert from Celsius to Fahrenheit or Fahrenheit to Celsius, validates the input, and displays the result with two decimal places."

def convert_temperature():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Choose conversion (1 or 2): ")
    if choice == "1":
        temp_str = input("Enter temperature in Celsius: ")
        try:
            celsius = float(temp_str)
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius:.2f}°C is {fahrenheit:.2f}°F")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    elif choice == "2":
        temp_str = input("Enter temperature in Fahrenheit: ")
        try:
            fahrenheit = float(temp_str)
            celsius = (fahrenheit - 32) * 5/9
            print(f"{fahrenheit:.2f}°F is {celsius:.2f}°C")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    else:
        print("Invalid choice. Please select 1 or 2.")

# Example usage (improved prompt):
convert_temperature()

# Comparison and Explanation:
#
# The basic prompt leads to simple functions and direct input/output, but lacks user guidance, input validation, and flexibility.
# The improved prompt results in a user-friendly program: it lets the user choose the conversion direction, checks for valid input, and formats the output clearly.
# Being more specific in the prompt improves code quality by encouraging better user experience, error handling, and clarity.

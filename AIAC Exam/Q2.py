# Read a list of integers from user input
input_str = input("Enter a list of integers separated by commas: ")
input_list = [int(x.strip()) for x in input_str.strip('[]').split(',') if x.strip().isdigit()]

# Remove duplicates and sort the list
result = sorted(set(input_list))

print("Output =", result)
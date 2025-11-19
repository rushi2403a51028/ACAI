# Function using FOR loop
def print_multiples_for(number):
    print("Correct loopbased implementation using FOR loop: - task_2.py:3")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i} - task_2.py:5")

# Function using WHILE loop
def print_multiples_while(number):
    print("Correct loopbased implementation using WHILE loop: - task_2.py:9")
    i = 1
    while i <= 10:
        print(f"{number} x {i} = {number * i} - task_2.py:12")
        i += 1

# Input from user
num = int(input("Enter a number to generate its first 10 multiples: "))
# Call both functions
print_multiples_for(num)
print()  # Separator
print_multiples_while(num)

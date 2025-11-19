def sum_to_n_for(n):
    if n < 0:
        return "Invalid input. Please enter a non-negative integer."
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def sum_to_n_while(n):
    if n < 0:
        return "Invalid input. Please enter a non-negative integer."
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total

def sum_to_n_formula(n):
    if n < 0:
        return "Invalid input. Please enter a non-negative integer."
    return n * (n + 1) // 2

def sum_to_n_builtin(n):
    if n < 0:
        return "Invalid input. Please enter a non-negative integer."
    return sum(range(1, n + 1))

def main():
    try:
        n = int(input("Enter a non-negative integer: "))
        print("\nUsing for loop: - task_4.py:32")
        print(f"Sum of first {n} numbers: {sum_to_n_for(n)} - task_4.py:33")
        print("\nUsing while loop: - task_4.py:34")
        print(f"Sum of first {n} numbers: {sum_to_n_while(n)} - task_4.py:35")
        print("\nUsing formula: - task_4.py:36")
        print(f"Sum of first {n} numbers: {sum_to_n_formula(n)} - task_4.py:37")
        print("\nUsing builtin sum(): - task_4.py:38")
        print(f"Sum of first {n} numbers: {sum_to_n_builtin(n)} - task_4.py:39")
    except ValueError:
        print("Invalid input. Please enter a valid integer. - task_4.py:41")

main()

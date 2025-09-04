def sum_even_odd(numbers):
    """
    Calculates the sum of even and odd numbers in a given list.

    Args:
        numbers (list): List of integers provided by the user.

    Returns:
        tuple: A tuple containing (sum_of_even_numbers, sum_of_odd_numbers).
    """
    even_sum = 0
    odd_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    return even_sum, odd_sum

if __name__ == "__main__":
    user_input = input("Enter numbers separated by spaces: ")
    num_list = [int(x) for x in user_input.split()]
    even, odd = sum_even_odd(num_list)
    print(f"Sum of even numbers: {even}")
    print(f"Sum of odd numbers: {odd}")
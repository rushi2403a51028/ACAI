def sum_even_odd(numbers):
    """
    Calculates the sum of even and odd numbers in a list.

    Args:
        numbers (list[int]): A list of integers.

    Returns:
        tuple[int, int]: A tuple containing:
            - The sum of even numbers
            - The sum of odd numbers

    Example:
        >>> sum_even_odd([10, 15, 20, 25])
        (30, 40)
    """
    even_sum = sum(n for n in numbers if n % 2 == 0)
    odd_sum = sum(n for n in numbers if n % 2 != 0)
    return (even_sum, odd_sum)

# ✅ Call the function and print the result
if __name__ == "__main__":
    sample_list = [10, 15, 20, 25]
    result = sum_even_odd(sample_list)
    print("Sum of even numbers:", result[0])
    print("Sum of odd numbers:", result[1])
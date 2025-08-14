def sum_odd_even(numbers):
    odd_sum = 0
    even_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    return odd_sum, even_sum

# Example usage:
nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
odd_total, even_total = sum_odd_even(nums)
print(f"Sum of odd numbers: {odd_total}")
print(f"Sum of even numbers: {even_total}")
def get_and_sort_list():
    """
    Prompts the user to enter a list of integers separated by spaces,
    and returns the sorted list in ascending order.
    """
    user_input = input("Enter integers separated by spaces: ")
    try:
        int_list = [int(x) for x in user_input.strip().split()]
        return sorted(int_list)
    except ValueError:
        print("Error: Please enter only integers separated by spaces.")
        return []

# Example usage:
if __name__ == "__main__":
    sorted_list = get_and_sort_list()
    print("Sorted list:", sorted_list)

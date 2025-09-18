import re
import unittest

def is_palindrome(text: str) -> bool:
    """
    Determines if the input string is a palindrome, ignoring case and non-alphanumeric characters.

    Args:
        text (str): The input string to evaluate.

    Returns:
        bool: True if the cleaned string is a palindrome, False otherwise.
    """
    cleaned = re.sub(r'[^A-Za-z0-9]', '', text).lower()
    return cleaned == cleaned[::-1]

# 🔹 Manual input section
if __name__ == "__main__":
    user_input = input("Enter a string to check for palindrome: ")
    result = is_palindrome(user_input)
    print(f"Is palindrome? {result}")

    # 🔹 Run tests
    print("\nRunning unit tests...\n")
    class TestIsPalindrome(unittest.TestCase):
        def test_classic_palindrome(self):
            self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))

        def test_non_palindrome(self):
            self.assertFalse(is_palindrome("hello"))

        def test_empty_string(self):
            self.assertTrue(is_palindrome(""))

        def test_numeric_palindrome(self):
            self.assertTrue(is_palindrome("12321"))

        def test_mixed_case_and_symbols(self):
            self.assertTrue(is_palindrome("No 'x' in Nixon"))

        def test_only_symbols(self):
            self.assertTrue(is_palindrome("!!!@@@###"))  # becomes empty → True

        def test_single_character(self):
            self.assertTrue(is_palindrome("Z"))

    unittest.main(argv=[''], exit=False)
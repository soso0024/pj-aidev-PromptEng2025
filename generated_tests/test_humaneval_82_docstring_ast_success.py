# Test cases for HumanEval/82
# Generated using Claude API


def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    l = len(string)
    if l == 0 or l == 1:
        return False
    for i in range(2, l):
        if l % i == 0:
            return False
    return True


# Generated test cases:
import pytest

@pytest.mark.parametrize("input_str,expected", [
    ("Hello", True),      # length 5 (prime)
    ("abcdcba", True),    # length 7 (prime)
    ("kittens", True),    # length 7 (prime)
    ("orange", False),    # length 6 (not prime)
    ("", False),          # length 0 (edge case)
    ("a", False),         # length 1 (edge case)
    ("ab", True),         # length 2 (prime)
    ("abc", True),        # length 3 (prime)
    ("abcd", False),      # length 4 (not prime)
    ("pneumonoultramicroscopicsilicovolcanoconiosis", False),  # length 45 (not prime)
    ("aaa", True),        # length 3 (prime)
    ("abcdef", False),    # length 6 (not prime)
    ("test", False),      # length 4 (not prime)
])
def test_prime_length(input_str, expected):
    assert prime_length(input_str) == expected

def test_prime_length_with_spaces():
    assert prime_length("   ") == True  # length 3 (prime)
    assert prime_length(" ") == False   # length 1 (not prime)
    assert prime_length("  ") == True   # length 2 (prime)

def test_prime_length_with_special_chars():
    assert prime_length("!@#") == True      # length 3 (prime)
    assert prime_length("!@#$") == False    # length 4 (not prime)
    assert prime_length("!@#$%") == True    # length 5 (prime)

def test_prime_length_with_numbers():
    assert prime_length("123") == True       # length 3 (prime)
    assert prime_length("1234") == False     # length 4 (not prime)
    assert prime_length("12345") == True     # length 5 (prime)

def test_prime_length_with_mixed_content():
    assert prime_length("a1!") == True       # length 3 (prime)
    assert prime_length("a1!@") == False     # length 4 (not prime)
    assert prime_length("a1!@#") == True     # length 5 (prime)

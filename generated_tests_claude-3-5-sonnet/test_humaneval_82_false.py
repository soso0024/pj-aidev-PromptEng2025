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
    ("", False),  # empty string
    ("a", False),  # single character
    ("ab", True),  # length 2 (prime)
    ("abc", True),  # length 3 (prime)
    ("abcd", False),  # length 4 (not prime)
    ("abcde", True),  # length 5 (prime)
    ("abcdef", False),  # length 6 (not prime)
    ("abcdefg", True),  # length 7 (prime)
    ("abcdefgh", False),  # length 8 (not prime)
    ("abcdefghi", False),  # length 9 (not prime)
    ("abcdefghijk", True),  # length 11 (prime)
    ("Hello World!", False),  # length 12 (not prime)
    ("This is a test", False),  # length 14 (not prime)
    ("!@#$%^&*()", False),  # length 10 (not prime)
    ("   ", True),  # length 3 (prime) with spaces
    ("\n\n", True),  # length 2 (prime) with newlines
    ("🌟🌟🌟", True),  # length 3 (prime) with emojis
    ("12345", True),  # length 5 (prime) with numbers
])
def test_prime_length(input_str, expected):
    assert prime_length(input_str) == expected

def test_prime_length_with_none():
    with pytest.raises(TypeError):
        prime_length(None)

def test_prime_length_with_non_string():
    with pytest.raises(TypeError):
        prime_length(123)
    with pytest.raises(TypeError):
        prime_length(['a', 'b', 'c'])
    with pytest.raises(TypeError):
        prime_length({'key': 'value'})
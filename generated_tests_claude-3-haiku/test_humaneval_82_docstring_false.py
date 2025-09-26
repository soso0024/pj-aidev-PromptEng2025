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
from prime_length import prime_length
import pytest

@pytest.mark.parametrize("input,expected", [
    ("Hello", True),
    ("abcdcba", True),
    ("kittens", True),
    ("orange", False),
    ("", False),
    ("a", False),
    ("12345", True),
    ("hello world", False),
])
def test_prime_length(input, expected):
    assert prime_length(input) == expected

def test_prime_length_type_error():
    with pytest.raises(TypeError):
        prime_length(123)
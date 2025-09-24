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

@pytest.mark.parametrize("input,expected", [
    ("", False),
    ("a", False),
    ("abc", True),
    ("abcd", False),
    ("hello", False),
    ("prime", True),
    ("12345", False),
    ("123456", False),
    ("1", False),
    (123, TypeError),
    (None, TypeError)
])
def test_prime_length(input, expected):
    if expected is TypeError:
        with pytest.raises(TypeError):
            prime_length(input)
    else:
        assert prime_length(str(input)) == expected

def prime_length(string):
    l = len(str(string))
    if l <= 1:
        return False
    for i in range(2, int(l ** 0.5) + 1):
        if l % i == 0:
            return False
    return True
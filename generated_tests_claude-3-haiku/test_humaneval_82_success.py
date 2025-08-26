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

def test_prime_length_empty_string():
    assert prime_length("") == False

def test_prime_length_single_char_string():
    assert prime_length("a") == False

@pytest.mark.parametrize("input,expected", [
    ("test", False),
    ("another", True),
    ("prime", True),
    ("composite", False),
    ("abcdef", False),
    ("abcd", False)
])
def test_prime_length_normal_cases(input, expected):
    assert prime_length(input) == expected

def test_prime_length_non_string_input():
    with pytest.raises(TypeError):
        prime_length(123)

def prime_length(string):
    l = len(string)
    if l <= 1:
        return False
    for i in range(2, l):
        if l % i == 0:
            return False
    return True
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
    ("prime", True),
    ("composite", False),
    ("abcdef", False),
    ("123456", False),
    ("a1b2c3", False),
    ("   ", True),
    ("\t\n\r", True),
    ("!@#$%^&*", False)
])
def test_prime_length_various_inputs(input, expected):
    assert prime_length(input) == expected

def test_prime_length_negative_integer():
    with pytest.raises(TypeError):
        prime_length(-5)

def test_prime_length_float_input():
    with pytest.raises(TypeError):
        prime_length(3.14)

def test_prime_length_list_input():
    with pytest.raises(TypeError):
        prime_length([1, 2, 3])

def test_prime_length_dict_input():
    with pytest.raises(TypeError):
        prime_length({"a": 1, "b": 2})
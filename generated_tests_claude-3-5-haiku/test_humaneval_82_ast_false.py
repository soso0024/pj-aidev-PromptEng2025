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

def test_prime_length_single_char():
    assert prime_length("a") == False

def test_prime_length_prime_length_strings():
    assert prime_length("ab") == False
    assert prime_length("abc") == True
    assert prime_length("abcd") == False
    assert prime_length("abcde") == True
    assert prime_length("abcdef") == False

def test_prime_length_longer_strings():
    assert prime_length("abcdefg") == True
    assert prime_length("abcdefgh") == False
    assert prime_length("abcdefghi") == False
    assert prime_length("abcdefghij") == False
    assert prime_length("abcdefghijk") == True

@pytest.mark.parametrize("input_string,expected", [
    ("", False),
    ("a", False),
    ("ab", False),
    ("abc", True),
    ("abcd", False),
    ("abcde", True),
    ("hello", False),
    ("python", False),
    ("programming", False)
])
def test_prime_length_parametrized(input_string, expected):
    assert prime_length(input_string) == expected
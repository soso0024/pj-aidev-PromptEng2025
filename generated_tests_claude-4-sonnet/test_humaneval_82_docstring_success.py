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

def prime_length(string):
    l = len(string)
    if l == 0 or l == 1:
        return False
    for i in range(2, l):
        if l % i == 0:
            return False
    return True

@pytest.mark.parametrize("input_string,expected", [
    ("Hello", True),
    ("abcdcba", True),
    ("kittens", True),
    ("orange", False),
    ("", False),
    ("a", False),
    ("ab", True),
    ("abc", True),
    ("abcd", False),
    ("abcde", True),
    ("abcdef", False),
    ("abcdefg", True),
    ("abcdefgh", False),
    ("abcdefghi", False),
    ("abcdefghij", False),
    ("abcdefghijk", True),
    ("abcdefghijkl", False),
    ("abcdefghijklm", True),
    ("abcdefghijklmn", False),
    ("abcdefghijklmno", False),
    ("abcdefghijklmnop", False),
    ("abcdefghijklmnopq", True),
    ("abcdefghijklmnopqr", False),
    ("abcdefghijklmnopqrs", True),
    ("x" * 2, True),
    ("x" * 3, True),
    ("x" * 4, False),
    ("x" * 5, True),
    ("x" * 6, False),
    ("x" * 7, True),
    ("x" * 8, False),
    ("x" * 9, False),
    ("x" * 10, False),
    ("x" * 11, True),
    ("x" * 12, False),
    ("x" * 13, True),
    ("x" * 17, True),
    ("x" * 19, True),
    ("x" * 23, True),
    ("x" * 29, True),
    ("x" * 31, True),
    ("123", True),
    ("1234", False),
    ("12345", True),
    ("!@#$%", True),
    ("!@#$", False),
    ("   ", True),
    ("  ", True),
    (" ", False),
    ("\n\t\r", True),
    ("\n\t", True),
    ("special chars !@#$%^&*()", False),
    ("unicode: αβγδε", False),
    ("mixed123ABC", True),
])
def test_prime_length(input_string, expected):
    assert prime_length(input_string) == expected

def test_prime_length_empty_string():
    assert prime_length("") == False

def test_prime_length_single_char():
    assert prime_length("a") == False

def test_prime_length_two_chars():
    assert prime_length("ab") == True

def test_prime_length_large_prime():
    large_string = "x" * 97
    assert prime_length(large_string) == True

def test_prime_length_large_composite():
    large_string = "x" * 100
    assert prime_length(large_string) == False

def test_prime_length_whitespace():
    assert prime_length("   ") == True
    assert prime_length("    ") == False

def test_prime_length_newlines():
    assert prime_length("\n\n") == True
    assert prime_length("\n\n\n\n") == False

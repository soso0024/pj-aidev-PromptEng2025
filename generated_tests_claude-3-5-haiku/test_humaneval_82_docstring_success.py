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

def test_prime_length_true_cases():
    assert prime_length('Hello') == True
    assert prime_length('abcdcba') == True
    assert prime_length('kittens') == True

def test_prime_length_false_cases():
    assert prime_length('orange') == False
    assert prime_length('python') == False

def test_prime_length_edge_cases():
    assert prime_length('') == False
    assert prime_length('a') == False

@pytest.mark.parametrize("input_string,expected", [
    ('Hello', True),
    ('abcdcba', True),
    ('kittens', True),
    ('orange', False),
    ('python', False),
    ('', False),
    ('a', False)
])
def test_prime_length_parametrized(input_string, expected):
    assert prime_length(input_string) == expected

def test_prime_length_long_prime_string():
    assert prime_length('x' * 11) == True
    assert prime_length('x' * 13) == True

def test_prime_length_long_non_prime_string():
    assert prime_length('x' * 12) == False
    assert prime_length('x' * 15) == False

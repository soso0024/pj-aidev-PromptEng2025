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

def test_prime_length_normal_cases():
    assert prime_length('Hello') == True
    assert prime_length('abcdcba') == True
    assert prime_length('kittens') == True
    assert prime_length('orange') == False

def test_prime_length_edge_cases():
    assert prime_length('') == False
    assert prime_length('a') == False
    assert prime_length('ab') == False
    assert prime_length('abc') == True

@pytest.mark.parametrize("input_string,expected", [
    ('Hello', True),
    ('abcdcba', True),
    ('kittens', True),
    ('orange', False),
    ('', False),
    ('a', False),
    ('ab', False),
    ('abc', True),
    ('programming', True),
    ('python', False)
])
def test_prime_length_parametrized(input_string, expected):
    assert prime_length(input_string) == expected

def test_prime_length_type_error():
    with pytest.raises(TypeError):
        prime_length(123)
        prime_length(None)
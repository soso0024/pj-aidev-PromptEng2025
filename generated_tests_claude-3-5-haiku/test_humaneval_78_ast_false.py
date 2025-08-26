# Test cases for HumanEval/78
# Generated using Claude API


def hex_key(num):
    """You have been tasked to write a function that receives 
    a hexadecimal number as a string and counts the number of hexadecimal 
    digits that are primes (prime number, or a prime, is a natural number 
    greater than 1 that is not a product of two smaller natural numbers).
    Hexadecimal digits are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F.
    Prime numbers are 2, 3, 5, 7, 11, 13, 17,...
    So you have to determine a number of the following digits: 2, 3, 5, 7, 
    B (=decimal 11), D (=decimal 13).
    Note: you may assume the input is always correct or empty string, 
    and symbols A,B,C,D,E,F are always uppercase.
    Examples:
    For num = "AB" the output should be 1.
    For num = "1077E" the output should be 2.
    For num = "ABED1A33" the output should be 4.
    For num = "123456789ABCDEF0" the output should be 6.
    For num = "2020" the output should be 2.
    """

    primes = ('2', '3', '5', '7', 'B', 'D')
    total = 0
    for i in range(0, len(num)):
        if num[i] in primes:
            total += 1
    return total


# Generated test cases:
import pytest

def test_hex_key_normal_cases():
    assert hex_key('2') == 1
    assert hex_key('3') == 1
    assert hex_key('5') == 1
    assert hex_key('7') == 1
    assert hex_key('B') == 1
    assert hex_key('D') == 1

def test_hex_key_multiple_primes():
    assert hex_key('23') == 2
    assert hex_key('57') == 2
    assert hex_key('BD') == 2

def test_hex_key_mixed_characters():
    assert hex_key('123') == 1
    assert hex_key('A2B') == 2
    assert hex_key('C5D7') == 2

def test_hex_key_no_primes():
    assert hex_key('14689ACE') == 0
    assert hex_key('') == 0

@pytest.mark.parametrize("input_str,expected", [
    ('2', 1),
    ('3', 1),
    ('5', 1),
    ('7', 1),
    ('B', 1),
    ('D', 1),
    ('23', 2),
    ('57', 2),
    ('BD', 2),
    ('123', 1),
    ('A2B', 2),
    ('C5D7', 2),
    ('14689ACE', 0),
    ('', 0)
])
def test_hex_key_parametrized(input_str, expected):
    assert hex_key(input_str) == expected
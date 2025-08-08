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
from your_module import hex_key
import pytest

@pytest.mark.parametrize("num,expected", [
    ("AB", 1),
    ("1077E", 2),
    ("ABED1A33", 4),
    ("123456789ABCDEF0", 6),
    ("2020", 2),
    ("", 0),
    ("0", 0),
    ("AAAAA", 0),
    ("BBBBB", 5),
    ("DDDDD", 5),
])
def test_hex_key(num, expected):
    assert hex_key(num) == expected

def test_hex_key_invalid_input():
    with pytest.raises(TypeError):
        hex_key(123)
    with pytest.raises(TypeError):
        hex_key(None)
    with pytest.raises(ValueError):
        hex_key("abc123")
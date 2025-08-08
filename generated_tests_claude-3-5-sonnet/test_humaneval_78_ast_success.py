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

def test_hex_key_empty_string():
    assert hex_key("") == 0

def test_hex_key_no_primes():
    assert hex_key("14689ACE") == 0

def test_hex_key_all_primes():
    assert hex_key("2357BD") == 6

@pytest.mark.parametrize("input_str,expected", [
    ("123", 2),
    ("ABC", 1),
    ("2B3D", 4),
    ("ABCD", 2),
    ("0123456789ABCDEF", 6),
    ("FF", 0),
    ("22", 2),
    ("BD", 2),
    ("0000", 0),
    ("2222", 4),
    ("abcd", 0),
    ("2B3D5", 5)
])
def test_hex_key_various_inputs(input_str, expected):
    assert hex_key(input_str) == expected

def test_hex_key_mixed_case():
    assert hex_key("2b3d") == 2

def test_hex_key_single_char():
    assert hex_key("2") == 1
    assert hex_key("A") == 0

@pytest.mark.parametrize("invalid_input", [
    None,
    123,
    2.5
])
def test_hex_key_invalid_inputs(invalid_input):
    with pytest.raises((TypeError, AttributeError)):
        hex_key(invalid_input)

def test_hex_key_special_chars():
    result = hex_key("\n\t")
    assert result == 0

def test_hex_key_unicode():
    assert hex_key("2357") == 4
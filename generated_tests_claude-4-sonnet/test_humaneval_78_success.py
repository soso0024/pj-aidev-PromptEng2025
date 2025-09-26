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

def hex_key(num):
    primes = ('2', '3', '5', '7', 'B', 'D')
    total = 0
    for i in range(0, len(num)):
        if num[i] in primes:
            total += 1
    return total

@pytest.mark.parametrize("input_str,expected", [
    ("", 0),
    ("123", 2),
    ("2357BD", 6),
    ("ABCDEF", 2),
    ("0189ACE", 0),
    ("222", 3),
    ("BBB", 3),
    ("2B", 2),
    ("1", 0),
    ("A", 0),
    ("2", 1),
    ("3", 1),
    ("5", 1),
    ("7", 1),
    ("B", 1),
    ("D", 1),
    ("F", 0),
    ("0", 0),
    ("4", 0),
    ("6", 0),
    ("8", 0),
    ("9", 0),
    ("C", 0),
    ("E", 0),
    ("23456789ABCDEF", 6),
    ("FEDCBA9876543210", 6),
    ("2357BD2357BD", 12),
    ("abcdef", 0),
    ("2b3d5", 3),
])
def test_hex_key_parametrized(input_str, expected):
    assert hex_key(input_str) == expected

def test_hex_key_empty_string():
    assert hex_key("") == 0

def test_hex_key_single_prime():
    assert hex_key("2") == 1
    assert hex_key("3") == 1
    assert hex_key("5") == 1
    assert hex_key("7") == 1
    assert hex_key("B") == 1
    assert hex_key("D") == 1

def test_hex_key_single_non_prime():
    assert hex_key("0") == 0
    assert hex_key("1") == 0
    assert hex_key("4") == 0
    assert hex_key("6") == 0
    assert hex_key("8") == 0
    assert hex_key("9") == 0
    assert hex_key("A") == 0
    assert hex_key("C") == 0
    assert hex_key("E") == 0
    assert hex_key("F") == 0

def test_hex_key_all_primes():
    assert hex_key("2357BD") == 6

def test_hex_key_no_primes():
    assert hex_key("0189ACEF") == 0

def test_hex_key_mixed():
    assert hex_key("AB2CD3") == 4
    assert hex_key("123456789ABCDEF") == 6

def test_hex_key_repeated_primes():
    assert hex_key("2222") == 4
    assert hex_key("BBBB") == 4
    assert hex_key("2B2B") == 4

def test_hex_key_case_sensitivity():
    assert hex_key("b") == 0
    assert hex_key("d") == 0
    assert hex_key("B") == 1
    assert hex_key("D") == 1

def test_hex_key_long_string():
    long_string = "2357BD" * 100
    assert hex_key(long_string) == 600

def test_hex_key_type_error():
    with pytest.raises(TypeError):
        hex_key(123)
    
    with pytest.raises(TypeError):
        hex_key(None)
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

@pytest.mark.parametrize("num,expected", [
    ("AB", 1),
    ("1077E", 2),
    ("ABED1A33", 4),
    ("123456789ABCDEF0", 6),
    ("2020", 2),
    ("", 0),
    ("0", 0),
    ("1", 0),
    ("2", 1),
    ("3", 1),
    ("4", 0),
    ("5", 1),
    ("6", 0),
    ("7", 1),
    ("8", 0),
    ("9", 0),
    ("A", 0),
    ("B", 1),
    ("C", 0),
    ("D", 1),
    ("E", 0),
    ("F", 0),
    ("2357BD", 6),
    ("014689ACEF", 0),
    ("22222", 5),
    ("33333", 5),
    ("55555", 5),
    ("77777", 5),
    ("BBBBB", 5),
    ("DDDDD", 5),
    ("AAAAAAA", 0),
    ("CCCCCCC", 0),
    ("EEEEEEE", 0),
    ("FFFFFFF", 0),
    ("0000000", 0),
    ("1111111", 0),
    ("4444444", 0),
    ("6666666", 0),
    ("8888888", 0),
    ("9999999", 0),
    ("2B", 2),
    ("3D", 2),
    ("57", 2),
    ("BD", 2),
    ("23", 2),
    ("35", 2),
    ("75", 2),
    ("B7", 2),
    ("D2", 2),
    ("2357BDACEF014689", 6),
    ("FEDCBA9876543210", 6),
    ("0123456789ABCDEF", 6)
])
def test_hex_key(num, expected):
    assert hex_key(num) == expected

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
    assert hex_key("014689ACEF") == 0

def test_hex_key_mixed_long():
    assert hex_key("123456789ABCDEF0123456789ABCDEF0") == 12

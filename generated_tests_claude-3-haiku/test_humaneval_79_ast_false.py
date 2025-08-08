# Test cases for HumanEval/79
# Generated using Claude API


def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    """

    return "db" + bin(decimal)[2:] + "db"


# Generated test cases:
import pytest

def test_decimal_to_binary_positive():
    assert decimal_to_binary(42) == 'db101010db'
    assert decimal_to_binary(0) == 'db0db'
    assert decimal_to_binary(255) == 'db11111111db'

def test_decimal_to_binary_negative():
    assert decimal_to_binary(-1) == 'db-1db'
    assert decimal_to_binary(-42) == 'db-101010db'

def test_decimal_to_binary_float():
    with pytest.raises(TypeError):
        decimal_to_binary(3.14)

def test_decimal_to_binary_string():
    with pytest.raises(TypeError):
        decimal_to_binary('42')

@pytest.mark.parametrize("input,expected", [
    (42, 'db101010db'),
    (0, 'db0db'),
    (255, 'db11111111db'),
    (-1, 'db-1db'),
    (-42, 'db-101010db')
])
def test_decimal_to_binary_parametrized(input, expected):
    assert decimal_to_binary(input) == expected

def decimal_to_binary(decimal):
    return "db" + bin(decimal)[2:] + "db"
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

def test_decimal_to_binary_positive_number():
    assert decimal_to_binary(10) == 'db1010db'
    assert decimal_to_binary(7) == 'db111db'
    assert decimal_to_binary(15) == 'db1111db'

def test_decimal_to_binary_zero():
    assert decimal_to_binary(0) == 'db0db'

def test_decimal_to_binary_large_number():
    assert decimal_to_binary(255) == 'db11111111db'
    assert decimal_to_binary(1024) == 'db10000000000db'

@pytest.mark.parametrize("decimal,expected", [
    (10, 'db1010db'),
    (7, 'db111db'),
    (0, 'db0db'),
    (255, 'db11111111db'),
    (1024, 'db10000000000db')
])
def test_decimal_to_binary_parametrized(decimal, expected):
    assert decimal_to_binary(decimal) == expected

def test_decimal_to_binary_negative_number():
    with pytest.raises(ValueError, match="Decimal must be a non-negative integer"):
        decimal_to_binary(-5)

def test_decimal_to_binary_non_integer():
    with pytest.raises(TypeError, match="Decimal must be an integer"):
        decimal_to_binary(3.14)
    with pytest.raises(TypeError, match="Decimal must be an integer"):
        decimal_to_binary('10')
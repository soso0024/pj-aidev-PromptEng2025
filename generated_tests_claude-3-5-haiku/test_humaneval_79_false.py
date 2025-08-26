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
    assert decimal_to_binary(10) == "db1010db"
    assert decimal_to_binary(0) == "db0db"
    assert decimal_to_binary(255) == "db11111111db"

def test_decimal_to_binary_negative_number():
    assert decimal_to_binary(-10) == "db-1010db"
    assert decimal_to_binary(-255) == "db-11111111db"

@pytest.mark.parametrize("decimal,expected", [
    (0, "db0db"),
    (1, "db1db"),
    (2, "db10db"),
    (10, "db1010db"),
    (15, "db1111db"),
    (16, "db10000db"),
    (255, "db11111111db"),
    (-1, "db-1db"),
    (-10, "db-1010db"),
    (-255, "db-11111111db")
])
def test_decimal_to_binary_parametrized(decimal, expected):
    assert decimal_to_binary(decimal) == expected

def test_decimal_to_binary_large_number():
    assert decimal_to_binary(1024) == "db10000000000db"

def test_decimal_to_binary_type_error():
    with pytest.raises(TypeError):
        decimal_to_binary("not a number")

def test_decimal_to_binary_float():
    with pytest.raises(TypeError):
        decimal_to_binary(3.14)
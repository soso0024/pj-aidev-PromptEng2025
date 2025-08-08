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

def test_decimal_to_binary_basic():
    assert decimal_to_binary(15) == "db1111db"
    assert decimal_to_binary(32) == "db100000db"

def test_decimal_to_binary_zero():
    assert decimal_to_binary(0) == "db0db"

def test_decimal_to_binary_one():
    assert decimal_to_binary(1) == "db1db"

@pytest.mark.parametrize("decimal,expected", [
    (7, "db111db"),
    (10, "db1010db"),
    (64, "db1000000db"),
    (100, "db1100100db"),
    (255, "db11111111db"),
    (512, "db1000000000db")
])
def test_decimal_to_binary_various_numbers(decimal, expected):
    assert decimal_to_binary(decimal) == expected

def test_decimal_to_binary_large_number():
    assert decimal_to_binary(1000000) == "db11110100001001000000db"

@pytest.mark.parametrize("decimal", [-1, -15, -32])
def test_decimal_to_binary_negative_numbers(decimal):
    with pytest.raises(ValueError):
        decimal_to_binary(decimal)

def test_decimal_to_binary_format():
    result = decimal_to_binary(42)
    assert result.startswith("db")
    assert result.endswith("db")
    assert all(c in "01" for c in result[2:-2])

@pytest.mark.parametrize("invalid_input", [
    "string",
    None,
    [],
    {},
    3.14
])
def test_decimal_to_binary_invalid_input(invalid_input):
    with pytest.raises((TypeError, ValueError)):
        decimal_to_binary(invalid_input)
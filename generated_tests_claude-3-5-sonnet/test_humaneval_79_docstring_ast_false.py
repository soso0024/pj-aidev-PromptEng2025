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

def test_decimal_to_binary_zero():
    assert decimal_to_binary(0) == "db0db"

def test_decimal_to_binary_one():
    assert decimal_to_binary(1) == "db1db"

def test_decimal_to_binary_power_of_two():
    assert decimal_to_binary(2) == "db10db"
    assert decimal_to_binary(4) == "db100db"
    assert decimal_to_binary(8) == "db1000db"
    assert decimal_to_binary(16) == "db10000db"
    assert decimal_to_binary(32) == "db100000db"

def test_decimal_to_binary_fifteen():
    assert decimal_to_binary(15) == "db1111db"

@pytest.mark.parametrize("decimal,expected", [
    (0, "db0db"),
    (1, "db1db"),
    (2, "db10db"),
    (3, "db11db"),
    (7, "db111db"),
    (10, "db1010db"),
    (42, "db101010db"),
    (100, "db1100100db"),
    (255, "db11111111db"),
    (1000, "db1111101000db")
])
def test_decimal_to_binary_various_inputs(decimal, expected):
    assert decimal_to_binary(decimal) == expected

def test_decimal_to_binary_large_number():
    assert decimal_to_binary(999999) == "db11110100001000111111db"

@pytest.mark.parametrize("invalid_input", [
    "string",
    None,
    [],
    {},
    1.5,
    float('inf'),
    float('nan')
])
def test_decimal_to_binary_invalid_inputs(invalid_input):
    with pytest.raises((ValueError, TypeError)):
        decimal_to_binary(invalid_input)

def test_decimal_to_binary_negative_numbers():
    result = decimal_to_binary(-1)
    assert result == "db-1db"
    result = decimal_to_binary(-42)
    assert result == "db-101010db"
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

@pytest.mark.parametrize("decimal,expected", [
    (0, "db0db"),
    (1, "db1db"),
    (2, "db10db"),
    (10, "db1010db"),
    (15, "db1111db"),
    (16, "db10000db"),
    (255, "db11111111db"),
    (1000, "db1111101000db"),
])
def test_decimal_to_binary_valid_inputs(decimal, expected):
    assert decimal_to_binary(decimal) == expected

@pytest.mark.parametrize("decimal", [
    -1,
    -10,
    -100
])
def test_decimal_to_binary_negative_numbers(decimal):
    result = decimal_to_binary(decimal)
    assert result.startswith("db")
    assert result.endswith("db")
    binary_part = result[2:-2]
    expected_binary = bin(abs(decimal))[2:]
    assert binary_part == expected_binary

def test_decimal_to_binary_zero():
    assert decimal_to_binary(0) == "db0db"

def test_decimal_to_binary_large_number():
    assert decimal_to_binary(999999) == "db11110100001000111111db"

@pytest.mark.parametrize("invalid_input", [
    "string",
    None,
    [],
    {},
    3.14
])
def test_decimal_to_binary_invalid_inputs(invalid_input):
    with pytest.raises((TypeError, ValueError)):
        decimal_to_binary(invalid_input)
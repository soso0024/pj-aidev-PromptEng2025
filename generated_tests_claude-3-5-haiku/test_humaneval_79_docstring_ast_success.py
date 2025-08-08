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

def decimal_to_binary(decimal):
    if not isinstance(decimal, int):
        raise TypeError("Input must be an integer")
    if decimal < 0:
        raise ValueError("Input must be a non-negative integer")
    return "db" + bin(decimal)[2:] + "db"

def test_decimal_to_binary_positive_numbers():
    assert decimal_to_binary(0) == "db0db"
    assert decimal_to_binary(1) == "db1db"
    assert decimal_to_binary(15) == "db1111db"
    assert decimal_to_binary(32) == "db100000db"
    assert decimal_to_binary(255) == "db11111111db"

def test_decimal_to_binary_large_numbers():
    assert decimal_to_binary(1024) == "db10000000000db"
    assert decimal_to_binary(65535) == "db1111111111111111db"

@pytest.mark.parametrize("decimal,expected", [
    (0, "db0db"),
    (1, "db1db"),
    (2, "db10db"),
    (7, "db111db"),
    (8, "db1000db"),
    (15, "db1111db"),
    (16, "db10000db"),
    (32, "db100000db"),
    (64, "db1000000db"),
    (128, "db10000000db"),
    (255, "db11111111db")
])
def test_decimal_to_binary_parametrized(decimal, expected):
    assert decimal_to_binary(decimal) == expected

def test_decimal_to_binary_negative_numbers():
    with pytest.raises(ValueError):
        decimal_to_binary(-1)
    with pytest.raises(ValueError):
        decimal_to_binary(-100)

def test_decimal_to_binary_non_integer():
    with pytest.raises(TypeError):
        decimal_to_binary(3.14)
    with pytest.raises(TypeError):
        decimal_to_binary("10")
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
from decimal_to_binary import decimal_to_binary

import pytest

@pytest.mark.parametrize("decimal,expected", [
    (0, "db0db"),
    (1, "db1db"),
    (15, "db1111db"),
    (32, "db100000db"),
    (-1, "db-1db"),
    (3.14, "db11.1000011001000100db"),
])
def test_decimal_to_binary(decimal, expected):
    assert decimal_to_binary(decimal) == expected

def test_decimal_to_binary_type_error():
    with pytest.raises(TypeError):
        decimal_to_binary("abc")
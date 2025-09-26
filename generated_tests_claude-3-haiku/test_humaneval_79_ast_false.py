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

@pytest.mark.parametrize("input,expected", [
    (3.14, 'db1.10db'),
    ('test', TypeError),
    (None, TypeError)
])
def test_decimal_to_binary_edge_cases(input, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            decimal_to_binary(input)
    else:
        assert decimal_to_binary(input) == expected
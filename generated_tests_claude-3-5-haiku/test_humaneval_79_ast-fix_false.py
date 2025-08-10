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
    assert decimal_to_binary(15) == "db1111db"
    assert decimal_to_binary(32) == "db100000db"
    assert decimal_to_binary(0) == "db0db"

def test_decimal_to_binary_negative():
    assert decimal_to_binary(-15) == "db-1111db"
    assert decimal_to_binary(-32) == "db-100000db"

def test_decimal_to_binary_type_error():
    with pytest.raises(TypeError):
        decimal_to_binary("not an integer")
        decimal_to_binary(3.14)
        decimal_to_binary(None)
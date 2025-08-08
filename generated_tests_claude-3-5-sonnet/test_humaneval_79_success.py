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

def test_decimal_to_binary_positive():
    assert decimal_to_binary(10) == "db1010db"

def test_decimal_to_binary_large_number():
    assert decimal_to_binary(1000) == "db1111101000db"

@pytest.mark.parametrize("decimal,expected", [
    (0, "db0db"),
    (1, "db1db"),
    (2, "db10db"),
    (3, "db11db"),
    (4, "db100db"),
    (15, "db1111db"),
    (16, "db10000db"),
    (100, "db1100100db"),
])
def test_decimal_to_binary_multiple_values(decimal, expected):
    assert decimal_to_binary(decimal) == expected

def test_decimal_to_binary_max_int():
    assert decimal_to_binary(2**31-1) == "db" + "1" * 31 + "db"

@pytest.mark.xfail(raises=TypeError)
def test_decimal_to_binary_string_input():
    decimal_to_binary("10")

@pytest.mark.xfail(raises=TypeError)
def test_decimal_to_binary_float_input():
    decimal_to_binary(10.5)

@pytest.mark.xfail(raises=TypeError)
def test_decimal_to_binary_none_input():
    decimal_to_binary(None)

@pytest.mark.xfail(raises=OverflowError)
def test_decimal_to_binary_negative():
    decimal_to_binary(-1)

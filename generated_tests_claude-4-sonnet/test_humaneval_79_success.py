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
    return "db" + bin(decimal)[2:] + "db"

def test_decimal_to_binary_zero():
    assert decimal_to_binary(0) == "db0db"

def test_decimal_to_binary_positive_small():
    assert decimal_to_binary(1) == "db1db"
    assert decimal_to_binary(2) == "db10db"
    assert decimal_to_binary(3) == "db11db"
    assert decimal_to_binary(4) == "db100db"
    assert decimal_to_binary(5) == "db101db"

def test_decimal_to_binary_positive_large():
    assert decimal_to_binary(255) == "db11111111db"
    assert decimal_to_binary(1024) == "db10000000000db"
    assert decimal_to_binary(1000000) == "db11110100001001000000db"

@pytest.mark.parametrize("decimal,expected", [
    (7, "db111db"),
    (8, "db1000db"),
    (15, "db1111db"),
    (16, "db10000db"),
    (31, "db11111db"),
    (32, "db100000db"),
    (63, "db111111db"),
    (64, "db1000000db"),
    (127, "db1111111db"),
    (128, "db10000000db")
])
def test_decimal_to_binary_powers_of_two_and_neighbors(decimal, expected):
    assert decimal_to_binary(decimal) == expected

def test_decimal_to_binary_negative():
    assert decimal_to_binary(-1) == "dbb1db"
    assert decimal_to_binary(-10) == "dbb1010db"
    assert decimal_to_binary(-100) == "dbb1100100db"

def test_decimal_to_binary_invalid_types():
    with pytest.raises(TypeError):
        decimal_to_binary("5")
    with pytest.raises(TypeError):
        decimal_to_binary(5.5)
    with pytest.raises(TypeError):
        decimal_to_binary(None)
    with pytest.raises(TypeError):
        decimal_to_binary([])
    with pytest.raises(TypeError):
        decimal_to_binary({})

def test_decimal_to_binary_very_large():
    assert decimal_to_binary(2**20) == "db100000000000000000000db"
    assert decimal_to_binary(2**30) == "db1000000000000000000000000000000db"
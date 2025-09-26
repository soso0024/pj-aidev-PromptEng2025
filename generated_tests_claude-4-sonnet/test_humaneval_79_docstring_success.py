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

def test_decimal_to_binary_one():
    assert decimal_to_binary(1) == "db1db"

def test_decimal_to_binary_small_numbers():
    assert decimal_to_binary(2) == "db10db"
    assert decimal_to_binary(3) == "db11db"
    assert decimal_to_binary(4) == "db100db"
    assert decimal_to_binary(5) == "db101db"
    assert decimal_to_binary(7) == "db111db"
    assert decimal_to_binary(8) == "db1000db"

def test_decimal_to_binary_examples():
    assert decimal_to_binary(15) == "db1111db"
    assert decimal_to_binary(32) == "db100000db"

def test_decimal_to_binary_powers_of_two():
    assert decimal_to_binary(16) == "db10000db"
    assert decimal_to_binary(64) == "db1000000db"
    assert decimal_to_binary(128) == "db10000000db"
    assert decimal_to_binary(256) == "db100000000db"

def test_decimal_to_binary_large_numbers():
    assert decimal_to_binary(255) == "db11111111db"
    assert decimal_to_binary(1023) == "db1111111111db"
    assert decimal_to_binary(1024) == "db10000000000db"

@pytest.mark.parametrize("decimal,expected", [
    (6, "db110db"),
    (9, "db1001db"),
    (10, "db1010db"),
    (11, "db1011db"),
    (12, "db1100db"),
    (13, "db1101db"),
    (14, "db1110db"),
    (31, "db11111db"),
    (63, "db111111db"),
    (127, "db1111111db"),
    (100, "db1100100db"),
    (200, "db11001000db"),
    (500, "db111110100db"),
    (1000, "db1111101000db")
])
def test_decimal_to_binary_parametrized(decimal, expected):
    assert decimal_to_binary(decimal) == expected

def test_decimal_to_binary_negative_numbers():
    assert decimal_to_binary(-1) == "dbb1db"
    assert decimal_to_binary(-10) == "dbb1010db"
    assert decimal_to_binary(-100) == "dbb1100100db"

def test_decimal_to_binary_invalid_types():
    with pytest.raises(TypeError):
        decimal_to_binary("15")
    with pytest.raises(TypeError):
        decimal_to_binary(15.5)
    with pytest.raises(TypeError):
        decimal_to_binary(None)
    with pytest.raises(TypeError):
        decimal_to_binary([15])
    with pytest.raises(TypeError):
        decimal_to_binary({"value": 15})
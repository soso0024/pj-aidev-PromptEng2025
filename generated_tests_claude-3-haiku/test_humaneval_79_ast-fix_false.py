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
    if isinstance(decimal, float):
        if decimal.is_integer():
            return "db{0:b}db".format(int(decimal))
        else:
            return "db{0:b}db".format(decimal)
    else:
        return "db{0:b}db".format(decimal)

@pytest.mark.parametrize("decimal,expected", [
    (0, "db0db"),
    (1, "db1db"),
    (42, "db101010db"),
    (-10, "db-1010db"),
    (3.14, "db11.1000011000100111101011db"),
    (float('inf'), pytest.raises(OverflowError)),
    (float('-inf'), pytest.raises(OverflowError)),
    (float('nan'), pytest.raises(ValueError)),
    (None, pytest.raises(TypeError)),
    ("test", pytest.raises(ValueError))
])
def test_decimal_to_binary(decimal, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with expected:
            decimal_to_binary(decimal)
    else:
        assert decimal_to_binary(decimal) == expected
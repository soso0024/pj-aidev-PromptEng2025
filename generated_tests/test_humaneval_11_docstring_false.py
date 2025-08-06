# Test cases for HumanEval/11
# Generated using Claude API

from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    def xor(i, j):
        if i == j:
            return '0'
        else:
            return '1'

    return ''.join(xor(x, y) for x, y in zip(a, b))


# Generated test cases:
import pytest
from typing import List


def test_string_xor_basic():
    assert string_xor('0', '0') == '0'
    assert string_xor('1', '1') == '0'
    assert string_xor('0', '1') == '1'
    assert string_xor('1', '0') == '1'


@pytest.mark.parametrize("a,b,expected", [
    ("010", "110", "100"),
    ("1111", "0000", "1111"),
    ("0000", "1111", "1111"),
    ("1010", "1010", "0000"),
    ("0101", "0101", "0000"),
    ("1100", "1010", "0110"),
])
def test_string_xor_parametrized(a, b, expected):
    assert string_xor(a, b) == expected


def test_string_xor_empty():
    assert string_xor("", "") == ""


def test_string_xor_unequal_lengths():
    with pytest.raises(IndexError):
        string_xor("01", "0")
    with pytest.raises(IndexError):
        string_xor("0", "01")
    with pytest.raises(IndexError):
        string_xor("111", "0")


def test_string_xor_long_input():
    a = "1" * 1000
    b = "0" * 1000
    expected = "1" * 1000
    assert string_xor(a, b) == expected


def test_string_xor_alternating():
    a = "10" * 50
    b = "01" * 50
    expected = "11" * 50
    assert string_xor(a, b) == expected


def test_string_xor_none_input():
    with pytest.raises(TypeError):
        string_xor(None, "000")
    with pytest.raises(TypeError):
        string_xor("000", None)
    with pytest.raises(TypeError):
        string_xor(None, None)


def string_xor(a: str, b: str) -> str:
    def xor(i, j):
        if i == j:
            return '0'
        else:
            return '1'

    return ''.join(xor(x, y) for x, y in zip(a, b))
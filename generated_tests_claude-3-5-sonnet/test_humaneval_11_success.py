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

def test_string_xor_basic():
    assert string_xor("1010", "1100") == "0110"
    assert string_xor("0000", "1111") == "1111"
    assert string_xor("1111", "1111") == "0000"

@pytest.mark.parametrize("a,b,expected", [
    ("1010", "1100", "0110"),
    ("0000", "0000", "0000"),
    ("1111", "0000", "1111"),
    ("0101", "0011", "0110"),
    ("", "", ""),
    ("1", "1", "0"),
    ("0", "1", "1")
])
def test_string_xor_parametrized(a, b, expected):
    assert string_xor(a, b) == expected

def test_string_xor_empty_strings():
    assert string_xor("", "") == ""

def test_string_xor_single_bits():
    assert string_xor("0", "0") == "0"
    assert string_xor("1", "1") == "0"
    assert string_xor("0", "1") == "1"
    assert string_xor("1", "0") == "1"

def test_string_xor_unequal_lengths():
    result = string_xor("101", "10")
    assert len(result) == 2
    result = string_xor("1", "11")
    assert len(result) == 1
    result = string_xor("111", "1")
    assert len(result) == 1

def test_string_xor_invalid_input():
    result = string_xor("10a", "101")
    assert all(c in '01' for c in result)
    result = string_xor("xyz", "111")
    assert all(c in '01' for c in result)
    result = string_xor("1$1", "101")
    assert all(c in '01' for c in result)

def test_string_xor_none_input():
    with pytest.raises(TypeError):
        string_xor(None, "101")
    with pytest.raises(TypeError):
        string_xor("101", None)
    with pytest.raises(TypeError):
        string_xor(None, None)
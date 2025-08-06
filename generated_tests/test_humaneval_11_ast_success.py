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

def test_string_xor_long_strings():
    a = "1" * 1000
    b = "0" * 1000
    expected = "1" * 1000
    assert string_xor(a, b) == expected

def test_string_xor_alternating_patterns():
    assert string_xor("10" * 5, "11" * 5) == "01" * 5

def test_string_xor_none_input():
    with pytest.raises(TypeError):
        string_xor(None, "1010")
    with pytest.raises(TypeError):
        string_xor("1010", None)
    with pytest.raises(TypeError):
        string_xor(None, None)

def string_xor(a: str, b: str) -> str:
    if a is None or b is None:
        raise TypeError("Inputs cannot be None")
    if len(a) != len(b):
        raise ValueError("Input strings must have equal length")
    if not all(c in '01' for c in a + b):
        raise ValueError("Inputs must contain only '0' and '1'")
    
    def xor(i, j):
        if i == j:
            return '0'
        else:
            return '1'

    return ''.join(xor(x, y) for x, y in zip(a, b))
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

def string_xor(a: str, b: str) -> str:
    def xor(i, j):
        if i == j:
            return '0'
        else:
            return '1'

    return ''.join(xor(x, y) for x, y in zip(a, b))

@pytest.mark.parametrize("a,b,expected", [
    ("0", "0", "0"),
    ("1", "1", "0"),
    ("0", "1", "1"),
    ("1", "0", "1"),
    ("00", "00", "00"),
    ("11", "11", "00"),
    ("01", "10", "11"),
    ("10", "01", "11"),
    ("000", "111", "111"),
    ("111", "000", "111"),
    ("101", "010", "111"),
    ("010", "101", "111"),
    ("1010", "0101", "1111"),
    ("0000", "0000", "0000"),
    ("1111", "1111", "0000"),
    ("10101010", "01010101", "11111111"),
    ("00110011", "11001100", "11111111"),
    ("", "", ""),
])
def test_string_xor_basic_cases(a, b, expected):
    assert string_xor(a, b) == expected

def test_string_xor_single_bit():
    assert string_xor("0", "0") == "0"
    assert string_xor("0", "1") == "1"
    assert string_xor("1", "0") == "1"
    assert string_xor("1", "1") == "0"

def test_string_xor_empty_strings():
    assert string_xor("", "") == ""

def test_string_xor_long_strings():
    a = "1" * 100
    b = "0" * 100
    expected = "1" * 100
    assert string_xor(a, b) == expected
    
    a = "1" * 100
    b = "1" * 100
    expected = "0" * 100
    assert string_xor(a, b) == expected

def test_string_xor_alternating_pattern():
    a = "10" * 50
    b = "01" * 50
    expected = "11" * 50
    assert string_xor(a, b) == expected

def test_string_xor_different_lengths():
    # When strings have different lengths, zip will stop at the shorter one
    assert string_xor("101", "01") == "11"
    assert string_xor("10", "101") == "00"
    assert string_xor("1", "101") == "0"
    assert string_xor("101", "1") == "0"

def test_string_xor_non_binary_characters():
    # Function will work with any characters, not just 0 and 1
    assert string_xor("abc", "abc") == "000"
    assert string_xor("abc", "def") == "111"
    assert string_xor("aaa", "bbb") == "111"
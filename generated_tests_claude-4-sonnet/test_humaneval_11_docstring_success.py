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

class TestStringXor:
    
    @pytest.mark.parametrize("a,b,expected", [
        ("0", "0", "0"),
        ("1", "1", "0"),
        ("0", "1", "1"),
        ("1", "0", "1"),
        ("010", "110", "100"),
        ("101", "010", "111"),
        ("000", "000", "000"),
        ("111", "111", "000"),
        ("101010", "010101", "111111"),
        ("000000", "111111", "111111"),
        ("1111", "0000", "1111"),
        ("10101010", "01010101", "11111111"),
        ("11110000", "00001111", "11111111"),
        ("1", "0", "1"),
        ("0", "1", "1"),
        ("10", "01", "11"),
        ("01", "10", "11"),
        ("100", "011", "111"),
        ("001", "110", "111"),
        ("1010101", "0101010", "1111111")
    ])
    def test_string_xor_valid_inputs(self, a, b, expected):
        assert string_xor(a, b) == expected
    
    def test_empty_strings(self):
        assert string_xor("", "") == ""
    
    def test_single_bit_all_combinations(self):
        assert string_xor("0", "0") == "0"
        assert string_xor("0", "1") == "1"
        assert string_xor("1", "0") == "1"
        assert string_xor("1", "1") == "0"
    
    def test_different_lengths_truncated(self):
        assert string_xor("101", "01") == "11"
        assert string_xor("10", "101") == "00"
        assert string_xor("1", "101") == "0"
        assert string_xor("101", "1") == "0"
    
    def test_long_strings(self):
        a = "1" * 100
        b = "0" * 100
        expected = "1" * 100
        assert string_xor(a, b) == expected
        
        a = "1" * 50
        b = "1" * 50
        expected = "0" * 50
        assert string_xor(a, b) == expected
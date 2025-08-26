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

def test_string_xor_equal_strings():
    assert string_xor('0', '0') == '0'
    assert string_xor('1', '1') == '0'

def test_string_xor_different_strings():
    assert string_xor('0', '1') == '1'
    assert string_xor('1', '0') == '1'

def test_string_xor_longer_strings():
    assert string_xor('1010', '0101') == '1111'
    assert string_xor('11110000', '00001111') == '11111111'

def test_string_xor_empty_strings():
    assert string_xor('', '') == ''

@pytest.mark.parametrize("a,b,expected", [
    ('0', '0', '0'),
    ('1', '1', '0'),
    ('0', '1', '1'),
    ('1', '0', '1'),
    ('1010', '0101', '1111'),
    ('', '', ''),
    ('11110000', '00001111', '11111111')
])
def test_string_xor_parametrized(a, b, expected):
    assert string_xor(a, b) == expected

def test_string_xor_unequal_length():
    with pytest.raises(ValueError):
        string_xor('10', '101')

def string_xor(a: str, b: str) -> str:
    if len(a) != len(b):
        raise ValueError("Input strings must have equal length")
    
    def xor(i, j):
        if i == j:
            return '0'
        else:
            return '1'

    return ''.join(xor(x, y) for x, y in zip(a, b))
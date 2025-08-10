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
from typing import List
import pytest

def string_xor(a: str, b: str) -> str:
    if len(a) != len(b):
        raise ValueError("Input strings must have equal length")
    
    if not all(c in '01' for c in a + b):
        raise ValueError("Input must contain only binary digits")

    def xor(i, j):
        if i == j:
            return '0'
        else:
            return '1'

    return ''.join(xor(x, y) for x, y in zip(a, b))

def test_string_xor_equal_length_binary_strings():
    assert string_xor('1010', '0101') == '1111'
    assert string_xor('0000', '1111') == '1111'
    assert string_xor('1100', '1010') == '0110'

def test_string_xor_same_strings():
    assert string_xor('1010', '1010') == '0000'
    assert string_xor('0000', '0000') == '0000'

def test_string_xor_empty_strings():
    assert string_xor('', '') == ''

@pytest.mark.parametrize("a,b,expected", [
    ('10101', '01010', '11111'),
    ('11110000', '00001111', '11111111'),
    ('10', '01', '11')
])
def test_string_xor_parametrized(a, b, expected):
    assert string_xor(a, b) == expected

def test_string_xor_unequal_length_strings():
    with pytest.raises(ValueError):
        string_xor('1010', '10101')

def test_string_xor_non_binary_input():
    with pytest.raises(ValueError):
        string_xor('1012', '1010')
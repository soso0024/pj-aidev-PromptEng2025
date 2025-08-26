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

def test_string_xor_empty_strings():
    assert string_xor('', '') == ''

def test_string_xor_equal_strings():
    assert string_xor('1010', '1010') == '0000'

def test_string_xor_different_length_strings():
    with pytest.raises(ValueError):
        string_xor('1010', '101')

@pytest.mark.parametrize("a,b,expected", [
    ('1001', '0101', '1100'),
    ('101', '011', '110'),
    ('11', '00', '11')
])
def test_string_xor_normal_cases(a, b, expected):
    assert string_xor(a, b) == expected

def string_xor(a: str, b: str):
    if len(a) != len(b):
        raise ValueError("Input strings must be of equal length")

    def xor(i, j):
        if i == j:
            return '0'
        else:
            return '1'

    return ''.join(xor(x, y) for x, y in zip(a, b))

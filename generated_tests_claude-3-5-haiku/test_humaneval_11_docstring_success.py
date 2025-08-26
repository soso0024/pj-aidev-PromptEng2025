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

def string_xor(a: str, b: str) -> str:
    if len(a) != len(b):
        raise ValueError("Input strings must have equal length")
    
    if not all(c in '01' for c in a + b):
        raise ValueError("Input strings must contain only 0s and 1s")

    def xor(i, j):
        if i == j:
            return '0'
        else:
            return '1'

    return ''.join(xor(x, y) for x, y in zip(a, b))

def test_string_xor_normal_cases():
    assert string_xor('010', '110') == '100'
    assert string_xor('1010', '1100') == '0110'
    assert string_xor('0000', '1111') == '1111'
    assert string_xor('1111', '1111') == '0000'

def test_string_xor_edge_cases():
    assert string_xor('', '') == ''
    assert string_xor('0', '1') == '1'
    assert string_xor('1', '0') == '1'

@pytest.mark.parametrize("a,b,expected", [
    ('010', '110', '100'),
    ('1010', '1100', '0110'),
    ('0000', '1111', '1111'),
    ('1111', '1111', '0000'),
    ('', '', ''),
    ('0', '1', '1'),
    ('1', '0', '1')
])
def test_string_xor_parametrized(a, b, expected):
    assert string_xor(a, b) == expected

def test_string_xor_unequal_lengths():
    with pytest.raises(ValueError):
        string_xor('010', '1010')

def test_string_xor_invalid_input():
    with pytest.raises(ValueError):
        string_xor('012', '110')
    with pytest.raises(ValueError):
        string_xor('a10', '110')
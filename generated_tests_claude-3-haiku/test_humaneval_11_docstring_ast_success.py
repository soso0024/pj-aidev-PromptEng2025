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

    if len(a) != len(b):
        raise ValueError("Input strings must be of equal length")
    if not all(c in '01' for c in a) or not all(c in '01' for c in b):
        raise ValueError("Input strings must contain only 0s and 1s")

    return ''.join(xor(x, y) for x, y in zip(a, b))

@pytest.mark.parametrize("a,b,expected", [
    ('010', '110', '100'),
    ('111', '111', '000'),
    ('000', '000', '000'),
    ('101', '011', '110'),
    ('', '', ''),
    ('1', '0', '1'),
    ('0', '1', '1'),
])
def test_string_xor(a, b, expected):
    assert string_xor(a, b) == expected

def test_string_xor_different_lengths():
    with pytest.raises(ValueError):
        string_xor('010', '11')

def test_string_xor_non_binary_input():
    with pytest.raises(ValueError):
        string_xor('010', '11a')
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

@pytest.mark.parametrize("a, b, expected", [
    ('010', '110', '100'),
    ('1010', '1001', '0011'),
    ('111', '111', '000'),
    ('000', '000', '000'),
    ('', '', ''),
    ('1', '0', '1'),
    ('0', '1', '1'),
])
def test_string_xor(a, b, expected):
    assert string_xor(a, b) == expected

def test_string_xor_different_lengths():
    with pytest.raises(ValueError):
        string_xor('010', '11')
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

def test_string_xor_empty_strings():
    assert string_xor('', '') == ''

def test_string_xor_same_length():
    assert string_xor('1010', '1001') == '0011'
    assert string_xor('0101', '1010') == '1111'

def test_string_xor_different_lengths():
    with pytest.raises(ValueError):
        string_xor('123', '45')

@pytest.mark.parametrize("a,b,expected", [
    ('', '0', '0'),
    ('1', '0', '1'),
    ('101', '010', '111'),
    ('0101', '1010', '1111')
])
def test_string_xor_examples(a, b, expected):
    assert string_xor(a, b) == expected

def test_string_xor_non_string_input():
    with pytest.raises(TypeError):
        string_xor(123, '456')
    with pytest.raises(TypeError):
        string_xor('123', 456)
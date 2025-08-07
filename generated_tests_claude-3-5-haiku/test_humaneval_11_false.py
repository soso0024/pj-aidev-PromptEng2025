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
        if not a:
            return b
        if not b:
            return a
        raise ValueError("Inputs must be of equal length")

    def xor(i, j):
        if i == j:
            return '0'
        else:
            return '1'

    return ''.join(xor(x, y) for x, y in zip(a, b))

def test_string_xor_equal_length_binary():
    assert string_xor('1010', '0101') == '1111'

def test_string_xor_equal_length_mixed():
    assert string_xor('hello', 'world') == '\x1f\x16\x0f\x1c\x1b'

def test_string_xor_empty_strings():
    assert string_xor('', '') == ''

def test_string_xor_single_character():
    assert string_xor('1', '0') == '1'
    assert string_xor('1', '1') == '0'

@pytest.mark.parametrize("a,b,expected", [
    ('1100', '1010', '0110'),
    ('abc', 'xyz', '\x19\x1b\x1d'),
    ('', 'test', 'test'),
    ('test', '', 'test')
])
def test_string_xor_parametrized(a, b, expected):
    assert string_xor(a, b) == expected

def test_string_xor_different_lengths():
    with pytest.raises(ValueError):
        string_xor('short', 'longer')

def test_string_xor_unicode():
    assert string_xor('こんにちは', 'world') == '\x1c\x16\x0f\x1c\x1b'
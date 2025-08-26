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
    if a is None or b is None:
        raise TypeError("Inputs cannot be None")
    
    if not isinstance(a, str) or not isinstance(b, str):
        raise TypeError("Inputs must be strings")
    
    if len(a) != len(b):
        raise ValueError("Inputs must be of equal length")
    
    def xor(i, j):
        if i == j:
            return '0'
        else:
            return '1'

    return ''.join(xor(x, y) for x, y in zip(a, b))

def test_string_xor_equal_length_binary():
    assert string_xor('1010', '0101') == '1111'
    assert string_xor('0000', '1111') == '1111'
    assert string_xor('1100', '1010') == '0110'

def test_string_xor_equal_length_mixed():
    assert string_xor('abc', 'def') == '111'

@pytest.mark.parametrize("a,b,expected", [
    ('', '', ''),
    ('0', '1', '1'),
    ('1', '0', '1'),
    ('10', '01', '11'),
    ('hello', 'world', '11111')
])
def test_string_xor_parametrized(a, b, expected):
    assert string_xor(a, b) == expected

def test_string_xor_different_lengths():
    with pytest.raises(ValueError):
        string_xor('short', 'longer')

def test_string_xor_none_input():
    with pytest.raises(TypeError):
        string_xor(None, None)

def test_string_xor_non_string_input():
    with pytest.raises(TypeError):
        string_xor(123, 456)
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


@pytest.mark.parametrize("a,b,expected", [
    ("010", "110", "100"),
    ("1", "0", "1"),
    ("0", "1", "1"),
    ("1", "1", "0"),
    ("0", "0", "0"),
    ("11111", "00000", "11111"),
    ("00000", "11111", "11111"),
    ("11111", "11111", "00000"),
    ("00000", "00000", "00000"),
    ("1010", "0101", "1111"),
    ("1100", "1010", "0110"),
])
def test_string_xor_valid_inputs(a: str, b: str, expected: str):
    assert string_xor(a, b) == expected


@pytest.mark.parametrize("a,b", [
    ("", "1"),
    ("1", ""),
    ("", ""),
    ("01", "0"),
    ("0", "01"),
])
def test_string_xor_different_lengths(a: str, b: str):
    result = string_xor(a, b)
    assert len(result) == min(len(a), len(b))


def validate_binary_string(s: str) -> bool:
    return all(c in '01' for c in s)


@pytest.mark.parametrize("a,b", [
    ("012", "110"),
    ("abc", "101"),
    ("01a", "111"),
    ("2", "1"),
    ("", "2"),
])
def test_string_xor_invalid_inputs(a: str, b: str):
    if not validate_binary_string(a) or not validate_binary_string(b):
        try:
            string_xor(a, b)
            pytest.fail("Expected ValueError but no exception was raised")
        except ValueError:
            pass
        except Exception as e:
            pytest.fail(f"Expected ValueError but got {type(e)}")


@pytest.mark.parametrize("a,b", [
    (None, "110"),
    ("010", None),
    (None, None),
    (123, "101"),
    ("101", 123),
])
def test_string_xor_type_errors(a, b):
    with pytest.raises(TypeError):
        string_xor(a, b)
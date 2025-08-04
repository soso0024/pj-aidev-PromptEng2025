# Test cases for HumanEval/15
# Generated using Claude API



def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """

    return ' '.join([str(x) for x in range(n + 1)])


# Generated test cases:
import pytest

def test_string_sequence_zero():
    assert string_sequence(0) == "0"

def test_string_sequence_positive():
    assert string_sequence(3) == "0 1 2 3"

def test_string_sequence_one():
    assert string_sequence(1) == "0 1"

@pytest.mark.parametrize("input_n,expected", [
    (5, "0 1 2 3 4 5"),
    (2, "0 1 2"),
    (10, "0 1 2 3 4 5 6 7 8 9 10")
])
def test_string_sequence_various_inputs(input_n, expected):
    assert string_sequence(input_n) == expected

def test_string_sequence_negative_input():
    result = string_sequence(-1)
    assert result == ""

def test_string_sequence_large_number():
    assert string_sequence(100).count(" ") == 100
    assert string_sequence(100).startswith("0")
    assert string_sequence(100).endswith("100")

@pytest.mark.parametrize("invalid_type", [
    "string",
    None,
    3.14,
    [],
    {}
])
def test_string_sequence_invalid_types(invalid_type):
    with pytest.raises((TypeError, ValueError)):
        string_sequence(invalid_type)
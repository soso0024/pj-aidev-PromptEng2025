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

def string_sequence(n: int):
    return ' '.join([str(x) for x in range(n + 1)])

def test_string_sequence_zero():
    assert string_sequence(0) == "0"

def test_string_sequence_one():
    assert string_sequence(1) == "0 1"

def test_string_sequence_small_positive():
    assert string_sequence(3) == "0 1 2 3"

def test_string_sequence_larger_positive():
    assert string_sequence(10) == "0 1 2 3 4 5 6 7 8 9 10"

@pytest.mark.parametrize("n,expected", [
    (0, "0"),
    (1, "0 1"),
    (2, "0 1 2"),
    (4, "0 1 2 3 4"),
    (5, "0 1 2 3 4 5")
])
def test_string_sequence_parametrized(n, expected):
    assert string_sequence(n) == expected

def test_string_sequence_negative():
    assert string_sequence(-1) == ""

def test_string_sequence_negative_larger():
    assert string_sequence(-5) == ""

def test_string_sequence_type_error():
    with pytest.raises(TypeError):
        string_sequence("5")

def test_string_sequence_type_error_float():
    with pytest.raises(TypeError):
        string_sequence(5.5)

def test_string_sequence_type_error_none():
    with pytest.raises(TypeError):
        string_sequence(None)

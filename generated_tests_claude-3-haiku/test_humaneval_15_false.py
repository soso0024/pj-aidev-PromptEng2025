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

def test_string_sequence_positive_integer():
    assert string_sequence(5) == '0 1 2 3 4 5'

def test_string_sequence_zero():
    assert string_sequence(0) == '0'

def test_string_sequence_negative_integer():
    with pytest.raises(ValueError):
        string_sequence(-1)

@pytest.mark.parametrize("input,expected", [
    (0, '0'),
    (5, '0 1 2 3 4 5'),
    (10, '0 1 2 3 4 5 6 7 8 9 10')
])
def test_string_sequence_parameterized(input, expected):
    assert string_sequence(input) == expected
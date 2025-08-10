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

def test_string_sequence_positive_integers():
    assert string_sequence(0) == '0'
    assert string_sequence(1) == '0 1'
    assert string_sequence(5) == '0 1 2 3 4 5'

def test_string_sequence_negative_integers():
    with pytest.raises(ValueError):
        string_sequence(-1)

@pytest.mark.parametrize("input,expected", [
    (0, '0'),
    (1, '0 1'),
    (5, '0 1 2 3 4 5'),
    (-1, ValueError)
])
def test_string_sequence_parametrized(input, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            string_sequence(input)
    else:
        assert string_sequence(input) == expected
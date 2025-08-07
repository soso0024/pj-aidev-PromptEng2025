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

def test_string_sequence_positive():
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(0) == '0'
    assert string_sequence(10) == '0 1 2 3 4 5 6 7 8 9 10'

def test_string_sequence_negative():
    with pytest.raises(ValueError):
        string_sequence(-1)
    with pytest.raises(TypeError):
        string_sequence('a')

@pytest.mark.parametrize("n,expected", [
    (0, '0'),
    (5, '0 1 2 3 4 5'),
    (10, '0 1 2 3 4 5 6 7 8 9 10'),
    (-1, ValueError),
    ('a', TypeError)
])
def test_string_sequence_parametrize(n, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            string_sequence(n)
    else:
        assert string_sequence(n) == expected
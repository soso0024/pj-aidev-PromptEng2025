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
    assert string_sequence(0) == '0'

@pytest.mark.parametrize("n,expected", [
    (5, '0 1 2 3 4 5'),
    (10, '0 1 2 3 4 5 6 7 8 9 10'),
    (-1, ''),
])
def test_string_sequence_positive(n, expected):
    assert string_sequence(n) == expected

def test_string_sequence_type_error():
    with pytest.raises(TypeError):
        string_sequence('a')

def string_sequence(n: int) -> str:
    return ' '.join([str(x) for x in range(n + 1)])

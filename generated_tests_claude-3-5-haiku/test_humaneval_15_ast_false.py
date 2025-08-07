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

def test_string_sequence_single_number():
    assert string_sequence(1) == '0 1'

def test_string_sequence_multiple_numbers():
    assert string_sequence(5) == '0 1 2 3 4 5'

def test_string_sequence_large_number():
    assert string_sequence(10) == '0 1 2 3 4 5 6 7 8 9 10'

def test_string_sequence_negative_input():
    with pytest.raises(ValueError, match="Input must be non-negative"):
        string_sequence(-1)

@pytest.mark.parametrize("input_n,expected", [
    (0, '0'),
    (1, '0 1'),
    (3, '0 1 2 3'),
    (5, '0 1 2 3 4 5')
])
def test_string_sequence_parametrized(input_n, expected):
    assert string_sequence(input_n) == expected
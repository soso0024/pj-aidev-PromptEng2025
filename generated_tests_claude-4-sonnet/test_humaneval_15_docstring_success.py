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

def string_sequence(n: int) -> str:
    return ' '.join([str(x) for x in range(n + 1)])

def test_string_sequence_zero():
    assert string_sequence(0) == '0'

def test_string_sequence_positive_small():
    assert string_sequence(1) == '0 1'
    assert string_sequence(2) == '0 1 2'
    assert string_sequence(3) == '0 1 2 3'

def test_string_sequence_positive_medium():
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(10) == '0 1 2 3 4 5 6 7 8 9 10'

def test_string_sequence_positive_large():
    result = string_sequence(100)
    expected = ' '.join([str(i) for i in range(101)])
    assert result == expected

@pytest.mark.parametrize("n,expected", [
    (0, '0'),
    (1, '0 1'),
    (2, '0 1 2'),
    (3, '0 1 2 3'),
    (4, '0 1 2 3 4'),
    (5, '0 1 2 3 4 5'),
    (7, '0 1 2 3 4 5 6 7'),
    (15, '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15')
])
def test_string_sequence_parametrized(n, expected):
    assert string_sequence(n) == expected

def test_string_sequence_negative():
    assert string_sequence(-1) == ''
    assert string_sequence(-5) == ''
    assert string_sequence(-100) == ''

def test_string_sequence_type_errors():
    with pytest.raises(TypeError):
        string_sequence("5")
    with pytest.raises(TypeError):
        string_sequence(5.5)
    with pytest.raises(TypeError):
        string_sequence(None)
    with pytest.raises(TypeError):
        string_sequence([5])

def test_string_sequence_return_type():
    result = string_sequence(5)
    assert isinstance(result, str)

def test_string_sequence_spaces():
    result = string_sequence(3)
    assert result.count(' ') == 3
    assert not result.startswith(' ')
    assert not result.endswith(' ')
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

def test_string_sequence_positive():
    assert string_sequence(5) == '0 1 2 3 4 5'

def test_string_sequence_one():
    assert string_sequence(1) == '0 1'

@pytest.mark.parametrize("input_n,expected", [
    (3, "0 1 2 3"),
    (2, "0 1 2"),
    (7, "0 1 2 3 4 5 6 7"),
    (10, "0 1 2 3 4 5 6 7 8 9 10")
])
def test_string_sequence_various_inputs(input_n, expected):
    assert string_sequence(input_n) == expected

@pytest.mark.parametrize("invalid_input", [
    -1, -100, -999
])
def test_string_sequence_negative_numbers(invalid_input):
    assert string_sequence(invalid_input) == ''

def test_string_sequence_type_error():
    with pytest.raises(TypeError):
        string_sequence("not an integer")
    with pytest.raises(TypeError):
        string_sequence(None)
    with pytest.raises(TypeError):
        string_sequence(3.14)

def test_string_sequence_large_number():
    result = string_sequence(100)
    assert result.startswith("0 1 2")
    assert result.endswith("98 99 100")
    assert len(result.split()) == 101

def test_string_sequence_spacing():
    result = string_sequence(3)
    assert result.count(" ") == 3
    assert not result.startswith(" ")
    assert not result.endswith(" ")

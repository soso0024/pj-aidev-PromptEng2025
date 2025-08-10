# Test cases for HumanEval/42
# Generated using Claude API



def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """

    return [(e + 1) for e in l]


# Generated test cases:
import pytest

def test_incr_list_normal_integers():
    assert incr_list([1, 2, 3]) == [2, 3, 4]

def test_incr_list_negative_integers():
    assert incr_list([-1, -2, -3]) == [0, -1, -2]

def test_incr_list_zero():
    assert incr_list([0]) == [1]

def test_incr_list_empty_list():
    assert incr_list([]) == []

def test_incr_list_mixed_numbers():
    assert incr_list([1.5, -2.5, 0]) == [2.5, -1.5, 1]

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3], [2, 3, 4]),
    ([-1, -2, -3], [0, -1, -2]),
    ([0], [1]),
    ([], []),
    ([1.5, -2.5, 0], [2.5, -1.5, 1])
])
def test_incr_list_parametrized(input_list, expected):
    assert incr_list(input_list) == expected

def test_incr_list_type_error():
    with pytest.raises(TypeError):
        incr_list(None)

def test_incr_list_non_numeric():
    with pytest.raises(TypeError):
        incr_list(['a', 'b', 'c'])

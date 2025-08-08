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

def test_incr_list_basic():
    assert incr_list([1, 2, 3]) == [2, 3, 4]

def test_incr_list_empty():
    assert incr_list([]) == []

def test_incr_list_negative():
    assert incr_list([-1, -2, -3]) == [0, -1, -2]

def test_incr_list_mixed():
    assert incr_list([-1, 0, 1]) == [0, 1, 2]

def test_incr_list_zeros():
    assert incr_list([0, 0, 0]) == [1, 1, 1]

def test_incr_list_large_numbers():
    assert incr_list([999999, 1000000]) == [1000000, 1000001]

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3], [2, 3, 4]),
    ([], []),
    ([0], [1]),
    ([-1], [0]),
    ([999], [1000])
])
def test_incr_list_parametrized(input_list, expected):
    assert incr_list(input_list) == expected

def test_incr_list_type_error():
    with pytest.raises(TypeError):
        incr_list(None)

def test_incr_list_non_numeric():
    with pytest.raises(TypeError):
        incr_list(['a', 'b', 'c'])

def test_incr_list_mixed_types():
    with pytest.raises(TypeError):
        incr_list([1, 'a', 2])

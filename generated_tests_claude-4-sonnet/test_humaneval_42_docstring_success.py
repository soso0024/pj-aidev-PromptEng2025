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

def incr_list(l: list):
    return [(e + 1) for e in l]

def test_incr_list_basic():
    assert incr_list([1, 2, 3]) == [2, 3, 4]

def test_incr_list_longer():
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]

def test_incr_list_empty():
    assert incr_list([]) == []

def test_incr_list_single_element():
    assert incr_list([5]) == [6]

def test_incr_list_negative_numbers():
    assert incr_list([-1, -5, -10]) == [0, -4, -9]

def test_incr_list_zero():
    assert incr_list([0]) == [1]

def test_incr_list_mixed_positive_negative():
    assert incr_list([-2, 0, 3, -1]) == [-1, 1, 4, 0]

def test_incr_list_large_numbers():
    assert incr_list([999, 1000, 10000]) == [1000, 1001, 10001]

@pytest.mark.parametrize("input_list,expected", [
    ([1], [2]),
    ([0, 0, 0], [1, 1, 1]),
    ([-100], [-99]),
    ([1, 2, 3, 4, 5], [2, 3, 4, 5, 6])
])
def test_incr_list_parametrized(input_list, expected):
    assert incr_list(input_list) == expected

def test_incr_list_with_floats():
    assert incr_list([1.5, 2.7, 3.9]) == [2.5, 3.7, 4.9]

def test_incr_list_type_error():
    with pytest.raises(TypeError):
        incr_list([1, 2, "string"])

def test_incr_list_type_error_none():
    with pytest.raises(TypeError):
        incr_list([1, None, 3])

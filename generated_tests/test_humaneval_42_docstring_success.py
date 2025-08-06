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

def test_basic_increment():
    assert incr_list([1, 2, 3]) == [2, 3, 4]

def test_empty_list():
    assert incr_list([]) == []

def test_negative_numbers():
    assert incr_list([-1, -2, -3]) == [0, -1, -2]

def test_zero():
    assert incr_list([0]) == [1]

def test_large_numbers():
    assert incr_list([999999, 1000000]) == [1000000, 1000001]

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3], [2, 3, 4]),
    ([], []),
    ([0], [1]),
    ([-1, 0, 1], [0, 1, 2]),
    ([5, 3, 5, 2, 3, 3, 9, 0, 123], [6, 4, 6, 3, 4, 4, 10, 1, 124])
])
def test_incr_list_parametrized(input_list, expected):
    assert incr_list(input_list) == expected

def test_single_element():
    assert incr_list([42]) == [43]

def test_repeated_elements():
    assert incr_list([1, 1, 1]) == [2, 2, 2]

@pytest.mark.xfail(raises=TypeError)
def test_invalid_input_none():
    incr_list(None)

@pytest.mark.xfail(raises=TypeError)
def test_invalid_input_non_list():
    incr_list("not a list")

@pytest.mark.xfail(raises=TypeError)
def test_list_with_non_numeric():
    incr_list([1, "2", 3])

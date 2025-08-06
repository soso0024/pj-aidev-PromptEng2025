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
    assert incr_list([0, 0, 0]) == [1, 1, 1]

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3], [2, 3, 4]),
    ([5, 3, 5, 2, 3, 3, 9, 0, 123], [6, 4, 6, 3, 4, 4, 10, 1, 124]),
    ([], []),
    ([0], [1]),
    ([-1, -2, -3], [0, -1, -2]),
    ([999], [1000]),
])
def test_incr_list_parametrized(input_list, expected):
    assert incr_list(input_list) == expected

def test_incr_list_empty():
    assert incr_list([]) == []

def test_incr_list_single():
    assert incr_list([42]) == [43]

def test_incr_list_negative():
    assert incr_list([-5, -3, -1]) == [-4, -2, 0]

def test_incr_list_mixed():
    assert incr_list([-1, 0, 1]) == [0, 1, 2]

@pytest.mark.xfail(raises=TypeError)
def test_incr_list_non_numeric():
    incr_list(['a', 'b', 'c'])

@pytest.mark.xfail(raises=TypeError)
def test_incr_list_none():
    incr_list(None)

@pytest.mark.xfail(raises=TypeError)
def test_incr_list_invalid_input():
    incr_list("not a list")

def test_incr_list_large_numbers():
    assert incr_list([1000000, 2000000]) == [1000001, 2000001]

def test_incr_list_floats():
    result = incr_list([1.5, 2.7, 3.2])
    assert [abs(x - y) < 1e-10 for x, y in zip(result, [2.5, 3.7, 4.2])]

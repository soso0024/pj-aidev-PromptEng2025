# Test cases for HumanEval/30
# Generated using Claude API



def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """

    return [e for e in l if e > 0]


# Generated test cases:
import pytest

def test_get_positive_empty_list():
    assert get_positive([]) == []

def test_get_positive_all_positive():
    assert get_positive([1, 2, 3]) == [1, 2, 3]

def test_get_positive_all_negative():
    assert get_positive([-1, -2, -3]) == []

def test_get_positive_mixed():
    assert get_positive([-1, 0, 1, -2, 2, -3, 3]) == [1, 2, 3]

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3], [1, 2, 3]),
    ([-1, 0, 1], [1]),
    ([0, 0, 0], []),
    ([-1, -2, -3], []),
    ([1, -1, 2, -2, 3, -3], [1, 2, 3])
])
def test_get_positive_parametrized(input_list, expected):
    assert get_positive(input_list) == expected

def get_positive(l: list):
    return [e for e in l if e > 0]

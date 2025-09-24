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

def get_positive(l: list):
    return [e for e in l if e > 0]

def test_get_positive_mixed_numbers():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]

def test_get_positive_with_zero():
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]

def test_get_positive_empty_list():
    assert get_positive([]) == []

def test_get_positive_all_negative():
    assert get_positive([-1, -2, -3, -4, -5]) == []

def test_get_positive_all_positive():
    assert get_positive([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_get_positive_only_zero():
    assert get_positive([0]) == []

def test_get_positive_multiple_zeros():
    assert get_positive([0, 0, 0]) == []

def test_get_positive_single_positive():
    assert get_positive([5]) == [5]

def test_get_positive_single_negative():
    assert get_positive([-5]) == []

def test_get_positive_floats():
    assert get_positive([-1.5, 2.3, -4.7, 5.1, 0.0]) == [2.3, 5.1]

def test_get_positive_large_numbers():
    assert get_positive([-1000000, 2000000, -3000000]) == [2000000]

@pytest.mark.parametrize("input_list,expected", [
    ([1, -1, 2, -2], [1, 2]),
    ([0, 1, 0, 2], [1, 2]),
    ([-10, -20, -30], []),
    ([10, 20, 30], [10, 20, 30]),
    ([0.1, -0.1, 0.5], [0.1, 0.5])
])
def test_get_positive_parametrized(input_list, expected):
    assert get_positive(input_list) == expected

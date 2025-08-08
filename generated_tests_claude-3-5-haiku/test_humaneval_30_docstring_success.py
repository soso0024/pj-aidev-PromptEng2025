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

def test_get_positive_normal_case():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]

def test_get_positive_mixed_list():
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]

def test_get_positive_empty_list():
    assert get_positive([]) == []

def test_get_positive_no_positives():
    assert get_positive([-1, -2, -3, 0]) == []

def test_get_positive_all_positives():
    assert get_positive([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

@pytest.mark.parametrize("input_list,expected", [
    ([-1, 2, -4, 5, 6], [2, 5, 6]),
    ([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], [5, 3, 2, 3, 9, 123, 1]),
    ([], []),
    ([-1, -2, -3, 0], []),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
])
def test_get_positive_parametrized(input_list, expected):
    assert get_positive(input_list) == expected

def test_get_positive_large_numbers():
    assert get_positive([-1000000, 1000000]) == [1000000]

def test_get_positive_floating_point():
    assert get_positive([-1.5, 2.5, -4.7, 5.1, 6.0]) == [2.5, 5.1, 6.0]

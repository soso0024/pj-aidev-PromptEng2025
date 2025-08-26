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
    assert get_positive([1, -2, 3, -4, 5]) == [1, 3, 5]

def test_get_positive_empty_list():
    assert get_positive([]) == []

def test_get_positive_no_positive_numbers():
    assert get_positive([-1, -2, -3]) == []

def test_get_positive_all_positive_numbers():
    assert get_positive([1, 2, 3]) == [1, 2, 3]

def test_get_positive_zero_included():
    assert get_positive([0, 1, -1]) == [1]

@pytest.mark.parametrize("input_list,expected", [
    ([1, -2, 3, -4, 5], [1, 3, 5]),
    ([], []),
    ([-1, -2, -3], []),
    ([1, 2, 3], [1, 2, 3]),
    ([0, 1, -1], [1])
])
def test_get_positive_parametrized(input_list, expected):
    assert get_positive(input_list) == expected

def test_get_positive_mixed_types():
    with pytest.raises(TypeError):
        get_positive([1, 'a', 2, 'b'])

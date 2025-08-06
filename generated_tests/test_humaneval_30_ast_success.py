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

def test_get_positive_basic():
    assert get_positive([1, 2, 3]) == [1, 2, 3]
    assert get_positive([-1, 0, 1]) == [1]
    assert get_positive([]) == []

@pytest.mark.parametrize("input_list,expected", [
    ([1, -2, 3, -4, 5], [1, 3, 5]),
    ([0, 0, 0], []),
    ([-1, -2, -3], []),
    ([1.5, -2.5, 3.5], [1.5, 3.5]),
    ([10**6, -(10**6)], [10**6]),
])
def test_get_positive_parametrized(input_list, expected):
    assert get_positive(input_list) == expected

def test_get_positive_all_positive():
    assert get_positive([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_get_positive_all_negative():
    assert get_positive([-1, -2, -3, -4, -5]) == []

def test_get_positive_mixed_types():
    assert get_positive([1, -2.5, 3.14, -4, 5.0]) == [1, 3.14, 5.0]

def test_get_positive_single_element():
    assert get_positive([1]) == [1]
    assert get_positive([-1]) == []
    assert get_positive([0]) == []

@pytest.mark.parametrize("invalid_input", [
    None,
    "string",
    123,
    {'a': 1}
])
def test_get_positive_invalid_input(invalid_input):
    with pytest.raises((TypeError, AttributeError)):
        get_positive(invalid_input)

def test_get_positive_tuple_input():
    result = get_positive((1, 2, 3))
    assert result == [1, 2, 3]

def test_get_positive_nested_lists():
    with pytest.raises(TypeError):
        get_positive([1, [2, 3], 4])
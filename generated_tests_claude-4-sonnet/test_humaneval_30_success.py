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

def test_empty_list():
    assert get_positive([]) == []

def test_all_positive():
    assert get_positive([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_all_negative():
    assert get_positive([-1, -2, -3, -4, -5]) == []

def test_mixed_positive_negative():
    assert get_positive([-2, -1, 0, 1, 2]) == [1, 2]

def test_with_zero():
    assert get_positive([0, 1, 2]) == [1, 2]
    assert get_positive([-1, 0, 1]) == [1]
    assert get_positive([0]) == []

def test_with_floats():
    assert get_positive([1.5, -2.3, 0.1, -0.5]) == [1.5, 0.1]

def test_single_positive():
    assert get_positive([5]) == [5]

def test_single_negative():
    assert get_positive([-5]) == []

def test_single_zero():
    assert get_positive([0]) == []

def test_large_numbers():
    assert get_positive([1000000, -1000000, 999999]) == [1000000, 999999]

def test_very_small_positive():
    assert get_positive([0.0001, -0.0001, 0]) == [0.0001]

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3], [1, 2, 3]),
    ([-1, -2, -3], []),
    ([0, 0, 0], []),
    ([1, -1, 2, -2], [1, 2]),
    ([10, 20, 30, 40], [10, 20, 30, 40])
])
def test_parametrized_cases(input_list, expected):
    assert get_positive(input_list) == expected

def test_with_none_values():
    with pytest.raises(TypeError):
        get_positive([1, None, 2])

def test_with_string_values():
    with pytest.raises(TypeError):
        get_positive([1, "2", 3])

def test_with_boolean_values():
    assert get_positive([True, False, 1, 0]) == [True, 1]

def test_preserves_order():
    assert get_positive([5, 1, 9, 2, 8]) == [5, 1, 9, 2, 8]

def test_duplicate_values():
    assert get_positive([1, 1, 2, 2, -1, -1]) == [1, 1, 2, 2]

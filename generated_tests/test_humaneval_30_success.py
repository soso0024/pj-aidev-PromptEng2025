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
    assert get_positive([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_get_positive_all_negative():
    assert get_positive([-1, -2, -3, -4, -5]) == []

def test_get_positive_mixed_numbers():
    assert get_positive([-1, 2, -3, 4, 0, 5, -6]) == [2, 4, 5]

def test_get_positive_with_zero():
    assert get_positive([0, 1, 0, 2, 0]) == [1, 2]

def test_get_positive_single_element():
    assert get_positive([1]) == [1]
    assert get_positive([-1]) == []
    assert get_positive([0]) == []

@pytest.mark.parametrize("input_list,expected", [
    ([1.5, -2.5, 3.5], [1.5, 3.5]),
    ([0.1, -0.1, 0], [0.1]),
    ([-0.5, -1.5, -2.5], [])
])
def test_get_positive_floating_points(input_list, expected):
    assert get_positive(input_list) == expected

def test_get_positive_large_numbers():
    assert get_positive([1000000, -1000000]) == [1000000]

def test_get_positive_type_error():
    with pytest.raises(TypeError):
        get_positive(None)
    with pytest.raises(TypeError):
        get_positive("not a list")
    with pytest.raises(TypeError):
        get_positive(123)

def test_get_positive_invalid_elements():
    with pytest.raises(TypeError):
        get_positive(['a', 'b', 'c'])
    with pytest.raises(TypeError):
        get_positive([1, 'b', 3])
    with pytest.raises(TypeError):
        get_positive([None, 1, 2])

# Test cases for HumanEval/47
# Generated using Claude API



def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    l = sorted(l)
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    else:
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2.0


# Generated test cases:
import pytest
import math

def test_median_odd_length():
    assert median([1, 2, 3]) == 2
    assert median([3, 1, 2]) == 2
    assert median([5, 2, 1, 4, 3]) == 3

def test_median_even_length():
    assert median([1, 2, 3, 4]) == 2.5
    assert median([4, 1, 3, 2]) == 2.5
    assert median([6, 4, 2, 1, 3, 5]) == 3.5

def test_median_single_element():
    assert median([1]) == 1
    assert median([42]) == 42

def test_median_duplicate_values():
    assert median([1, 1, 1]) == 1
    assert median([1, 2, 2, 1]) == 1.5

def test_median_negative_numbers():
    assert median([-1, -2, -3]) == -2
    assert median([-4, -1, -3, -2]) == -2.5

def test_median_mixed_numbers():
    assert median([-1, 0, 1]) == 0
    assert median([-2, -1, 0, 1]) == -0.5

def test_median_float_values():
    assert math.isclose(median([1.5, 2.5, 3.5]), 2.5)
    assert math.isclose(median([1.1, 2.2, 3.3, 4.4]), 2.75)

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3], 2),
    ([4, 2, 1, 3], 2.5),
    ([1], 1),
    ([1, 1, 1], 1),
    ([-1, 0, 1], 0),
    ([2.5, 1.5, 3.5], 2.5)
])
def test_median_parametrized(input_list, expected):
    assert math.isclose(median(input_list), expected)

def test_median_empty_list():
    with pytest.raises(IndexError):
        median([])

def test_median_non_numeric():
    with pytest.raises(TypeError):
        median(['a', 'b', 'c'])
    with pytest.raises(TypeError):
        median([None, None])

def test_median_mixed_types():
    with pytest.raises(TypeError):
        median([1, 'a', 2.5])
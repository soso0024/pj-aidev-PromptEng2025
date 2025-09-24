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

def test_median_empty_list():
    with pytest.raises(ValueError):
        median([])

def test_median_single_element():
    assert median([5]) == 5

@pytest.mark.parametrize("input_list,expected", [
    ([3, 1, 2, 4, 5], 3),
    ([-10, 4, 6, 1000, 10, 20], 15.0),
    ([1, 2, 3, 4, 5, 6], 3.5),
    ([1, 1, 2, 2, 3, 3], 2),
    ([-1, -1, 0, 0, 1, 1], 0)
])
def test_median_normal_cases(input_list, expected):
    assert median(input_list) == expected

def test_median_non_numeric_elements():
    with pytest.raises(TypeError):
        median([1, 2, "3", 4, 5])
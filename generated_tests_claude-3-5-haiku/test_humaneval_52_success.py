# Test cases for HumanEval/52
# Generated using Claude API



def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """

    for e in l:
        if e >= t:
            return False
    return True


# Generated test cases:
import pytest

def test_below_threshold_empty_list():
    assert below_threshold([], 10) == True

def test_below_threshold_all_below():
    assert below_threshold([1, 2, 3, 4], 5) == True

def test_below_threshold_one_equal():
    assert below_threshold([1, 2, 5, 3], 5) == False

def test_below_threshold_one_above():
    assert below_threshold([1, 2, 6, 3], 5) == False

def test_below_threshold_all_above():
    assert below_threshold([6, 7, 8], 5) == False

@pytest.mark.parametrize("input_list,threshold,expected", [
    ([], 10, True),
    ([1, 2, 3], 4, True),
    ([4, 5, 6], 4, False),
    ([3, 3, 3], 3, False),
    ([0, 1, 2], 3, True)
])
def test_below_threshold_parametrized(input_list, threshold, expected):
    assert below_threshold(input_list, threshold) == expected

def test_below_threshold_negative_numbers():
    assert below_threshold([-1, -2, -3], 0) == True
    assert below_threshold([-1, 0, 1], 0) == False

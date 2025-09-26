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

def below_threshold(l: list, t: int):
    for e in l:
        if e >= t:
            return False
    return True

def test_below_threshold_all_below():
    assert below_threshold([1, 2, 4, 10], 100) == True

def test_below_threshold_some_above():
    assert below_threshold([1, 20, 4, 10], 5) == False

def test_below_threshold_empty_list():
    assert below_threshold([], 10) == True

def test_below_threshold_single_element_below():
    assert below_threshold([5], 10) == True

def test_below_threshold_single_element_above():
    assert below_threshold([15], 10) == False

def test_below_threshold_single_element_equal():
    assert below_threshold([10], 10) == False

def test_below_threshold_all_equal():
    assert below_threshold([5, 5, 5], 5) == False

def test_below_threshold_negative_numbers():
    assert below_threshold([-5, -10, -1], 0) == True

def test_below_threshold_negative_threshold():
    assert below_threshold([1, 2, 3], -5) == False

def test_below_threshold_mixed_positive_negative():
    assert below_threshold([-5, 0, 3], 5) == True

def test_below_threshold_zero_threshold():
    assert below_threshold([-1, -2, -3], 0) == True

def test_below_threshold_zero_in_list():
    assert below_threshold([0, 1, 2], 3) == True

def test_below_threshold_large_numbers():
    assert below_threshold([999, 1000, 1001], 1002) == True

@pytest.mark.parametrize("input_list,threshold,expected", [
    ([1, 2, 3], 4, True),
    ([1, 2, 3], 3, False),
    ([1, 2, 3], 2, False),
    ([0], 1, True),
    ([0], 0, False),
    ([-1, -2], -3, False),
    ([-5, -4], -3, True)
])
def test_below_threshold_parametrized(input_list, threshold, expected):
    assert below_threshold(input_list, threshold) == expected

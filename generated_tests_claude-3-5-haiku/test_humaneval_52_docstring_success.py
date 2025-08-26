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

def test_below_threshold_all_below():
    assert below_threshold([1, 2, 4, 10], 100) == True

def test_below_threshold_some_above():
    assert below_threshold([1, 20, 4, 10], 5) == False

def test_below_threshold_empty_list():
    assert below_threshold([], 10) == True

def test_below_threshold_single_element_below():
    assert below_threshold([5], 10) == True

def test_below_threshold_single_element_equal():
    assert below_threshold([10], 10) == False

def test_below_threshold_single_element_above():
    assert below_threshold([11], 10) == False

@pytest.mark.parametrize("input_list,threshold,expected", [
    ([1, 2, 3], 4, True),
    ([1, 2, 4], 4, False),
    ([-1, -2, -3], 0, True),
    ([0, 0, 0], 1, True),
    ([1, 1, 1], 1, False)
])
def test_below_threshold_parametrized(input_list, threshold, expected):
    assert below_threshold(input_list, threshold) == expected

def test_below_threshold_large_numbers():
    assert below_threshold([10000, 20000, 30000], 50000) == True

def test_below_threshold_large_numbers_fail():
    assert below_threshold([10000, 50000, 30000], 50000) == False

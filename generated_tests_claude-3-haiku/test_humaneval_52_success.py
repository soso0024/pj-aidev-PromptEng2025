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
    assert below_threshold([], 10)

def test_below_threshold_all_elements_below():
    assert below_threshold([5, 7, 3, 1], 10)

def test_below_threshold_some_elements_above():
    assert not below_threshold([5, 15, 3, 1], 10)

def test_below_threshold_single_element_above():
    assert not below_threshold([5, 15, 3], 10)

def test_below_threshold_single_element_equal():
    assert not below_threshold([10], 10)

@pytest.mark.parametrize("input_list,threshold,expected", [
    ([], 10, True),
    ([5, 7, 3, 1], 10, True),
    ([5, 15, 3, 1], 10, False),
    ([5, 15, 3], 10, False),
    ([10], 10, False)
])
def test_below_threshold_parametrized(input_list, threshold, expected):
    assert below_threshold(input_list, threshold) == expected

def below_threshold(l: list, t: int):
    for e in l:
        if e >= t:
            return False
    return True

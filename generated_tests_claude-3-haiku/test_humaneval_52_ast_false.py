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
    assert below_threshold([], 5) == True

def test_below_threshold_all_below():
    assert below_threshold([1, 2, 3, 4], 5) == True

def test_below_threshold_one_above():
    assert below_threshold([1, 2, 3, 6], 5) == False

@pytest.mark.parametrize("input_list,threshold,expected", [
    ([], 0, True),
    ([1, 2, 3, 4], 5, True),
    ([1, 2, 3, 6], 5, False),
    ([0, 0, 0, 0], 0, True),
    ([0, 0, 0, 1], 0, False)
])
def test_below_threshold_parametrized(input_list, threshold, expected):
    assert below_threshold(input_list, threshold) == expected

def below_threshold(l: list, t: int):
    for e in l:
        if e >= t:
            return False
    return True
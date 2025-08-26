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
    assert below_threshold([1, 2, 3], 4) == True

def test_below_threshold_some_above():
    assert below_threshold([1, 2, 5], 4) == False

def test_below_threshold_empty_list():
    assert below_threshold([], 5) == True

def test_below_threshold_equal_threshold():
    assert below_threshold([1, 2, 4], 4) == False

def test_below_threshold_negative_numbers():
    assert below_threshold([-1, -2, -3], 0) == True

def test_below_threshold_mixed_numbers():
    assert below_threshold([-1, 0, 2], 3) == True

@pytest.mark.parametrize("input_list,threshold,expected", [
    ([1, 2, 3], 4, True),
    ([1, 2, 5], 4, False),
    ([], 5, True),
    ([4, 4, 4], 4, False),
    ([-1, -2, -3], 0, True),
    ([0, 1, 2], 3, True)
])
def test_below_threshold_parametrized(input_list, threshold, expected):
    assert below_threshold(input_list, threshold) == expected

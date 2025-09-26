# Test cases for HumanEval/57
# Generated using Claude API



def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """

    if l == sorted(l) or l == sorted(l, reverse=True):
        return True
    return False


# Generated test cases:
import pytest

def monotonic(l: list):
    if l == sorted(l) or l == sorted(l, reverse=True):
        return True
    return False

def test_monotonic_increasing():
    assert monotonic([1, 2, 4, 20]) == True

def test_monotonic_decreasing():
    assert monotonic([4, 1, 0, -10]) == True

def test_not_monotonic():
    assert monotonic([1, 20, 4, 10]) == False

def test_empty_list():
    assert monotonic([]) == True

def test_single_element():
    assert monotonic([5]) == True

def test_two_elements_increasing():
    assert monotonic([1, 2]) == True

def test_two_elements_decreasing():
    assert monotonic([2, 1]) == True

def test_two_elements_equal():
    assert monotonic([1, 1]) == True

def test_all_equal_elements():
    assert monotonic([3, 3, 3, 3]) == True

def test_strictly_increasing():
    assert monotonic([1, 2, 3, 4, 5]) == True

def test_strictly_decreasing():
    assert monotonic([5, 4, 3, 2, 1]) == True

def test_increasing_with_duplicates():
    assert monotonic([1, 1, 2, 2, 3]) == True

def test_decreasing_with_duplicates():
    assert monotonic([3, 2, 2, 1, 1]) == True

def test_negative_numbers_increasing():
    assert monotonic([-10, -5, -1, 0, 5]) == True

def test_negative_numbers_decreasing():
    assert monotonic([5, 0, -1, -5, -10]) == True

def test_mixed_positive_negative_not_monotonic():
    assert monotonic([-1, 5, 2, -3]) == False

def test_floats_increasing():
    assert monotonic([1.1, 2.2, 3.3, 4.4]) == True

def test_floats_decreasing():
    assert monotonic([4.4, 3.3, 2.2, 1.1]) == True

def test_floats_not_monotonic():
    assert monotonic([1.1, 3.3, 2.2, 4.4]) == False

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3], True),
    ([3, 2, 1], True),
    ([1, 3, 2], False),
    ([0], True),
    ([], True),
    ([5, 5, 5], True),
    ([1, 1, 2], True),
    ([2, 1, 1], True),
    ([1, 2, 1], False)
])
def test_monotonic_parametrized(input_list, expected):
    assert monotonic(input_list) == expected

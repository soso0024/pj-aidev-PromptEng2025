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

def test_empty_list():
    assert monotonic([]) == True

def test_single_element():
    assert monotonic([5]) == True

def test_two_elements_ascending():
    assert monotonic([1, 2]) == True

def test_two_elements_descending():
    assert monotonic([2, 1]) == True

def test_two_elements_equal():
    assert monotonic([1, 1]) == True

def test_ascending_sequence():
    assert monotonic([1, 2, 3, 4, 5]) == True

def test_descending_sequence():
    assert monotonic([5, 4, 3, 2, 1]) == True

def test_non_monotonic_sequence():
    assert monotonic([1, 3, 2, 4]) == False

def test_ascending_with_duplicates():
    assert monotonic([1, 1, 2, 2, 3]) == True

def test_descending_with_duplicates():
    assert monotonic([3, 2, 2, 1, 1]) == True

def test_all_same_elements():
    assert monotonic([5, 5, 5, 5]) == True

def test_negative_numbers_ascending():
    assert monotonic([-5, -3, -1, 0, 2]) == True

def test_negative_numbers_descending():
    assert monotonic([2, 0, -1, -3, -5]) == True

def test_negative_numbers_non_monotonic():
    assert monotonic([-1, -5, -2, -3]) == False

def test_mixed_positive_negative():
    assert monotonic([-10, -5, 0, 5, 10]) == True

def test_floats_ascending():
    assert monotonic([1.1, 2.2, 3.3, 4.4]) == True

def test_floats_descending():
    assert monotonic([4.4, 3.3, 2.2, 1.1]) == True

def test_floats_non_monotonic():
    assert monotonic([1.1, 3.3, 2.2, 4.4]) == False

def test_large_ascending_sequence():
    assert monotonic(list(range(100))) == True

def test_large_descending_sequence():
    assert monotonic(list(range(99, -1, -1))) == True

def test_mountain_sequence():
    assert monotonic([1, 2, 3, 2, 1]) == False

def test_valley_sequence():
    assert monotonic([3, 2, 1, 2, 3]) == False

@pytest.mark.parametrize("input_list,expected", [
    ([], True),
    ([1], True),
    ([1, 2], True),
    ([2, 1], True),
    ([1, 1], True),
    ([1, 2, 3], True),
    ([3, 2, 1], True),
    ([1, 3, 2], False),
    ([1, 2, 2, 3], True),
    ([3, 2, 2, 1], True),
    ([0, 0, 0], True),
    ([-1, 0, 1], True),
    ([1, 0, -1], True),
    ([1, -1, 0], False)
])
def test_monotonic_parametrized(input_list, expected):
    assert monotonic(input_list) == expected

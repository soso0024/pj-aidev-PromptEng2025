# Test cases for HumanEval/43
# Generated using Claude API



def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    """

    for i, l1 in enumerate(l):
        for j in range(i + 1, len(l)):
            if l1 + l[j] == 0:
                return True
    return False


# Generated test cases:
import pytest

def pairs_sum_to_zero(l):
    for i, l1 in enumerate(l):
        for j in range(i + 1, len(l)):
            if l1 + l[j] == 0:
                return True
    return False

def test_pairs_sum_to_zero_empty_list():
    assert pairs_sum_to_zero([]) == False

def test_pairs_sum_to_zero_single_element():
    assert pairs_sum_to_zero([1]) == False
    assert pairs_sum_to_zero([0]) == False
    assert pairs_sum_to_zero([-5]) == False

def test_pairs_sum_to_zero_two_elements_sum_to_zero():
    assert pairs_sum_to_zero([1, -1]) == True
    assert pairs_sum_to_zero([5, -5]) == True
    assert pairs_sum_to_zero([0, 0]) == True
    assert pairs_sum_to_zero([-3, 3]) == True

def test_pairs_sum_to_zero_two_elements_no_sum():
    assert pairs_sum_to_zero([1, 2]) == False
    assert pairs_sum_to_zero([5, 3]) == False
    assert pairs_sum_to_zero([-1, -2]) == False

def test_pairs_sum_to_zero_multiple_elements_with_pairs():
    assert pairs_sum_to_zero([1, 3, -2, 2]) == True
    assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
    assert pairs_sum_to_zero([1, -1, 2, 3]) == True
    assert pairs_sum_to_zero([0, 1, 2, 0]) == True
    assert pairs_sum_to_zero([10, -5, 3, 5, -10]) == True

def test_pairs_sum_to_zero_multiple_elements_no_pairs():
    assert pairs_sum_to_zero([1, 3, 5, 0]) == False
    assert pairs_sum_to_zero([1, 3, -2, 1]) == False
    assert pairs_sum_to_zero([1, 2, 3, 7]) == False
    assert pairs_sum_to_zero([1, 2, 3, 4, 5]) == False
    assert pairs_sum_to_zero([-1, -2, -3, -4]) == False

def test_pairs_sum_to_zero_all_zeros():
    assert pairs_sum_to_zero([0, 0]) == True
    assert pairs_sum_to_zero([0, 0, 0]) == True
    assert pairs_sum_to_zero([0, 0, 0, 0]) == True

def test_pairs_sum_to_zero_duplicates():
    assert pairs_sum_to_zero([1, 1, -1]) == True
    assert pairs_sum_to_zero([2, 2, 2, -2]) == True
    assert pairs_sum_to_zero([3, 3, 3, 3]) == False
    assert pairs_sum_to_zero([1, 1, 1, 1]) == False

def test_pairs_sum_to_zero_large_numbers():
    assert pairs_sum_to_zero([1000, -1000]) == True
    assert pairs_sum_to_zero([999, 1000, -999]) == True
    assert pairs_sum_to_zero([1000, 2000, 3000]) == False

@pytest.mark.parametrize("input_list,expected", [
    ([1, 3, 5, 0], False),
    ([1, 3, -2, 1], False),
    ([1, 2, 3, 7], False),
    ([2, 4, -5, 3, 5, 7], True),
    ([1], False),
    ([], False),
    ([0, 0], True),
    ([1, -1], True),
    ([-5, 10, 5, -10], True),
    ([1, 2, 3, 4, 5, 6], False)
])
def test_pairs_sum_to_zero_parametrized(input_list, expected):
    assert pairs_sum_to_zero(input_list) == expected

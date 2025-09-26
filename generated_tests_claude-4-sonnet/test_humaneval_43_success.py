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

def test_empty_list():
    assert pairs_sum_to_zero([]) == False

def test_single_element():
    assert pairs_sum_to_zero([5]) == False
    assert pairs_sum_to_zero([0]) == False

def test_two_elements_sum_to_zero():
    assert pairs_sum_to_zero([1, -1]) == True
    assert pairs_sum_to_zero([-5, 5]) == True
    assert pairs_sum_to_zero([0, 0]) == True

def test_two_elements_no_sum_to_zero():
    assert pairs_sum_to_zero([1, 2]) == False
    assert pairs_sum_to_zero([-3, -4]) == False
    assert pairs_sum_to_zero([10, 5]) == False

def test_multiple_elements_with_zero_sum_pair():
    assert pairs_sum_to_zero([1, 2, -1, 4]) == True
    assert pairs_sum_to_zero([3, -2, 1, -1, 5]) == True
    assert pairs_sum_to_zero([10, -5, 3, 5, -10]) == True
    assert pairs_sum_to_zero([1, 2, 3, -3, 4]) == True

def test_multiple_elements_no_zero_sum_pair():
    assert pairs_sum_to_zero([1, 2, 3, 4]) == False
    assert pairs_sum_to_zero([-1, -2, -3, -4]) == False
    assert pairs_sum_to_zero([5, 10, 15, 20]) == False

def test_multiple_zeros():
    assert pairs_sum_to_zero([0, 0, 0]) == True
    assert pairs_sum_to_zero([1, 0, 0, 2]) == True

def test_zero_with_other_numbers():
    assert pairs_sum_to_zero([0, 1, 2, 3]) == False
    assert pairs_sum_to_zero([5, 0, -5, 3]) == True

def test_duplicate_numbers():
    assert pairs_sum_to_zero([3, 3, -3, 4]) == True
    assert pairs_sum_to_zero([2, 2, 2, 2]) == False
    assert pairs_sum_to_zero([1, 1, -1, -1]) == True

def test_large_numbers():
    assert pairs_sum_to_zero([1000000, -1000000]) == True
    assert pairs_sum_to_zero([999999, 1000000, -999999]) == True

def test_floating_point_numbers():
    assert pairs_sum_to_zero([1.5, -1.5]) == True
    assert pairs_sum_to_zero([2.7, 3.3, -2.7]) == True
    assert pairs_sum_to_zero([1.1, 2.2, 3.3]) == False

@pytest.mark.parametrize("input_list,expected", [
    ([], False),
    ([1], False),
    ([1, -1], True),
    ([1, 2, 3], False),
    ([1, 2, -1], True),
    ([0, 0], True),
    ([5, -3, 3, -5], True),
    ([1, 2, 4, 8], False)
])
def test_parametrized_cases(input_list, expected):
    assert pairs_sum_to_zero(input_list) == expected

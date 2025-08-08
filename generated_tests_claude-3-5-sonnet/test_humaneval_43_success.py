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

def test_empty_list():
    assert pairs_sum_to_zero([]) == False

def test_single_element():
    assert pairs_sum_to_zero([1]) == False

def test_two_elements_sum_zero():
    assert pairs_sum_to_zero([1, -1]) == True

def test_two_elements_no_sum_zero():
    assert pairs_sum_to_zero([1, 1]) == False

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, -2], True),
    ([1, 2, 3, 4], False),
    ([-1, -2, -3, -4], False),
    ([0, 0], True),
    ([1, -1, 2, -2], True),
    ([1.5, -1.5], True),
    ([-1, 2, 3, -3], True),
    ([10, -5, 5, -10], True),
    ([1, 2, 3, 4, 5], False),
    ([-1, -2, -3, -4, -5], False)
])
def test_various_lists(input_list, expected):
    assert pairs_sum_to_zero(input_list) == expected

def test_large_numbers():
    assert pairs_sum_to_zero([1000000, -1000000]) == True

def test_small_numbers():
    assert pairs_sum_to_zero([0.0001, -0.0001]) == True

def test_mixed_types():
    assert pairs_sum_to_zero([1, -1.0]) == True

def test_all_zeros():
    assert pairs_sum_to_zero([0, 0, 0, 0]) == True

def test_repeated_numbers():
    assert pairs_sum_to_zero([1, 1, -1, -1]) == True

@pytest.mark.parametrize("invalid_input", [
    None,
    123,
    True,
    [1, "2", 3]
])
def test_invalid_inputs(invalid_input):
    with pytest.raises((TypeError, ValueError)):
        pairs_sum_to_zero(invalid_input)
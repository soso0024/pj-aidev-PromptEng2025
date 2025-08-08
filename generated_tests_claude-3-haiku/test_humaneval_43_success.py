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

def test_pairs_sum_to_zero_empty_list():
    assert not pairs_sum_to_zero([])

def test_pairs_sum_to_zero_single_element_list():
    assert not pairs_sum_to_zero([1])

def test_pairs_sum_to_zero_two_elements_sum_to_zero():
    assert pairs_sum_to_zero([-1, 1])

def test_pairs_sum_to_zero_two_elements_do_not_sum_to_zero():
    assert not pairs_sum_to_zero([1, 2])

def test_pairs_sum_to_zero_multiple_pairs_sum_to_zero():
    assert pairs_sum_to_zero([-2, -1, 1, 2])

def test_pairs_sum_to_zero_no_pairs_sum_to_zero():
    assert not pairs_sum_to_zero([1, 2, 3, 4])

@pytest.mark.parametrize("input,expected", [
    ([0, 0], True),
    ([-1, 0, 1], True),
    ([1, 2, 3, 4, 5], False),
    ([-5, -4, -3, -2, -1], False),
    ([0, 0, 0, 0], True),
    ([-1, -1, 1, 1], True),
])
def test_pairs_sum_to_zero_parametrized(input, expected):
    assert pairs_sum_to_zero(input) == expected

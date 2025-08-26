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
    assert pairs_sum_to_zero([]) is False

def test_pairs_sum_to_zero_single_element():
    assert pairs_sum_to_zero([1]) is False

@pytest.mark.parametrize("input_list,expected", [
    ([1, -1], True),
    ([2, -2], True),
    ([3, -3], True),
    ([1, 2, -3], True),
    ([1, 2, 3], False),
    ([1, 1, -2], True),
    ([0, 0], True),
    ([0, 1, -1], True),
    ([1, 1, 1], False),
    ([1, 1, 1, -2], True)
])
def test_pairs_sum_to_zero(input_list, expected):
    assert pairs_sum_to_zero(input_list) == expected
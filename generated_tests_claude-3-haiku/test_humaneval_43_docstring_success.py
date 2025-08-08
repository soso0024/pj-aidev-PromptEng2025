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

def test_pairs_sum_to_zero_single_element():
    assert not pairs_sum_to_zero([1])

def test_pairs_sum_to_zero_no_pairs():
    assert not pairs_sum_to_zero([1, 3, 5, 0])

def test_pairs_sum_to_zero_one_pair():
    assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7])

def test_pairs_sum_to_zero_multiple_pairs():
    assert pairs_sum_to_zero([1, 3, -2, 1, 2, -2])

def test_pairs_sum_to_zero_negative_numbers():
    assert pairs_sum_to_zero([-1, -3, 2, 1, -2])

def test_pairs_sum_to_zero_duplicate_elements():
    assert pairs_sum_to_zero([1, 2, -1, 1, 3, -2])

@pytest.mark.parametrize("input,expected", [
    ([1, 3, -2, 1], False),
    ([1, 2, 3, 7], False),
    ([2, 4, -5, 3, 5, 7], True),
    ([1], False),
])
def test_pairs_sum_to_zero_examples(input, expected):
    assert pairs_sum_to_zero(input) == expected

def pairs_sum_to_zero(l):
    for i, l1 in enumerate(l):
        for j in range(i + 1, len(l)):
            if l1 + l[j] == 0:
                return True
    return False

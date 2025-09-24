# Test cases for HumanEval/40
# Generated using Claude API



def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> triples_sum_to_zero([1, 3, 5, 0])
    False
    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    """

    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                if l[i] + l[j] + l[k] == 0:
                    return True
    return False


# Generated test cases:
import pytest

def triples_sum_to_zero(l: list):
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                if l[i] + l[j] + l[k] == 0:
                    return True
    return False

@pytest.mark.parametrize("input_list,expected", [
    ([1, 3, 5, 0], False),
    ([1, 3, -2, 1], True),
    ([1, 2, 3, 7], False),
    ([2, 4, -5, 3, 9, 7], True),
    ([1], False),
    ([1, 2], False),
    ([0, 0, 0], True),
    ([1, -1, 0], True),
    ([5, -5, 0], True),
    ([1, 2, -3], True),
    ([10, -5, -5], True),
    ([1, 1, 1], False),
    ([-1, -1, -1], False),
    ([0, 1, 2], False),
    ([3, 5, -1, -5, -3, 1], False),
    ([100, -50, -50], True),
    ([1, 2, 3, 4, 5], False),
    ([-1, -2, -3, -4, -5], False),
    ([0], False),
    ([], False),
    ([0, 0, 1], False),
    ([0, 1, -1], True),
    ([2, -1, -1], True),
    ([3, -1, -2], True),
    ([1, 1, -2], True),
    ([5, 5, -10], True),
    ([1, 2, 3, 4, -6], True),
    ([10, 20, 30], False),
    ([-10, -20, -30], False),
    ([0, 0, 0, 0], True),
    ([1, 1, 1, -3], False),
    ([2, 2, 2, -6], False)
])
def test_triples_sum_to_zero(input_list, expected):
    assert triples_sum_to_zero(input_list) == expected

def test_empty_list():
    assert triples_sum_to_zero([]) == False

def test_single_element():
    assert triples_sum_to_zero([5]) == False

def test_two_elements():
    assert triples_sum_to_zero([1, -1]) == False

def test_all_zeros():
    assert triples_sum_to_zero([0, 0, 0, 0, 0]) == True

def test_large_numbers():
    assert triples_sum_to_zero([1000000, -500000, -500000]) == True

def test_negative_numbers():
    assert triples_sum_to_zero([-1, -2, 3]) == True

def test_mixed_positive_negative():
    assert triples_sum_to_zero([1, -1, 2, -2, 0]) == True

def test_no_valid_triple():
    assert triples_sum_to_zero([1, 2, 4, 8]) == False
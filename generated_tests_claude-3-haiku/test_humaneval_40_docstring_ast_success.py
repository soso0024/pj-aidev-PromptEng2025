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
from collections import Counter
from itertools import combinations

@pytest.mark.parametrize("input_list,expected", [
    ([1, 3, 5, 0], False),
    ([1, 3, -2, 1], True),
    ([1, 2, 3, 7], False),
    ([2, 4, -5, 3, 9, 7], True),
    ([1], False),
    ([], False),
    ([0, 0, 0], True),
    ([-1, 0, 1], True),
    ([1, 1, -2], True),
    ([1, 2, -3], True),
    ([1, 2, 3], False),
    ([1, 1, 1], False),
    ([0, 0, 0, 0], True),
    ([-1, -1, 2], True),
    ([1, -1, 0], True)
])
def test_triples_sum_to_zero(input_list, expected):
    assert triples_sum_to_zero(input_list) == expected
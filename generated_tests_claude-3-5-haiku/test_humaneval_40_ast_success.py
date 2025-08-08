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

def test_triples_sum_to_zero_positive_case():
    assert triples_sum_to_zero([-1, 0, 1]) == True
    assert triples_sum_to_zero([3, 1, -4, 2, -2]) == True

def test_triples_sum_to_zero_negative_case():
    assert triples_sum_to_zero([1, 2, 3]) == False
    assert triples_sum_to_zero([5, 7, 9]) == False

def test_triples_sum_to_zero_edge_cases():
    assert triples_sum_to_zero([]) == False
    assert triples_sum_to_zero([0, 0, 0]) == True
    assert triples_sum_to_zero([-1, 0, 1, 0]) == True

@pytest.mark.parametrize("input_list,expected", [
    ([-1, 0, 1], True),
    ([3, 1, -4, 2, -2], True),
    ([1, 2, 3], False),
    ([0, 0, 0], True),
    ([], False),
    ([-5, 5, 0], True)
])
def test_triples_sum_to_zero_parametrized(input_list, expected):
    assert triples_sum_to_zero(input_list) == expected

def test_triples_sum_to_zero_large_list():
    large_list = list(range(-100, 100))
    assert triples_sum_to_zero(large_list) == True

def test_triples_sum_to_zero_negative_numbers():
    assert triples_sum_to_zero([-3, -1, 4]) == True
    assert triples_sum_to_zero([-10, -5, 15]) == True

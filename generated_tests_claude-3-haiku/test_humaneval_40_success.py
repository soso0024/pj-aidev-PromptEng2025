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

def test_triples_sum_to_zero_empty_list():
    assert triples_sum_to_zero([]) == False

def test_triples_sum_to_zero_single_element_list():
    assert triples_sum_to_zero([1]) == False

def test_triples_sum_to_zero_two_element_list():
    assert triples_sum_to_zero([1, 2]) == False

def test_triples_sum_to_zero_three_element_list_with_zero_sum():
    assert triples_sum_to_zero([-1, 0, 1]) == True

def test_triples_sum_to_zero_three_element_list_without_zero_sum():
    assert triples_sum_to_zero([1, 2, 3]) == False

def test_triples_sum_to_zero_multiple_zero_sum_triples():
    assert triples_sum_to_zero([-1, -1, 2, 0, 1, 1]) == True

def test_triples_sum_to_zero_large_list_with_zero_sum():
    assert triples_sum_to_zero([-10, -5, 0, 5, 10]) == True

def test_triples_sum_to_zero_large_list_without_zero_sum():
    assert triples_sum_to_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False

@pytest.mark.parametrize("input,expected", [
    ([0, 0, 0], True),
    ([-1, -1, 2], True),
    ([1, 2, 3], False),
    ([-10, -5, 15], True),
    ([1, 1, 1], False)
])
def test_triples_sum_to_zero_parametrized(input, expected):
    assert triples_sum_to_zero(input) == expected

def triples_sum_to_zero(l: list):
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                if l[i] + l[j] + l[k] == 0:
                    return True
    return False

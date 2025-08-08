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

def test_triples_sum_to_zero_basic_true():
    assert triples_sum_to_zero([1, 3, -2, 1]) == True

def test_triples_sum_to_zero_basic_false():
    assert triples_sum_to_zero([1, 3, 5, 0]) == False

def test_triples_sum_to_zero_multiple_solutions():
    assert triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == True

def test_triples_sum_to_zero_short_list():
    assert triples_sum_to_zero([1]) == False

def test_triples_sum_to_zero_empty_list():
    assert triples_sum_to_zero([]) == False

@pytest.mark.parametrize("input_list,expected", [
    ([1, 3, -2, 1], True),
    ([1, 3, 5, 0], False),
    ([2, 4, -5, 3, 9, 7], True),
    ([1], False),
    ([], False),
    ([-1, 0, 1], True),
    ([10, -5, -5], True),
    ([1, 2, 3, 4, 5], False)
])
def test_triples_sum_to_zero_parametrized(input_list, expected):
    assert triples_sum_to_zero(input_list) == expected

def test_triples_sum_to_zero_negative_numbers():
    assert triples_sum_to_zero([-1, -2, 3]) == True

def test_triples_sum_to_zero_zero_values():
    assert triples_sum_to_zero([0, 0, 0]) == True

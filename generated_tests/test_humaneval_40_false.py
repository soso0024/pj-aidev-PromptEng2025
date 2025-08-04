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

def test_empty_list():
    assert triples_sum_to_zero([]) == False

def test_list_less_than_three_elements():
    assert triples_sum_to_zero([1]) == False
    assert triples_sum_to_zero([1, 2]) == False

def test_basic_true_cases():
    assert triples_sum_to_zero([-1, 0, 1]) == True
    assert triples_sum_to_zero([1, -2, 1]) == True
    assert triples_sum_to_zero([3, -1, -2]) == True

def test_basic_false_cases():
    assert triples_sum_to_zero([1, 2, 3]) == False
    assert triples_sum_to_zero([-1, -2, -3]) == False

def test_larger_lists():
    assert triples_sum_to_zero([1, 2, 3, -6, 3, 0, 3]) == True
    assert triples_sum_to_zero([1, 2, 3, 4, 5, 6, 7]) == False

@pytest.mark.parametrize("input_list,expected", [
    ([0, 0, 0], True),
    ([1, -1, 0], True),
    ([1, 1, -2], True),
    ([1, 2, 3], False),
    ([-1, -1, -1], False),
    ([1, 2, 3, 4, -5, -2], True),
])
def test_parametrized_cases(input_list, expected):
    assert triples_sum_to_zero(input_list) == expected

def test_with_duplicates():
    assert triples_sum_to_zero([1, 1, 1, -2]) == False
    assert triples_sum_to_zero([1, 1, -2]) == False

def test_with_negative_numbers():
    assert triples_sum_to_zero([-1, -2, -3, 6]) == False
    assert triples_sum_to_zero([-1, -2, -3, -4]) == False

@pytest.mark.parametrize("invalid_input", [
    None,
    123,
    True,
    [1, "2", 3],
])
def test_invalid_inputs(invalid_input):
    with pytest.raises((TypeError, AttributeError)):
        triples_sum_to_zero(invalid_input)
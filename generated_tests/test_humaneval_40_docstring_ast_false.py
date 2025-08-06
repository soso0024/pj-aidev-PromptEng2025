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

def test_basic_true_case():
    assert triples_sum_to_zero([1, 3, -2, 1]) == True

def test_basic_false_case():
    assert triples_sum_to_zero([1, 3, 5, 0]) == False

def test_empty_list():
    assert triples_sum_to_zero([]) == False

def test_single_element():
    assert triples_sum_to_zero([1]) == False

def test_two_elements():
    assert triples_sum_to_zero([1, -1]) == False

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, 7], False),
    ([2, 4, -5, 3, 9, 7], True),
    ([0, 0, 0], True),
    ([-1, -1, 2], True),
    ([1, 1, -2], True),
    ([1, 2, 3, 4, 5], False),
    ([-5, -4, -3, -2, -1], False),
    ([10, -5, -5], True),
    ([1, 2, 3, -6, 4, 5], True),
    ([0, 1, 2, 3], False)
])
def test_various_cases(input_list, expected):
    assert triples_sum_to_zero(input_list) == expected

def test_large_numbers():
    assert triples_sum_to_zero([1000, -500, -500, 2000]) == True

def test_all_negative():
    assert triples_sum_to_zero([-1, -2, -3, -4]) == False

def test_all_positive():
    assert triples_sum_to_zero([1, 2, 3, 4]) == False

def test_with_duplicates():
    assert triples_sum_to_zero([1, 1, 1, -2]) == True

@pytest.mark.parametrize("input_list", [
    None,
    123,
    3.14
])
def test_invalid_input_types(input_list):
    with pytest.raises(TypeError):
        triples_sum_to_zero(input_list)

def test_string_input():
    with pytest.raises(TypeError):
        triples_sum_to_zero("string")

def test_list_with_non_numbers():
    with pytest.raises(TypeError):
        triples_sum_to_zero([1, "2", 3])
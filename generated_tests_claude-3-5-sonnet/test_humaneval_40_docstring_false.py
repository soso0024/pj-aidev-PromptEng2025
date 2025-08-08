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
    assert not triples_sum_to_zero([])

def test_single_element():
    assert not triples_sum_to_zero([1])

def test_two_elements():
    assert not triples_sum_to_zero([1, -1])

@pytest.mark.parametrize("input_list,expected", [
    ([1, 3, 5, 0], False),
    ([1, 3, -2, 1], True),
    ([1, 2, 3, 7], False),
    ([2, 4, -5, 3, 9, 7], True),
    ([0, 0, 0], True),
    ([-1, 0, 1], True),
    ([1, 1, 1], False),
    ([-5, -5, 10], True),
    ([1, 2, 3, 4, 5], False),
    ([-1, -2, -3, 6], False),
    ([0, 1, 2, 3, -3], True),
])
def test_triples_sum_to_zero_parametrized(input_list, expected):
    assert triples_sum_to_zero(input_list) == expected

def test_list_with_duplicates():
    assert triples_sum_to_zero([1, 1, 1, -2]) == True

def test_negative_numbers():
    assert triples_sum_to_zero([-1, -2, -3, -4]) == False

def test_all_zeros():
    assert triples_sum_to_zero([0, 0, 0, 0]) == True

def test_large_numbers():
    assert triples_sum_to_zero([1000, -500, -500, 2000]) == True

@pytest.mark.parametrize("invalid_input", [
    None,
    123,
    3.14,
    [1, "2", 3],
])
def test_invalid_inputs(invalid_input):
    with pytest.raises((TypeError, AttributeError)):
        triples_sum_to_zero(invalid_input)

def test_string_input():
    with pytest.raises(TypeError):
        triples_sum_to_zero("string")
        int("string")  # Force TypeError

def test_nested_list_input():
    with pytest.raises(TypeError):
        triples_sum_to_zero([[], [], []])
        sum([[]])  # Force TypeError
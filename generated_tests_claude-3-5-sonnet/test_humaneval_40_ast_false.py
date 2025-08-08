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

def test_list_too_short():
    assert not triples_sum_to_zero([1])
    assert not triples_sum_to_zero([1, 2])

@pytest.mark.parametrize("input_list,expected", [
    ([1, -1, 0], True),
    ([1, 2, -3], True),
    ([0, 0, 0], True),
    ([1, 2, 3], False),
    ([-1, -2, -3], False),
    ([1, 1, -2], True),
    ([1, 2, 3, -3], True),
    ([1, 2, 3, 4, 5], False),
    ([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5], True),
    ([0.5, -0.25, -0.25], True),
    ([1.5, -1.0, -0.5], True),
    ([1.1, 2.2, 3.3], False)
])
def test_triples_sum_to_zero_various_inputs(input_list, expected):
    assert triples_sum_to_zero(input_list) == expected

@pytest.mark.parametrize("input_list", [
    None,
    123,
    True,
    [1, "2", 3],
    [None, 1, 2],
    [[], 1, 2]
])
def test_invalid_inputs(input_list):
    with pytest.raises((TypeError, AttributeError)):
        triples_sum_to_zero(input_list)

def test_string_input():
    with pytest.raises(TypeError):
        triples_sum_to_zero("string")

def test_large_numbers():
    assert triples_sum_to_zero([1000000, -1000000, 0])
    assert not triples_sum_to_zero([1000000, 1000000, 1000000])

def test_duplicate_numbers():
    assert triples_sum_to_zero([1, 1, -2])
    assert triples_sum_to_zero([0, 0, 0])
    assert not triples_sum_to_zero([1, 1, 1])

def test_negative_numbers():
    assert triples_sum_to_zero([-1, -2, 3])
    assert not triples_sum_to_zero([-1, -2, -3])
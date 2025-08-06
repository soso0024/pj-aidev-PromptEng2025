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

def test_empty_list():
    assert pairs_sum_to_zero([]) == False

def test_single_element():
    assert pairs_sum_to_zero([1]) == False

def test_two_elements_sum_zero():
    assert pairs_sum_to_zero([1, -1]) == True

def test_two_elements_no_sum_zero():
    assert pairs_sum_to_zero([1, 1]) == False

@pytest.mark.parametrize("input_list,expected", [
    ([1, 3, 5, 0], False),
    ([1, 3, -2, 1], False),
    ([1, 2, 3, 7], False),
    ([2, 4, -5, 3, 5, 7], True),
    ([0, 0], False),
    ([-5, 2, 3, 5, -2], True),
    ([1, 2, 3, -3], True),
    ([100, -100, 50, 25], True),
    ([1, 1, 1, 1], False),
    ([-1, -2, -3, -4], False)
])
def test_pairs_sum_to_zero_parametrized(input_list, expected):
    assert pairs_sum_to_zero(input_list) == expected

def test_list_with_zeros():
    assert pairs_sum_to_zero([0, 0, 1, 2]) == False

def test_large_numbers():
    assert pairs_sum_to_zero([1000000, -1000000]) == True

def test_all_negative():
    assert pairs_sum_to_zero([-1, -2, -3, -4]) == False

def test_duplicate_numbers():
    assert pairs_sum_to_zero([1, 1, -1, -1]) == True

def test_mixed_types():
    with pytest.raises(TypeError):
        pairs_sum_to_zero([1, "2", 3, -1])

def test_none_in_list():
    with pytest.raises(TypeError):
        pairs_sum_to_zero([1, None, -1])

def test_invalid_input_type():
    with pytest.raises(TypeError):
        pairs_sum_to_zero("not a list")
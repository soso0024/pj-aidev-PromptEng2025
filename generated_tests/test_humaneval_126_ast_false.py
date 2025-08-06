# Test cases for HumanEval/126
# Generated using Claude API


def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Examples
    is_sorted([5]) ➞ True
    is_sorted([1, 2, 3, 4, 5]) ➞ True
    is_sorted([1, 3, 2, 4, 5]) ➞ False
    is_sorted([1, 2, 3, 4, 5, 6]) ➞ True
    is_sorted([1, 2, 3, 4, 5, 6, 7]) ➞ True
    is_sorted([1, 3, 2, 4, 5, 6, 7]) ➞ False
    is_sorted([1, 2, 2, 3, 3, 4]) ➞ True
    is_sorted([1, 2, 2, 2, 3, 4]) ➞ False
    '''

    count_digit = dict([(i, 0) for i in lst])
    for i in lst:
        count_digit[i]+=1 
    if any(count_digit[i] > 2 for i in lst):
        return False
    if all(lst[i-1] <= lst[i] for i in range(1, len(lst))):
        return True
    else:
        return False
    
    


# Generated test cases:
import pytest

def test_empty_list():
    assert is_sorted([]) is True

def test_single_element():
    assert is_sorted([1]) is True

def test_two_identical_elements():
    assert is_sorted([1, 1]) is True

def test_three_identical_elements():
    assert is_sorted([1, 1, 1]) is False

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, 4, 5], True),
    ([5, 4, 3, 2, 1], False),
    ([1, 1, 2, 2], True),
    ([1, 2, 2, 1], False),
    ([1, 2, 2, 2], False),
    ([0, 0, 1, 1], True),
    ([1, 2, 3], True),
    ([1, 2, 3], True),
    ([3, 2, 1], False),
    ([1, 2, 2, 3], True),
    ([1, 1, 1, 1], False),
    ([0], True),
    ([1, 1], True),
    ([2, 2, 2], False),
    ([1, 2, 3, 3, 3], False)
])
def test_is_sorted_parametrized(input_list, expected):
    assert is_sorted(input_list) == expected

@pytest.mark.parametrize("input_list", [
    [1, 2, None],
    [None, 1, 2],
    [1, "2", 3],
])
def test_invalid_inputs(input_list):
    with pytest.raises(Exception):
        is_sorted(input_list)

def test_integer_only():
    with pytest.raises(TypeError):
        is_sorted([1.1, 2.2, 3.3])
    with pytest.raises(TypeError):
        is_sorted([3.3, 2.2, 1.1])

def test_positive_only():
    with pytest.raises(ValueError):
        is_sorted([-3, -2, -1])
    with pytest.raises(ValueError):
        is_sorted([-1, -2, -3])
    with pytest.raises(ValueError):
        is_sorted([-2, -1, 0, 1, 2])
    with pytest.raises(ValueError):
        is_sorted([2, 1, 0, -1, -2])
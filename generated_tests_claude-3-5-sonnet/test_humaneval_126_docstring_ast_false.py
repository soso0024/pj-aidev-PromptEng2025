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

@pytest.mark.parametrize("input_list,expected", [
    ([5], True),
    ([1, 2, 3, 4, 5], True),
    ([1, 3, 2, 4, 5], False),
    ([1, 2, 3, 4, 5, 6], True),
    ([1, 2, 3, 4, 5, 6, 7], True),
    ([1, 3, 2, 4, 5, 6, 7], False),
    ([1, 2, 2, 3, 3, 4], True),
    ([1, 2, 2, 2, 3, 4], False),
    ([], True),
    ([1], True),
    ([1, 1], True),
    ([1, 1, 1], False),
    ([2, 1], False),
    ([1, 2, 2, 3], True),
    ([3, 2, 1], False),
    ([1, 2, 3, 3, 3], False),
    ([1, 1, 2, 2, 3, 3], True),
    ([10, 20, 30, 40, 50], True),
    ([50, 40, 30, 20, 10], False),
    ([1, 2, 2, 2, 2], False)
])
def test_is_sorted(input_list, expected):
    assert is_sorted(input_list) == expected

@pytest.mark.parametrize("input_list", [
    ["a", "b", "c"],
    [None, None],
    ["1", "2", "3"]
])
def test_is_sorted_invalid_input(input_list):
    with pytest.raises(TypeError):
        is_sorted(input_list)

@pytest.mark.parametrize("input_list", [
    [-1, -2, -3],
    [1.5, 2.5, 3.5]
])
def test_is_sorted_invalid_numbers(input_list):
    with pytest.raises(ValueError):
        is_sorted(input_list)

def test_is_sorted_none_input():
    with pytest.raises(TypeError):
        is_sorted(None)
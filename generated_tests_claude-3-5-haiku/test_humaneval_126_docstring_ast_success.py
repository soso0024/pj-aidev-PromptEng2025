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

def test_is_sorted_single_element():
    assert is_sorted([5]) == True

def test_is_sorted_ascending_sequence():
    assert is_sorted([1, 2, 3, 4, 5]) == True

def test_is_sorted_unsorted_sequence():
    assert is_sorted([1, 3, 2, 4, 5]) == False

def test_is_sorted_longer_ascending_sequence():
    assert is_sorted([1, 2, 3, 4, 5, 6]) == True
    assert is_sorted([1, 2, 3, 4, 5, 6, 7]) == True

def test_is_sorted_longer_unsorted_sequence():
    assert is_sorted([1, 3, 2, 4, 5, 6, 7]) == False

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 2, 3, 3, 4], True),
    ([1, 2, 2, 2, 3, 4], False)
])
def test_is_sorted_with_duplicates(input_list, expected):
    assert is_sorted(input_list) == expected

def test_is_sorted_empty_list():
    assert is_sorted([]) == True

def test_is_sorted_all_same_elements():
    assert is_sorted([2, 2]) == True
    assert is_sorted([2, 2, 2]) == False

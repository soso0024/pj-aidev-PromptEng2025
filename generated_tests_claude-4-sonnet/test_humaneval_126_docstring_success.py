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

def is_sorted(lst):
    count_digit = dict([(i, 0) for i in lst])
    for i in lst:
        count_digit[i]+=1 
    if any(count_digit[i] > 2 for i in lst):
        return False
    if all(lst[i-1] <= lst[i] for i in range(1, len(lst))):
        return True
    else:
        return False

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
    ([1, 2, 3, 3, 3], False),
    ([5, 4, 3, 2, 1], False),
    ([1, 1, 2, 2, 3, 3], True),
    ([0, 0, 1, 1, 2, 2], True),
    ([0, 0, 0], False),
    ([10, 20, 30], True),
    ([10, 10, 20, 30], True),
    ([10, 10, 10, 20], False),
    ([1, 2, 1], False),
    ([5, 5, 6, 6, 7], True),
    ([5, 5, 5, 6, 7], False),
    ([100], True),
    ([0, 1, 2, 3], True),
    ([0, 0], True),
    ([1, 2, 3, 2], False),
    ([7, 8, 9, 10, 11], True),
    ([7, 8, 8, 9, 10], True)
])
def test_is_sorted(input_list, expected):
    assert is_sorted(input_list) == expected

def test_empty_list():
    assert is_sorted([]) == True

def test_single_element():
    assert is_sorted([42]) == True

def test_two_identical_elements():
    assert is_sorted([3, 3]) == True

def test_three_identical_elements():
    assert is_sorted([7, 7, 7]) == False

def test_ascending_no_duplicates():
    assert is_sorted([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True

def test_descending_order():
    assert is_sorted([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == False

def test_mixed_order():
    assert is_sorted([1, 3, 2, 5, 4]) == False

def test_large_numbers():
    assert is_sorted([100, 200, 300, 400, 500]) == True

def test_zeros():
    assert is_sorted([0, 0, 1, 2, 3]) == True
    assert is_sorted([0, 0, 0, 1, 2]) == False

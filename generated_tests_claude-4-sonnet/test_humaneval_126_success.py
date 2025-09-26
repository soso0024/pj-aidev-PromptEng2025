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

def test_empty_list():
    assert is_sorted([]) == True

def test_single_element():
    assert is_sorted([1]) == True
    assert is_sorted([0]) == True
    assert is_sorted([-1]) == True

def test_two_elements_sorted():
    assert is_sorted([1, 2]) == True
    assert is_sorted([1, 1]) == True
    assert is_sorted([-1, 0]) == True

def test_two_elements_not_sorted():
    assert is_sorted([2, 1]) == False

def test_sorted_ascending():
    assert is_sorted([1, 2, 3, 4, 5]) == True
    assert is_sorted([-3, -1, 0, 2, 5]) == True

def test_sorted_with_duplicates():
    assert is_sorted([1, 1, 2, 3]) == True
    assert is_sorted([1, 2, 2, 3]) == True
    assert is_sorted([1, 1, 2, 2]) == True

def test_not_sorted():
    assert is_sorted([3, 2, 1]) == False
    assert is_sorted([1, 3, 2]) == False
    assert is_sorted([5, 1, 2, 3]) == False

def test_more_than_two_duplicates():
    assert is_sorted([1, 1, 1]) == False
    assert is_sorted([2, 2, 2, 3]) == False
    assert is_sorted([1, 2, 2, 2]) == False
    assert is_sorted([1, 1, 1, 2, 2, 2]) == False

def test_sorted_but_too_many_duplicates():
    assert is_sorted([1, 1, 1, 2]) == False
    assert is_sorted([1, 2, 3, 3, 3]) == False

def test_negative_numbers():
    assert is_sorted([-5, -3, -1]) == True
    assert is_sorted([-1, -3, -5]) == False
    assert is_sorted([-2, -2, -1]) == True
    assert is_sorted([-2, -2, -2]) == False

def test_mixed_positive_negative():
    assert is_sorted([-2, -1, 0, 1, 2]) == True
    assert is_sorted([-1, -1, 0, 1, 1]) == True
    assert is_sorted([2, -1, 0, 1]) == False

def test_all_same_elements():
    assert is_sorted([5, 5]) == True
    assert is_sorted([0, 0]) == True
    assert is_sorted([-1, -1]) == True

def test_floating_point_numbers():
    assert is_sorted([1.1, 2.2, 3.3]) == True
    assert is_sorted([3.3, 2.2, 1.1]) == False
    assert is_sorted([1.5, 1.5, 2.0]) == True
    assert is_sorted([1.0, 1.0, 1.0]) == False

@pytest.mark.parametrize("lst,expected", [
    ([1, 2, 3], True),
    ([3, 2, 1], False),
    ([1, 1, 2], True),
    ([1, 1, 1], False),
    ([], True),
    ([42], True),
    ([1, 2, 2, 3, 3], True),
    ([1, 1, 2, 2, 3, 3], True),
    ([0, 0, 1], True),
    ([2, 1, 1], False)
])
def test_parametrized_cases(lst, expected):
    assert is_sorted(lst) == expected
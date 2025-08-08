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

def test_is_sorted_empty_list():
    assert is_sorted([]) == True

def test_is_sorted_single_element():
    assert is_sorted([1]) == True

def test_is_sorted_two_elements_sorted():
    assert is_sorted([1, 2]) == True

def test_is_sorted_two_elements_unsorted():
    assert is_sorted([2, 1]) == False

def test_is_sorted_duplicate_elements_allowed():
    assert is_sorted([1, 1, 2, 2]) == True

def test_is_sorted_more_than_two_duplicates():
    assert is_sorted([1, 1, 1]) == False

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, 4, 5], True),
    ([5, 4, 3, 2, 1], False),
    ([1, 1, 2, 2, 3], True),
    ([1, 2, 2, 2, 3], False),
    ([1, 2, 1], False),
    ([3, 3, 3, 3], False),
    ([1, 2, 2, 3, 3], True),
    ([0, 0, 1, 1], True),
    ([-2, -1, 0, 1, 2], True),
    ([2.5, 3.5, 4.5], True),
    ([1.0, 1.0, 2.0], True),
    ([1.0, 1.0, 1.0], False)
])
def test_is_sorted_parametrized(input_list, expected):
    assert is_sorted(input_list) == expected

def test_is_sorted_mixed_types():
    with pytest.raises(TypeError):
        is_sorted([1, "2", 3])

def test_is_sorted_none_element():
    with pytest.raises(TypeError):
        is_sorted([1, None, 3])

def test_is_sorted_large_numbers():
    assert is_sorted([10**6, 10**7, 10**8]) == True

def test_is_sorted_negative_numbers():
    assert is_sorted([-3, -2, -1]) == True

def test_is_sorted_same_numbers_at_limit():
    assert is_sorted([-1, -1, 0, 0, 1, 1]) == True

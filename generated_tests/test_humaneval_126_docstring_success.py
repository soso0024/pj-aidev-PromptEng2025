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
    ([1, 2, 2, 2], False),
    ([3, 2, 1], False),
    ([1, 2, 3, 3, 2], False),
    ([1, 2, 3, 3, 3], False),
    ([10, 20, 30, 40, 50], True),
    ([50, 40, 30, 20, 10], False),
    ([1, 1, 2, 2, 3, 3], True)
])
def test_is_sorted(input_list, expected):
    assert is_sorted(input_list) == expected

def test_is_sorted_type_error():
    with pytest.raises(TypeError):
        is_sorted(None)
    with pytest.raises(TypeError):
        is_sorted("string")
    with pytest.raises(TypeError):
        is_sorted(123)
        
def test_is_sorted_empty_list():
    assert is_sorted([]) == True

def test_is_sorted_single_element():
    assert is_sorted([1]) == True

def test_is_sorted_two_duplicates():
    assert is_sorted([1, 1]) == True
    assert is_sorted([2, 2]) == True

def test_is_sorted_three_duplicates():
    assert is_sorted([1, 1, 1]) == False
    assert is_sorted([2, 2, 2]) == False

def test_is_sorted_mixed_duplicates():
    assert is_sorted([1, 1, 2, 2, 3]) == True
    assert is_sorted([1, 2, 2, 3, 3]) == True
    assert is_sorted([1, 1, 2, 2, 2]) == False

def is_sorted(lst):
    if lst is None or not isinstance(lst, list):
        raise TypeError("Input must be a list")
    if not lst:
        return True
    count_digit = dict([(i, 0) for i in lst])
    for i in lst:
        count_digit[i] += 1
    if any(count_digit[i] > 2 for i in lst):
        return False
    if all(lst[i-1] <= lst[i] for i in range(1, len(lst))):
        return True
    return False
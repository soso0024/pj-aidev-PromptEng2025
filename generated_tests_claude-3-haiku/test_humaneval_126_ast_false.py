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
    count_digit = {}
    for i in lst:
        if not isinstance(i, int):
            raise TypeError
        count_digit[i] = count_digit.get(i, 0) + 1
        if count_digit[i] > 2:
            return False
    return all(lst[i-1] <= lst[i] for i in range(1, len(lst)))

@pytest.mark.parametrize("lst, expected", [
    ([1, 2, 3, 4, 5], True),
    ([5, 4, 3, 2, 1], False),
    ([1, 1, 2, 2, 3], True),
    ([1, 2, 2, 3, 3], True),
    ([], True),
    ([1], True),
    ([1, 1, 1], False),
    ([1, 2, 2, 3, 4], True),
    ([4, 3, 2, 2, 1], False),
    ([1.0, 2.0, 3.0, 4.0, 5.0], True),
    ([5.0, 4.0, 3.0, 2.0, 1.0], False),
    ([1, 2, 3, 4, 4], True),
    ([1, 1, 2, 3, 4], True),
    ([1, 2, 3, 3, 4], True),
])
def test_is_sorted(lst, expected):
    assert is_sorted(lst) == expected

@pytest.mark.parametrize("lst", [
    [1, 'a', 3],
    [1, 2.0, 3],
    [1, 2, '3'],
])
def test_is_sorted_with_mixed_types(lst):
    with pytest.raises(TypeError):
        is_sorted(lst)
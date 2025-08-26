# Test cases for HumanEval/72
# Generated using Claude API


def will_it_fly(q,w):
    '''
    Write a function that returns True if the object q will fly, and False otherwise.
    The object q will fly if it's balanced (it is a palindromic list) and the sum of its elements is less than or equal the maximum possible weight w.

    Example:
    will_it_fly([1, 2], 5) ➞ False 
    # 1+2 is less than the maximum possible weight, but it's unbalanced.

    will_it_fly([3, 2, 3], 1) ➞ False
    # it's balanced, but 3+2+3 is more than the maximum possible weight.

    will_it_fly([3, 2, 3], 9) ➞ True
    # 3+2+3 is less than the maximum possible weight, and it's balanced.

    will_it_fly([3], 5) ➞ True
    # 3 is less than the maximum possible weight, and it's balanced.
    '''

    if sum(q) > w:
        return False

    i, j = 0, len(q)-1
    while i<j:
        if q[i] != q[j]:
            return False
        i+=1
        j-=1
    return True


# Generated test cases:
import pytest

def will_it_fly(q,w):
    if sum(q) > w:
        return False

    i, j = 0, len(q)-1
    while i<j:
        if q[i] != q[j]:
            return False
        i+=1
        j-=1
    return True

def test_will_it_fly_basic_palindrome():
    assert will_it_fly([1,2,2,1], 4) == True

def test_will_it_fly_not_palindrome():
    assert will_it_fly([1,2,3,4], 10) == False

def test_will_it_fly_weight_limit_exceeded():
    assert will_it_fly([1,2,3], 5) == False

def test_will_it_fly_empty_list():
    assert will_it_fly([], 0) == True

def test_will_it_fly_single_element():
    assert will_it_fly([5], 5) == True

@pytest.mark.parametrize("q,w,expected", [
    ([1,2,2,1], 4, True),
    ([1,2,3,4], 10, False),
    ([3,2,2,3], 10, True),
    ([1,2,1], 4, True),
    ([1,2,3], 5, False),
    ([], 0, True),
    ([5], 5, True),
    ([1,1,1,1], 4, True),
    ([1,2,3,2,1], 10, True),
    ([1,2,3,4,5], 15, False)
])
def test_will_it_fly_parametrized(q, w, expected):
    assert will_it_fly(q, w) == expected
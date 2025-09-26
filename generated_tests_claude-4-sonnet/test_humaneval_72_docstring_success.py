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

@pytest.mark.parametrize("q,w,expected", [
    ([1, 2], 5, False),
    ([3, 2, 3], 1, False),
    ([3, 2, 3], 9, True),
    ([3], 5, True),
    ([], 0, True),
    ([], 10, True),
    ([1], 1, True),
    ([1], 0, False),
    ([1, 1], 2, True),
    ([1, 1], 1, False),
    ([1, 2, 1], 4, True),
    ([1, 2, 1], 3, False),
    ([1, 2, 3], 10, False),
    ([5, 5, 5, 5], 20, True),
    ([5, 5, 5, 5], 19, False),
    ([1, 2, 3, 2, 1], 9, True),
    ([1, 2, 3, 2, 1], 8, False),
    ([1, 2, 3, 4, 1], 15, False),
    ([0], 0, True),
    ([0], 1, True),
    ([0, 0], 0, True),
    ([0, 1, 0], 1, True),
    ([0, 1, 0], 0, False),
    ([-1, -1], -2, True),
    ([-1, -1], -3, False),
    ([-1, 0, -1], -2, True),
    ([-1, 0, -1], -3, False),
    ([10, 20, 30, 20, 10], 90, True),
    ([10, 20, 30, 20, 10], 89, False),
    ([100], 100, True),
    ([100], 99, False)
])
def test_will_it_fly(q, w, expected):
    assert will_it_fly(q, w) == expected

def test_will_it_fly_empty_list():
    assert will_it_fly([], 0) == True
    assert will_it_fly([], 100) == True
    assert will_it_fly([], -1) == False

def test_will_it_fly_single_element():
    assert will_it_fly([5], 5) == True
    assert will_it_fly([5], 4) == False
    assert will_it_fly([0], 0) == True
    assert will_it_fly([-5], -5) == True
    assert will_it_fly([-5], -6) == False

def test_will_it_fly_two_elements():
    assert will_it_fly([1, 1], 2) == True
    assert will_it_fly([1, 1], 1) == False
    assert will_it_fly([1, 2], 10) == False
    assert will_it_fly([0, 0], 0) == True

def test_will_it_fly_odd_length_palindrome():
    assert will_it_fly([1, 2, 1], 4) == True
    assert will_it_fly([1, 2, 1], 3) == False
    assert will_it_fly([5, 3, 5], 13) == True
    assert will_it_fly([5, 3, 5], 12) == False

def test_will_it_fly_even_length_palindrome():
    assert will_it_fly([1, 2, 2, 1], 6) == True
    assert will_it_fly([1, 2, 2, 1], 5) == False
    assert will_it_fly([3, 4, 4, 3], 14) == True
    assert will_it_fly([3, 4, 4, 3], 13) == False

def test_will_it_fly_not_palindrome():
    assert will_it_fly([1, 2, 3], 100) == False
    assert will_it_fly([1, 2, 3, 4], 100) == False
    assert will_it_fly([5, 4, 3, 2, 1], 100) == False

def test_will_it_fly_negative_numbers():
    assert will_it_fly([-1, -1], -2) == True
    assert will_it_fly([-1, -1], -3) == False
    assert will_it_fly([-2, 0, -2], -4) == True
    assert will_it_fly([-2, 0, -2], -5) == False

def test_will_it_fly_zero_weight():
    assert will_it_fly([0], 0) == True
    assert will_it_fly([0, 0], 0) == True
    assert will_it_fly([1], 0) == False
    assert will_it_fly([0, 1, 0], 0) == False
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
    ([1, 2, 3], 6, False),
    ([1, 2, 1], 4, True),
    ([1, 2, 1], 3, False),
    ([5, 1, 8], 9, False),
    ([2, 2], 5, True),
    ([1, 1, 1, 1], 4, True),
    ([1, 1, 1, 1], 3, False),
    ([7, 4, 7], 17, False),
    ([7, 4, 7], 18, True),
    ([1, 2, 2, 1], 6, True),
    ([1, 2, 2, 1], 5, False),
    ([5, 1, 1, 5], 12, True),
    ([5, 1, 1, 5], 11, False),
    ([1, 2, 3, 4, 5], 15, False),
    ([5, 4, 3, 4, 5], 21, True),
    ([5, 4, 3, 4, 5], 20, False),
    ([1, 2, 3, 2, 1], 9, True),
    ([1, 2, 3, 2, 1], 8, False),
    ([0, 0, 0], 1, True),
    ([0, 1, 0], 1, True),
    ([0, 1, 0], 0, False),
    ([10], 10, True),
    ([10], 9, False),
    ([1, 1], 2, True),
    ([1, 1], 1, False),
    ([2, 1, 2], 5, True),
    ([2, 1, 2], 4, False),
    ([100, 100], 200, True),
    ([100, 100], 199, False),
    ([1, 2, 3, 4, 3, 2, 1], 16, True),
    ([1, 2, 3, 4, 3, 2, 1], 15, False),
    ([0], 0, True),
    ([0], -1, False),
    ([-1, -1], -2, True),
    ([-1, -1], -3, False),
    ([1, 0, 1], 2, True),
    ([1, 0, 1], 1, False)
])
def test_will_it_fly_parametrized(q, w, expected):
    assert will_it_fly(q, w) == expected

def test_empty_list():
    assert will_it_fly([], 0) == True
    assert will_it_fly([], 1) == True
    assert will_it_fly([], -1) == False

def test_single_element():
    assert will_it_fly([5], 5) == True
    assert will_it_fly([5], 6) == True
    assert will_it_fly([5], 4) == False

def test_two_elements_palindrome():
    assert will_it_fly([3, 3], 6) == True
    assert will_it_fly([3, 3], 7) == True
    assert will_it_fly([3, 3], 5) == False

def test_two_elements_not_palindrome():
    assert will_it_fly([1, 2], 10) == False
    assert will_it_fly([1, 2], 3) == False
    assert will_it_fly([1, 2], 2) == False

def test_odd_length_palindrome():
    assert will_it_fly([1, 2, 1], 4) == True
    assert will_it_fly([1, 2, 1], 5) == True
    assert will_it_fly([1, 2, 1], 3) == False

def test_even_length_palindrome():
    assert will_it_fly([1, 2, 2, 1], 6) == True
    assert will_it_fly([1, 2, 2, 1], 7) == True
    assert will_it_fly([1, 2, 2, 1], 5) == False

def test_negative_numbers():
    assert will_it_fly([-1, 0, -1], -2) == True
    assert will_it_fly([-1, 0, -1], -1) == True
    assert will_it_fly([-1, 0, -1], -3) == False
    assert will_it_fly([-2, -2], -4) == True
    assert will_it_fly([-2, -2], -5) == False

def test_zero_weight():
    assert will_it_fly([0, 0, 0], 0) == True
    assert will_it_fly([1, 1], 0) == False
    assert will_it_fly([0], 0) == True

def test_large_numbers():
    assert will_it_fly([1000, 1000], 2000) == True
    assert will_it_fly([1000, 1000], 1999) == False
    assert will_it_fly([999, 1, 999], 1999) == True
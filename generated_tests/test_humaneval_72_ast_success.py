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

def test_will_it_fly_basic_symmetrical():
    assert will_it_fly([1, 2, 2, 1], 8) == True
    assert will_it_fly([1, 2, 3, 2, 1], 10) == True

def test_will_it_fly_basic_asymmetrical():
    assert will_it_fly([1, 2, 3, 1], 8) == False
    assert will_it_fly([1, 2, 2, 3], 10) == False

def test_will_it_fly_weight_limit():
    assert will_it_fly([2, 2, 2, 2], 7) == False
    assert will_it_fly([1, 1, 1, 1], 3) == False

def test_will_it_fly_single_element():
    assert will_it_fly([1], 2) == True
    assert will_it_fly([2], 1) == False

def test_will_it_fly_empty_list():
    assert will_it_fly([], 5) == True

@pytest.mark.parametrize("q,w,expected", [
    ([1, 2, 2, 1], 8, True),
    ([1, 2, 3, 1], 8, False),
    ([5, 5, 5, 5], 19, False),
    ([2, 3, 3, 2], 12, True),
    ([], 5, True),
    ([1], 2, True),
    ([10], 5, False),
    ([1, 1], 3, True),
    ([1, 2], 5, False),
    ([1, 2, 3, 2, 1], 10, True),
    ([1, 2, 3, 3, 2, 1], 15, True),
    ([1, 2, 3, 4, 2, 1], 15, False)
])
def test_will_it_fly_parametrized(q, w, expected):
    assert will_it_fly(q, w) == expected

def test_will_it_fly_large_numbers():
    assert will_it_fly([100, 200, 200, 100], 1000) == True
    assert will_it_fly([1000, 1000], 1999) == False

def test_will_it_fly_zero_weight():
    assert will_it_fly([0, 0, 0], 1) == True
    assert will_it_fly([0], 0) == True

def test_will_it_fly_negative_numbers():
    assert will_it_fly([-1, -1], 0) == True
    assert will_it_fly([-2, -1], 0) == False

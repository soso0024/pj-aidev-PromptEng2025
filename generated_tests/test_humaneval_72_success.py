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
    assert will_it_fly([1, 2, 2, 1], 6) == True
    assert will_it_fly([1, 2, 3, 2, 1], 9) == True

def test_will_it_fly_basic_asymmetrical():
    assert will_it_fly([1, 2, 3, 1], 7) == False
    assert will_it_fly([1, 2, 2, 3], 8) == False

def test_will_it_fly_weight_limit():
    assert will_it_fly([1, 1], 1) == False
    assert will_it_fly([2, 2], 4) == True
    assert will_it_fly([2, 2], 3) == False

def test_will_it_fly_single_element():
    assert will_it_fly([1], 2) == True
    assert will_it_fly([5], 4) == False

def test_will_it_fly_empty_list():
    assert will_it_fly([], 5) == True

@pytest.mark.parametrize("q, w, expected", [
    ([1, 2, 2, 1], 6, True),
    ([1, 2, 3, 1], 7, False),
    ([5, 5], 9, False),
    ([2, 3, 3, 2], 10, True),
    ([], 0, True),
    ([1], 1, True),
    ([10, 20, 20, 10], 50, False),
    ([1, 1, 1, 1, 1], 4, False),
    ([2, 4, 6, 4, 2], 18, True),
    ([0, 0, 0, 0], 1, True)
])
def test_will_it_fly_parametrized(q, w, expected):
    assert will_it_fly(q, w) == expected

def test_will_it_fly_zero_weight():
    assert will_it_fly([0, 0], 1) == True
    assert will_it_fly([0], 0) == True

def test_will_it_fly_large_numbers():
    assert will_it_fly([1000, 2000, 2000, 1000], 6000) == True
    assert will_it_fly([1000, 2000, 2000, 1000], 5999) == False

def test_will_it_fly_odd_length():
    assert will_it_fly([1, 2, 1], 4) == True
    assert will_it_fly([1, 2, 3], 6) == False

def test_will_it_fly_even_length():
    assert will_it_fly([1, 1], 2) == True
    assert will_it_fly([1, 2], 3) == False

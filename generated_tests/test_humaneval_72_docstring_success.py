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

def test_empty_list():
    assert will_it_fly([], 5) == True

def test_single_element():
    assert will_it_fly([3], 5) == True

def test_balanced_under_weight():
    assert will_it_fly([3, 2, 3], 9) == True

def test_balanced_equal_weight():
    assert will_it_fly([1, 1, 1], 3) == True

def test_balanced_over_weight():
    assert will_it_fly([3, 2, 3], 7) == False

def test_unbalanced_under_weight():
    assert will_it_fly([1, 2], 5) == False

def test_unbalanced_over_weight():
    assert will_it_fly([1, 2], 2) == False

@pytest.mark.parametrize("q,w,expected", [
    ([1, 2, 2, 1], 10, True),
    ([2, 2], 4, True),
    ([3, 2, 1], 6, False),
    ([1, 2, 3, 2, 1], 10, True),
    ([1, 2, 3, 2, 1], 8, False),
    ([4], 3, False),
    ([], 0, True),
    ([5, 5], 9, False),
    ([1, 2, 3, 3, 2, 1], 12, True),
    ([1, 2, 3, 4, 2, 1], 13, False)
])
def test_multiple_cases(q, w, expected):
    assert will_it_fly(q, w) == expected

@pytest.mark.parametrize("q,w", [
    ([0, 0], 0),
    ([1, 1], 2),
    ([5], 5),
    ([2, 1, 2], 6),
    ([1, 2, 2, 1], 8)
])
def test_edge_weight_cases(q, w):
    assert will_it_fly(q, w) == True

def test_large_numbers():
    assert will_it_fly([1000, 1000], 2001) == True
    assert will_it_fly([1000, 1000], 1999) == False

def test_zero_elements():
    assert will_it_fly([0, 0, 0], 1) == True

def test_negative_numbers():
    assert will_it_fly([-1, -1], 2) == True
    assert will_it_fly([-1, 0, -1], 5) == True
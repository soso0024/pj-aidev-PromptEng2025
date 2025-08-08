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

def test_basic_balanced_under_weight():
    assert will_it_fly([3, 2, 3], 9) == True

def test_basic_balanced_over_weight():
    assert will_it_fly([3, 2, 3], 1) == False

def test_unbalanced_under_weight():
    assert will_it_fly([1, 2], 5) == False

def test_single_element():
    assert will_it_fly([3], 5) == True

def test_empty_list():
    assert will_it_fly([], 5) == True

@pytest.mark.parametrize("input_list,weight,expected", [
    ([1, 2, 2, 1], 10, True),
    ([2, 2], 5, True),
    ([3, 4, 3], 12, True),
    ([1, 2, 3, 2, 1], 10, True),
    ([1, 2, 3, 3, 2, 1], 15, True),
    ([1, 2, 3, 4], 20, False),
    ([1, 2, 1], 2, False),
    ([5, 5, 5, 5], 19, False),
    ([1], 1, True),
    ([], 0, True)
])
def test_multiple_cases(input_list, weight, expected):
    assert will_it_fly(input_list, weight) == expected

@pytest.mark.parametrize("input_list,weight", [
    ([1, 2, 3], -1),
    ([1, 2, 3], 0),
    ([-1, -1], 5),
    ([0, 0], 1)
])
def test_edge_cases(input_list, weight):
    result = will_it_fly(input_list, weight)
    assert isinstance(result, bool)

def test_large_numbers():
    assert will_it_fly([1000, 2000, 2000, 1000], 10000) == True
    assert will_it_fly([1000, 2000, 2000, 1000], 5000) == False

def test_identical_elements():
    assert will_it_fly([5, 5, 5, 5, 5], 30) == True
    assert will_it_fly([5, 5, 5, 5, 5], 20) == False

def test_zero_elements():
    assert will_it_fly([0, 0, 0], 1) == True
    assert will_it_fly([0], 0) == True

def test_single_heavy_element():
    assert will_it_fly([100], 99) == False
    assert will_it_fly([100], 100) == True

def test_palindrome_verification():
    assert will_it_fly([1, 2, 3, 2, 2], 20) == False
    assert will_it_fly([1, 2, 2, 2, 1], 20) == True

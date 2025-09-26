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
from generated_tests_claude_3_haiku.test_humaneval_72_docstring import will_it_fly
import pytest

@pytest.mark.parametrize("q, w, expected", [
    ([1, 2], 5, False),
    ([3, 2, 3], 1, False),
    ([3, 2, 3], 9, True),
    ([3], 5, True),
    ([1, 1], 2, True),
    ([1, 2, 3, 2, 1], 10, True),
    ([1, 2, 3, 4, 5], 10, False),
    ([], 0, True),
    ([1], 0, False),
    ([1, 1, 1, 1, 1, 1], 6, True),
    ([1, 2, 3, 4, 5, 6], 10, False),
    ([1, 2, 3, 4, 5, 6], 21, True),
])
def test_will_it_fly(q, w, expected):
    assert will_it_fly(q, w) == expected
# Test cases for HumanEval/108
# Generated using Claude API


def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """

    def digits_sum(n):
        neg = 1
        if n < 0: n, neg = -1 * n, -1 
        n = [int(i) for i in str(n)]
        n[0] = n[0] * neg
        return sum(n)
    return len(list(filter(lambda x: x > 0, [digits_sum(i) for i in arr])))


# Generated test cases:
from count_nums import count_nums
import pytest

@pytest.mark.parametrize("arr, expected", [
    ([123, -456, 789], 3),
    ([0, 0, 0], 0),
    ([-1, -2, -3], 0),
    ([1, 2, 3], 6),
    ([1, -1, 2, -2, 3, -3], 6),
    ([], 0),
    ([0], 0),
    ([123.45, -67.89, 0.0], 3),
    ([1000000, -1000000, 1000000], 9),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 46),
])
def test_count_nums(arr, expected):
    assert count_nums(arr) == expected

def test_count_nums_with_non_numeric_input():
    with pytest.raises(TypeError):
        count_nums([1, 2, "3", 4])

def test_count_nums_with_none_input():
    with pytest.raises(TypeError):
        count_nums(None)
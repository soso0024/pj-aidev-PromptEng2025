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
import pytest

def test_count_nums_empty_list():
    assert count_nums([]) == 0

def test_count_nums_negative_numbers():
    assert count_nums([-1, 11, -11]) == 1

def test_count_nums_positive_numbers():
    assert count_nums([1, 1, 2]) == 3

def test_count_nums_mixed_numbers():
    assert count_nums([-123, 456, -789, 0]) == 3

def test_count_nums_single_negative_number():
    assert count_nums([-1]) == 0

def test_count_nums_single_positive_number():
    assert count_nums([123]) == 1

def test_count_nums_zero():
    assert count_nums([0]) == 0

@pytest.mark.parametrize("input,expected", [
    ([-1, -2, -3, 4, 5, 6], 3),
    ([0, 0, 0, 0], 0),
    ([-10, -20, -30, 40, 50, 60], 3),
    ([100, -200, 300, -400, 500], 3)
])
def test_count_nums_parametrized(input, expected):
    assert count_nums(input) == expected
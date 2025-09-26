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

def test_empty_array():
    assert count_nums([]) == 0

def test_negative_numbers():
    assert count_nums([-1, 11, -11]) == 1

def test_positive_numbers():
    assert count_nums([1, 1, 2]) == 3

@pytest.mark.parametrize("input_arr,expected", [
    ([0, 0, 0], 0),
    ([1, 2, 3], 3),
    ([-123, 456, -789], 2),
    ([10, -20, 30, -40], 2),
    ([100, -100, 200, -200], 2),
])
def test_various_inputs(input_arr, expected):
    assert count_nums(input_arr) == expected

def test_negative_digit_sum():
    assert count_nums([-123, 456, -789]) == 2

def test_zero_digit_sum():
    assert count_nums([0, 0, 0]) == 0

def test_single_negative_number():
    assert count_nums([-1]) == 0

def test_single_positive_number():
    assert count_nums([1]) == 1

def count_nums(arr):
    def digits_sum(n):
        neg = 1
        if n < 0: n, neg = abs(n), -1 
        n = [int(i) for i in str(n)]
        n[0] = n[0] * neg
        return sum(n)
    return len(list(filter(lambda x: x > 0, [digits_sum(i) for i in arr])))
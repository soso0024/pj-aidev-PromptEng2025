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

def test_single_positive():
    assert count_nums([123]) == 1

def test_single_negative():
    assert count_nums([-123]) == 1

@pytest.mark.parametrize("input_arr,expected", [
    ([1, 2, 3, 4, 5], 5),
    ([-1, -2, -3, -4, -5], 0),
    ([11, -11, 22, -22], 2),
    ([10, 20, 30, -40, 50], 4),
    ([9, -9, 0, 99, -99], 2),
])
def test_mixed_numbers(input_arr, expected):
    assert count_nums(input_arr) == expected

@pytest.mark.parametrize("input_arr,expected", [
    ([111, 222, 333], 3),
    ([-111, -222, -333], 0),
    ([123, -123, 456, -456], 2),
])
def test_three_digit_numbers(input_arr, expected):
    assert count_nums(input_arr) == expected

def test_large_numbers():
    assert count_nums([1000, 2000, 3000]) == 3
    assert count_nums([-1000, -2000, -3000]) == 0

def test_zero():
    assert count_nums([0]) == 0
    assert count_nums([0, 0, 0]) == 0

def test_mixed_digit_lengths():
    assert count_nums([1, 22, 333, 4444]) == 4
    assert count_nums([-1, -22, -333, -4444]) == 0

@pytest.mark.parametrize("input_arr,expected", [
    ([12345, -12345], 2),
    ([9999, -9999, 8888, -8888], 4),
    ([1, -1, 22, -22, 333, -333], 3),
])
def test_symmetric_pairs(input_arr, expected):
    assert count_nums(input_arr) == expected

def test_single_digits():
    assert count_nums([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 9
    assert count_nums([-1, -2, -3, -4, -5, -6, -7, -8, -9]) == 0

def test_repeated_numbers():
    assert count_nums([11, 11, 11]) == 3
    assert count_nums([-11, -11, -11]) == 0
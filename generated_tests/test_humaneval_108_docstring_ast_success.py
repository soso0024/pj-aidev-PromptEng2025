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
    assert count_nums([1]) == 1

def test_single_negative():
    assert count_nums([-1]) == 0

def test_multiple_digits():
    assert count_nums([123, 456, 789]) == 3

def test_negative_numbers():
    assert count_nums([-123, -456, -789]) == 3

def test_mixed_numbers():
    assert count_nums([-1, 11, -11]) == 1

def test_zeros():
    assert count_nums([0, 0, 0]) == 0

@pytest.mark.parametrize("input_arr,expected", [
    ([1, 1, 2], 3),
    ([10, 20, 30], 3),
    ([-1, -2, -3], 0),
    ([11, -11, 121], 2),
    ([999, -999, 0], 2),
    ([-123, 456, -789], 3),
    ([0], 0),
    ([1, -1], 1),
    ([100, 200, 300], 3),
    ([-10, -20, -30], 0)
])
def test_parametrized_cases(input_arr, expected):
    assert count_nums(input_arr) == expected

def test_large_numbers():
    assert count_nums([1000000, 2000000, 3000000]) == 3

def test_mixed_digit_sums():
    assert count_nums([19, -19, 91, -91]) == 3

def test_repeated_numbers():
    assert count_nums([11, 11, 11]) == 3

def test_single_digit_sequence():
    assert count_nums([1, 2, 3, 4, 5]) == 5

def test_negative_single_digit_sequence():
    assert count_nums([-1, -2, -3, -4, -5]) == 0
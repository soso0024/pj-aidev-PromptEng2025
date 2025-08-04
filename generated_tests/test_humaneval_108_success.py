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

def test_count_nums_empty_array():
    assert count_nums([]) == 0

def test_count_nums_single_positive():
    assert count_nums([123]) == 1

def test_count_nums_single_negative():
    assert count_nums([-123]) == 1

@pytest.mark.parametrize("input_arr,expected", [
    ([1, 2, 3, 4, 5], 5),
    ([-1, -2, -3, -4, -5], 0),
    ([11, -11, 22, -22], 2),
    ([10, 20, 30, 40, 50], 5),
    ([9, -9, 0, 23, -24], 3),
    ([100, 200, 300], 3),
    ([-1, -11, -111], 1),
    ([0], 0),
    ([1000, -1000], 1),
    ([12345, -12345, 0, 999], 3)
])
def test_count_nums_parametrized(input_arr, expected):
    assert count_nums(input_arr) == expected

def test_count_nums_all_zeros():
    assert count_nums([0, 0, 0, 0]) == 0

def test_count_nums_mixed_values():
    assert count_nums([11, -11, 0, 123, -123, 1, -1]) == 4

def test_count_nums_large_numbers():
    assert count_nums([999999, -999999, 1000000]) == 3

def test_count_nums_single_digits():
    assert count_nums([1, 2, 3, -1, -2, -3]) == 3

def test_count_nums_repeated_numbers():
    assert count_nums([11, 11, 11, -11, -11]) == 3

@pytest.mark.parametrize("input_arr", [
    None,
    "string",
    123,
    True,
    [None],
    ["string"],
    [True, False]
])
def test_count_nums_invalid_input(input_arr):
    with pytest.raises(Exception):
        count_nums(input_arr)
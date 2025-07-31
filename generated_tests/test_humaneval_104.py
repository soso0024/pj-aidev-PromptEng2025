# Test cases for HumanEval/104
# Generated using Claude API


def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """

    odd_digit_elements = []
    for i in x:
        if all (int(c) % 2 == 1 for c in str(i)):
            odd_digit_elements.append(i)
    return sorted(odd_digit_elements)


# Generated test cases:
import pytest

def test_unique_digits_basic():
    assert unique_digits([15, 33, 1422, 1]) == [1, 15, 33]
    assert unique_digits([152, 323, 1422, 10]) == []

def test_unique_digits_empty_list():
    assert unique_digits([]) == []

def test_unique_digits_single_element():
    assert unique_digits([1]) == [1]
    assert unique_digits([2]) == []

def test_unique_digits_all_odd():
    assert unique_digits([1, 3, 5, 7, 9]) == [1, 3, 5, 7, 9]

def test_unique_digits_all_even():
    assert unique_digits([2, 4, 6, 8]) == []

def test_unique_digits_mixed_numbers():
    assert unique_digits([11, 22, 33, 44, 55]) == [11, 33, 55]

def test_unique_digits_large_numbers():
    assert unique_digits([1111, 3333, 5555, 7777, 9999]) == [1111, 3333, 5555, 7777, 9999]
    assert unique_digits([2222, 4444, 6666, 8888]) == []

def test_unique_digits_mixed_digits():
    assert unique_digits([123, 456, 789, 135, 357]) == [135, 357]

def test_unique_digits_repeated_numbers():
    assert unique_digits([11, 11, 33, 33, 55, 55]) == [11, 33, 55]

def test_unique_digits_single_even_digit():
    assert unique_digits([12, 14, 16, 18]) == []

def test_unique_digits_zero():
    assert unique_digits([0]) == []

def test_unique_digits_large_list():
    input_list = list(range(1, 100))
    expected = sorted([x for x in input_list if all(int(c) % 2 == 1 for c in str(x))])
    assert unique_digits(input_list) == expected

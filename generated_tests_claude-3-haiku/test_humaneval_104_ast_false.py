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

def test_unique_digits_empty_list():
    assert unique_digits([]) == []

def test_unique_digits_all_even_digits():
    assert unique_digits([12, 24, 36]) == []

def test_unique_digits_mixed_digits():
    assert unique_digits([13, 25, 37, 49, 51]) == [13, 25, 37, 51]

def test_unique_digits_single_odd_digit():
    assert unique_digits([1]) == [1]

def test_unique_digits_negative_numbers():
    assert unique_digits([-13, -25, -37, -49, -51]) == [-13, -25, -37, -51]

def test_unique_digits_duplicate_odd_digits():
    assert unique_digits([13, 31, 51, 15]) == [13, 15, 31, 51]

def test_unique_digits_non_integer_input():
    with pytest.raises(ValueError):
        unique_digits(['a', 'b', 'c'])

def unique_digits(x):
    odd_digit_elements = []
    for i in x:
        if all(int(d) % 2 == 1 for d in str(abs(int(i)))):
            odd_digit_elements.append(i)
    return sorted(odd_digit_elements)
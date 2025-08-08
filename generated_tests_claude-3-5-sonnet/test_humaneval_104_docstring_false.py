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

def test_unique_digits_empty():
    assert unique_digits([]) == []

def test_unique_digits_single():
    assert unique_digits([1]) == [1]
    assert unique_digits([2]) == []

def test_unique_digits_all_odd():
    assert unique_digits([1, 3, 5, 7, 9]) == [1, 3, 5, 7, 9]

def test_unique_digits_all_even():
    assert unique_digits([2, 4, 6, 8]) == []

@pytest.mark.parametrize("input_list,expected", [
    ([11, 33, 55, 77, 99], [11, 33, 55, 77, 99]),
    ([22, 44, 66, 88], []),
    ([15, 21, 42, 35, 71], [15, 35, 71]),
    ([1, 11, 111, 1111], [1, 11, 111, 1111]),
    ([10, 20, 30, 40], []),
    ([123, 456, 789, 135], [135]),
    ([1, 2, 3, 4, 5], [1, 3, 5])
])
def test_unique_digits_parametrized(input_list, expected):
    assert unique_digits(input_list) == expected

def test_unique_digits_large_numbers():
    assert unique_digits([11111, 33333, 55555]) == [11111, 33333, 55555]
    assert unique_digits([12345, 67890]) == []

def test_unique_digits_mixed_length():
    assert unique_digits([1, 11, 111, 1111, 2, 22, 222]) == [1, 11, 111, 1111]

def test_unique_digits_duplicates():
    result = unique_digits([11, 11, 33, 33, 55, 55])
    assert len(set(result)) == len(result)  # Check for uniqueness
    assert sorted(set(result)) == [11, 33, 55]

@pytest.mark.parametrize("invalid_input", [
    [-1],
    [-15, -33],
    [1.5, 3.3],
    [None],
    [True, False]
])
def test_unique_digits_invalid_input(invalid_input):
    with pytest.raises((ValueError, TypeError)):
        unique_digits(invalid_input)

def test_unique_digits_zero():
    assert unique_digits([0]) == []

def test_unique_digits_string_input():
    with pytest.raises((ValueError, TypeError)):
        unique_digits(["1", "33"])
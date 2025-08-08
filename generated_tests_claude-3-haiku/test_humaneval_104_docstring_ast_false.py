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

def test_unique_digits_all_odd_digits():
    assert unique_digits([15, 33, 135, 79]) == [15, 33, 79, 135]

def test_unique_digits_some_even_digits():
    assert unique_digits([15, 33, 1422, 1]) == [1, 15, 33]

def test_unique_digits_all_even_digits():
    assert unique_digits([152, 322, 1422, 10]) == []

@pytest.mark.parametrize("input,expected", [
    ([15, 33, 1422, 1], [1, 15, 33]),
    ([152, 323, 1422, 10], []),
    ([1, 3, 5, 7, 9], [1, 3, 5, 7, 9]),
    ([2, 4, 6, 8, 10], []),
    ([15, 33, 51, 75, 93], [15, 33, 51, 75, 93])
])
def test_unique_digits_parametrized(input, expected):
    assert unique_digits(input) == expected

def test_unique_digits_single_element():
    assert unique_digits([15]) == [15]

def test_unique_digits_duplicate_elements():
    assert unique_digits([15, 15, 33, 33]) == [15, 33]

def unique_digits(x):
    odd_digit_elements = []
    for i in x:
        if all(int(d) % 2 == 1 for d in str(i)):
            odd_digit_elements.append(i)
    return sorted(odd_digit_elements)
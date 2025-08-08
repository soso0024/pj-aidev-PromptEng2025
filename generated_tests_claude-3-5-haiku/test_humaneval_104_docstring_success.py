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

def test_unique_digits_normal_cases():
    assert unique_digits([15, 33, 1422, 1]) == [1, 15, 33]
    assert unique_digits([152, 323, 1422, 10]) == []

def test_unique_digits_empty_list():
    assert unique_digits([]) == []

def test_unique_digits_single_digit_numbers():
    assert unique_digits([1, 3, 5, 7, 9]) == [1, 3, 5, 7, 9]
    assert unique_digits([2, 4, 6, 8]) == []

def test_unique_digits_mixed_numbers():
    assert unique_digits([11, 13, 15, 22, 33, 55]) == [11, 13, 15, 33, 55]

@pytest.mark.parametrize("input_list,expected", [
    ([15, 33, 1422, 1], [1, 15, 33]),
    ([152, 323, 1422, 10], []),
    ([], []),
    ([1, 3, 5, 7, 9], [1, 3, 5, 7, 9]),
    ([11, 13, 15, 22, 33, 55], [11, 13, 15, 33, 55])
])
def test_unique_digits_parametrized(input_list, expected):
    assert unique_digits(input_list) == expected

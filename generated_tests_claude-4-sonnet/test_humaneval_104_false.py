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

def test_empty_list():
    assert unique_digits([]) == []

def test_single_odd_digit_number():
    assert unique_digits([1]) == [1]
    assert unique_digits([3]) == [3]
    assert unique_digits([5]) == [5]
    assert unique_digits([7]) == [7]
    assert unique_digits([9]) == [9]

def test_single_even_digit_number():
    assert unique_digits([0]) == []
    assert unique_digits([2]) == []
    assert unique_digits([4]) == []
    assert unique_digits([6]) == []
    assert unique_digits([8]) == []

def test_multiple_odd_digit_numbers():
    assert unique_digits([1, 3, 5]) == [1, 3, 5]
    assert unique_digits([13, 57, 91]) == [13, 57, 91]
    assert unique_digits([135, 579, 913]) == [135, 579, 913]

def test_multiple_even_digit_numbers():
    assert unique_digits([2, 4, 6, 8]) == []
    assert unique_digits([24, 68, 2]) == []

def test_mixed_numbers():
    assert unique_digits([1, 2, 3, 4, 5]) == [1, 3, 5]
    assert unique_digits([12, 13, 24, 35]) == [13, 35]

def test_numbers_with_mixed_digits():
    assert unique_digits([12, 23, 34]) == []
    assert unique_digits([135, 246, 579]) == [135, 579]
    assert unique_digits([1357, 2468, 1379]) == [1357, 1379]

def test_negative_numbers():
    assert unique_digits([-1, -3, -5]) == []
    assert unique_digits([-2, -4, -6]) == []
    assert unique_digits([-13, -24, -35]) == []

def test_zero():
    assert unique_digits([0]) == []
    assert unique_digits([10, 20, 30]) == []

def test_large_numbers():
    assert unique_digits([1357913579]) == [1357913579]
    assert unique_digits([2468024680]) == []
    assert unique_digits([1357913579, 2468024680]) == [1357913579]

def test_unsorted_input():
    assert unique_digits([5, 1, 9, 3, 7]) == [1, 3, 5, 7, 9]
    assert unique_digits([97, 13, 531, 75]) == [13, 75, 97, 531]

def test_duplicates():
    assert unique_digits([1, 1, 3, 3, 5]) == [1, 1, 3, 3, 5]
    assert unique_digits([13, 31, 13]) == [13, 13, 31]

@pytest.mark.parametrize("input_list,expected", [
    ([15, 33, 1422, 1], [1, 15, 33]),
    ([152, 323, 1422, 10], []),
    ([12, 34, 56, 78], []),
    ([11, 22, 33, 44], [11, 33]),
    ([1, 11, 111, 1111], [1, 11, 111, 1111])
])
def test_parametrized_cases(input_list, expected):
    assert unique_digits(input_list) == expected

def test_single_digit_edge_cases():
    assert unique_digits([1, 3, 5, 7, 9, 0, 2, 4, 6, 8]) == [1, 3, 5, 7, 9]

def test_numbers_starting_with_zero():
    assert unique_digits([1, 3, 5]) == [1, 3, 5]

def test_very_large_list():
    large_list = list(range(1, 100))
    result = unique_digits(large_list)
    expected = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 31, 33, 35, 37, 39, 51, 53, 55, 57, 59, 71, 73, 75, 77, 79, 91, 93, 95, 97, 99]
    assert result == expected

def unique_digits(x):
    odd_digit_elements = []
    for i in x:
        if all (int(c) % 2 == 1 for c in str(i)):
            odd_digit_elements.append(i)
    return sorted(odd_digit_elements)
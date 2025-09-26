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

def unique_digits(x):
    odd_digit_elements = []
    for i in x:
        if all (int(c) % 2 == 1 for c in str(i)):
            odd_digit_elements.append(i)
    return sorted(odd_digit_elements)

def test_unique_digits_example_1():
    assert unique_digits([15, 33, 1422, 1]) == [1, 15, 33]

def test_unique_digits_example_2():
    assert unique_digits([152, 323, 1422, 10]) == []

def test_unique_digits_empty_list():
    assert unique_digits([]) == []

def test_unique_digits_single_odd_digit():
    assert unique_digits([1]) == [1]
    assert unique_digits([3]) == [3]
    assert unique_digits([5]) == [5]
    assert unique_digits([7]) == [7]
    assert unique_digits([9]) == [9]

def test_unique_digits_single_even_digit():
    assert unique_digits([2]) == []
    assert unique_digits([4]) == []
    assert unique_digits([6]) == []
    assert unique_digits([8]) == []
    assert unique_digits([0]) == []

def test_unique_digits_all_odd_digits():
    assert unique_digits([13, 57, 91, 35]) == [13, 35, 57, 91]

def test_unique_digits_all_even_digits():
    assert unique_digits([24, 68, 80, 42]) == []

def test_unique_digits_mixed_numbers():
    assert unique_digits([123, 246, 135, 579, 468]) == [135, 579]

def test_unique_digits_large_numbers():
    assert unique_digits([1357913579, 2468024680, 1111, 3333]) == [1111, 3333, 1357913579]

def test_unique_digits_duplicates():
    assert unique_digits([13, 13, 24, 24, 57, 57]) == [13, 13, 57, 57]

def test_unique_digits_unsorted_input():
    assert unique_digits([99, 11, 77, 33, 55]) == [11, 33, 55, 77, 99]

def test_unique_digits_numbers_with_zero():
    assert unique_digits([101, 303, 505, 707]) == []

def test_unique_digits_single_element_lists():
    assert unique_digits([13579]) == [13579]
    assert unique_digits([24680]) == []

@pytest.mark.parametrize("input_list,expected", [
    ([1, 3, 5, 7, 9], [1, 3, 5, 7, 9]),
    ([2, 4, 6, 8], []),
    ([11, 22, 33, 44], [11, 33]),
    ([135, 246, 579], [135, 579]),
    ([10, 20, 30], []),
    ([111, 222, 333], [111, 333])
])
def test_unique_digits_parametrized(input_list, expected):
    assert unique_digits(input_list) == expected

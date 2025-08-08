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

def test_basic_functionality():
    assert unique_digits([15, 33, 1422, 1]) == [1, 15, 33]
    assert unique_digits([152, 323, 1422, 10]) == []

@pytest.mark.parametrize("input_list,expected", [
    ([1, 3, 5, 7], [1, 3, 5, 7]),
    ([2, 4, 6, 8], []),
    ([11, 33, 55, 77, 99], [11, 33, 55, 77, 99]),
    ([10, 20, 30, 40], []),
    ([], []),
])
def test_various_inputs(input_list, expected):
    assert unique_digits(input_list) == expected

@pytest.mark.parametrize("input_list,expected", [
    ([123, 456, 789], []),
    ([135, 357, 579], [135, 357, 579]),
    ([111, 333, 555], [111, 333, 555]),
    ([222, 444, 666], []),
])
def test_three_digit_numbers(input_list, expected):
    assert unique_digits(input_list) == expected

def test_sorting():
    assert unique_digits([55, 1, 3, 33, 7, 9]) == [1, 3, 7, 9, 33, 55]
    assert unique_digits([999, 111, 333]) == [111, 333, 999]

def test_single_element():
    assert unique_digits([1]) == [1]
    assert unique_digits([2]) == []
    assert unique_digits([11]) == [11]
    assert unique_digits([22]) == []

def test_duplicate_numbers():
    result = unique_digits([11, 11, 11])
    assert result == [11]  # Function should return only unique values
    result = unique_digits([33, 33, 55, 55])
    assert result == [33, 55]  # Function should return only unique values

def test_large_numbers():
    assert unique_digits([11111, 33333, 55555]) == [11111, 33333, 55555]
    assert unique_digits([12345, 67890]) == []

@pytest.mark.parametrize("input_list", [
    [-1],
    [-15, 33],
])
def test_invalid_inputs(input_list):
    with pytest.raises(ValueError):
        unique_digits(input_list)

def test_mixed_valid_invalid():
    with pytest.raises(TypeError):
        unique_digits([15, "33", 1422, 1])

def test_non_list_input():
    with pytest.raises(AttributeError):
        unique_digits("123")
    with pytest.raises(AttributeError):
        unique_digits(123)
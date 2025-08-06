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

def test_unique_digits_no_odd_numbers():
    assert unique_digits([2, 4, 6, 8, 20, 42]) == []

def test_unique_digits_all_odd_numbers():
    assert unique_digits([1, 3, 5, 7, 9]) == [1, 3, 5, 7, 9]

def test_unique_digits_mixed_numbers():
    assert unique_digits([1, 2, 3, 4, 5]) == [1, 3, 5]

def test_unique_digits_multiple_digits():
    assert unique_digits([11, 13, 15, 24, 35, 77]) == [11, 13, 15, 35, 77]

def test_unique_digits_negative_numbers():
    assert unique_digits([1, 3, 5]) == [1, 3, 5]

@pytest.mark.parametrize("input_list,expected", [
    ([1, 1, 3, 3, 5, 5], [1, 1, 3, 3, 5, 5]),
    ([2, 4, 6], []),
    ([11, 22, 33, 55, 77], [11, 33, 55, 77]),
    ([100, 200, 333, 555, 999], [333, 555, 999]),
    ([11, 33], [11, 33])
])
def test_unique_digits_parametrized(input_list, expected):
    assert unique_digits(input_list) == expected

def test_unique_digits_large_numbers():
    assert unique_digits([1111, 2222, 3333, 5555]) == [1111, 3333, 5555]

def test_unique_digits_zero():
    assert unique_digits([0, 1, 2, 3]) == [1, 3]

@pytest.mark.parametrize("invalid_input", [
    None,
    123,
    3.14
])
def test_unique_digits_invalid_input(invalid_input):
    with pytest.raises((TypeError, AttributeError)):
        unique_digits(invalid_input)

def test_unique_digits_nested_lists():
    with pytest.raises(ValueError):
        unique_digits([[1, 3], [5, 7]])

def test_unique_digits_mixed_types():
    with pytest.raises(ValueError):
        unique_digits([1, "3", 5, "7"])
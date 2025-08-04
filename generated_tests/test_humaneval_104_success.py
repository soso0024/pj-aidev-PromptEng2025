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
    assert unique_digits([2, 4, 6, 8]) == []

def test_unique_digits_all_odd_numbers():
    assert unique_digits([1, 3, 5, 7, 9]) == [1, 3, 5, 7, 9]

def test_unique_digits_mixed_numbers():
    assert unique_digits([1, 2, 3, 4, 5]) == [1, 3, 5]

def test_unique_digits_multi_digit_numbers():
    assert unique_digits([11, 13, 15, 20, 31, 35]) == [11, 13, 15, 31, 35]

def test_unique_digits_positive_numbers():
    assert unique_digits([1, 3, 5]) == [1, 3, 5]

@pytest.mark.parametrize("input_list,expected", [
    ([111, 333, 555], [111, 333, 555]),
    ([123, 456, 789], []),
    ([135, 246, 357], [135, 357]),
    ([0, 1, 2, 3], [1, 3]),
    ([999, 888, 777], [777, 999])
])
def test_unique_digits_parametrized(input_list, expected):
    assert unique_digits(input_list) == expected

def test_unique_digits_large_numbers():
    assert unique_digits([11111, 22222, 33333]) == [11111, 33333]

def test_unique_digits_zero():
    assert unique_digits([0]) == []

def test_unique_digits_single_digit():
    assert unique_digits([1]) == [1]

def test_unique_digits_duplicates():
    result = unique_digits([1, 1, 3, 3, 5, 5])
    assert len(set(result)) == len(set([1, 3, 5]))
    assert sorted(set(result)) == [1, 3, 5]

@pytest.mark.parametrize("invalid_input", [
    None,
    123,
    3.14
])
def test_unique_digits_invalid_input(invalid_input):
    with pytest.raises((TypeError, AttributeError)):
        unique_digits(invalid_input)

def test_unique_digits_invalid_types():
    with pytest.raises((TypeError, ValueError)):
        unique_digits([1, "3", 5.0])

def test_unique_digits_nested_lists():
    with pytest.raises((TypeError, ValueError)):
        unique_digits([[1, 3], [5, 7]])

def test_unique_digits_string_input():
    with pytest.raises((TypeError, ValueError)):
        unique_digits("string")
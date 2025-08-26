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

def test_unique_digits_normal_case():
    assert unique_digits([1, 3, 5, 7, 9, 11, 13, 15]) == [1, 3, 5, 7, 9, 11, 13, 15]

def test_unique_digits_mixed_numbers():
    assert unique_digits([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 3, 5, 7, 9]

def test_unique_digits_empty_list():
    assert unique_digits([]) == []

def test_unique_digits_no_odd_digit_numbers():
    assert unique_digits([2, 4, 6, 8, 10, 12, 14]) == []

@pytest.mark.parametrize("input_list,expected", [
    ([111, 333, 555], [111, 333, 555]),
    ([123, 456, 789], []),
    ([11, 33, 55, 22, 44, 66], [11, 33, 55])
])
def test_unique_digits_parametrized(input_list, expected):
    assert unique_digits(input_list) == expected

def test_unique_digits_large_numbers():
    assert unique_digits([11111, 33333, 55555, 22222, 44444]) == [11111, 33333, 55555]

def test_unique_digits_sorting():
    assert unique_digits([9, 7, 5, 3, 1]) == [1, 3, 5, 7, 9]

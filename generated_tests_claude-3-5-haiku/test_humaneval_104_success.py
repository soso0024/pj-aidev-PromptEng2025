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
    assert unique_digits([1, 3, 5, 7, 9]) == [1, 3, 5, 7, 9]
    assert unique_digits([11, 33, 55, 77, 99]) == [11, 33, 55, 77, 99]

def test_unique_digits_mixed_numbers():
    assert unique_digits([10, 11, 12, 13, 14, 15]) == [11, 13, 15]
    assert unique_digits([20, 22, 31, 33, 45, 55]) == [31, 33, 55]

def test_unique_digits_empty_list():
    assert unique_digits([]) == []

def test_unique_digits_no_odd_digit_numbers():
    assert unique_digits([20, 40, 60, 80]) == []

@pytest.mark.parametrize("input_list,expected", [
    ([1, 3, 5, 7, 9], [1, 3, 5, 7, 9]),
    ([11, 33, 55, 77, 99], [11, 33, 55, 77, 99]),
    ([10, 11, 12, 13, 14, 15], [11, 13, 15]),
    ([], []),
    ([20, 40, 60, 80], [])
])
def test_unique_digits_parametrized(input_list, expected):
    assert unique_digits(input_list) == expected

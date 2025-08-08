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
    assert unique_digits([11, 33, 55, 22, 44]) == [11, 33, 55]

def test_unique_digits_empty_list():
    assert unique_digits([]) == []

def test_unique_digits_no_odd_digit_elements():
    assert unique_digits([22, 44, 66, 88]) == []

def test_unique_digits_mixed_elements():
    assert unique_digits([11, 22, 33, 44, 55, 66, 77, 88, 99]) == [11, 33, 55, 77, 99]

def test_unique_digits_single_element():
    assert unique_digits([11]) == [11]
    assert unique_digits([22]) == []

def test_unique_digits_large_numbers():
    assert unique_digits([1111, 3333, 5555, 2222, 4444]) == [1111, 3333, 5555]

@pytest.mark.parametrize("input_list,expected", [
    ([11, 33, 55, 22, 44], [11, 33, 55]),
    ([], []),
    ([22, 44, 66, 88], []),
    ([11, 22, 33, 44, 55, 66, 77, 88, 99], [11, 33, 55, 77, 99]),
    ([11], [11]),
    ([22], []),
    ([1111, 3333, 5555, 2222, 4444], [1111, 3333, 5555])
])
def test_unique_digits_parametrized(input_list, expected):
    assert unique_digits(input_list) == expected

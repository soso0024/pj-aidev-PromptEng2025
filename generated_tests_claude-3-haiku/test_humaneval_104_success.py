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

def test_unique_digits_all_even_digits():
    assert unique_digits([12, 24, 36]) == []

def test_unique_digits_all_odd_digits():
    assert unique_digits([13, 57, 91]) == [13, 57, 91]

def test_unique_digits_mixed_digits():
    assert unique_digits([13, 24, 57, 68, 91]) == [13, 57, 91]

def test_unique_digits_single_element():
    assert unique_digits([13]) == [13]

@pytest.mark.parametrize("input,expected", [
    ([13, 24, 57, 68, 91], [13, 57, 91]),
    ([13, 57, 91], [13, 57, 91]),
    ([], []),
    ([12, 24, 36], [])
])
def test_unique_digits_parametrized(input, expected):
    assert unique_digits(input) == expected

def test_unique_digits_with_non_integer_elements():
    with pytest.raises(ValueError):
        unique_digits([13, 'a', 57, 91])

def unique_digits(x):
    odd_digit_elements = []
    for i in x:
        if all(int(c) % 2 == 1 for c in str(i)):
            odd_digit_elements.append(i)
    return sorted(odd_digit_elements)

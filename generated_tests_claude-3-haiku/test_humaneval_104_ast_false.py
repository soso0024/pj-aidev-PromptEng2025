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

def test_unique_digits_all_odd():
    assert unique_digits([13, 57, 79]) == [13, 57, 79]

def test_unique_digits_mixed():
    assert unique_digits([13, 24, 57, 79, 86]) == [13, 57, 79]

def test_unique_digits_single_element():
    assert unique_digits([13]) == [13]

def test_unique_digits_string_input():
    with pytest.raises(TypeError):
        unique_digits('123')

@pytest.mark.parametrize("input,expected", [
    ([13, 24, 57, 79, 86], [13, 57, 79]),
    ([11, 33, 55, 77, 99], [11, 33, 55, 77, 99]),
    ([2, 4, 6, 8, 10], []),
    ([1], [1]),
    ([], [])
])
def test_unique_digits_parametrized(input, expected):
    assert unique_digits(input) == expected

def unique_digits(x):
    odd_digit_elements = []
    for i in x:
        if all(int(d) % 2 == 1 for d in str(i)):
            odd_digit_elements.append(i)
    return sorted(odd_digit_elements)
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
from your_module import unique_digits
import pytest

@pytest.mark.parametrize("input_list,expected", [
    ([15, 33, 1422, 1], [1, 15, 33]),
    ([152, 323, 1422, 10], []),
    ([1, 3, 5, 7, 9], [1, 3, 5, 7, 9]),
    ([11, 13, 15, 17, 19], [11, 13, 15, 17, 19]),
    ([], []),
    ([0], []),
    ([-1, -3, -5, -7, -9], []),
    ([1.5, 3.7, 5.1, 7.9], []),
    ([15.0, 33.0, 1422.0, 1.0], [1.0, 15.0, 33.0]),
    ([15, 33, 1422, 1, 11, 13, 15, 17, 19], [1, 11, 13, 15, 15, 17, 19, 33])
])
def test_unique_digits(input_list, expected):
    assert unique_digits(input_list) == expected

@pytest.mark.parametrize("input_list", [
    None,
    "test",
    [1, 2, 3, 4],
    [1.5, 2.3, 3.7, 4.9]
])
def test_unique_digits_invalid_input(input_list):
    with pytest.raises(TypeError):
        unique_digits(input_list)
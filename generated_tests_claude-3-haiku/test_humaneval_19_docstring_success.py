# Test cases for HumanEval/19
# Generated using Claude API

from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    value_map = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    return ' '.join(sorted([x for x in numbers.split(' ') if x], key=lambda x: value_map[x]))


# Generated test cases:
import pytest

def test_sort_numbers_empty_input():
    assert sort_numbers('') == ''

def test_sort_numbers_single_number():
    assert sort_numbers('three') == 'three'

def test_sort_numbers_multiple_numbers():
    assert sort_numbers('three one five') == 'one three five'

@pytest.mark.parametrize("input,expected", [
    ('three one five', 'one three five'),
    ('eight two six', 'two six eight'),
    ('nine four seven', 'four seven nine'),
    ('zero five one', 'zero one five')
])
def test_sort_numbers_parametrized(input, expected):
    assert sort_numbers(input) == expected

def test_sort_numbers_invalid_input():
    with pytest.raises(KeyError):
        sort_numbers('three one invalid')

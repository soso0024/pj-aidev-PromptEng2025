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
from sort_numbers import sort_numbers
import pytest

def test_sort_numbers_empty_input():
    assert sort_numbers('') == ''

def test_sort_numbers_single_number():
    assert sort_numbers('one') == 'one'

@pytest.mark.parametrize("input_str, expected", [
    ('one two three', 'one two three'),
    ('five eight two', 'two five eight'),
    ('nine four seven', 'four seven nine'),
    ('zero six one', 'zero one six')
])
def test_sort_numbers_multiple_numbers(input_str, expected):
    assert sort_numbers(input_str) == expected

def test_sort_numbers_invalid_input():
    with pytest.raises(KeyError):
        sort_numbers('invalid one two')
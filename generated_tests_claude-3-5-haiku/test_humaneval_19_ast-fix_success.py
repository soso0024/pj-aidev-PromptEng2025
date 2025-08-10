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

def test_sort_numbers_basic_case():
    assert sort_numbers('nine five two') == 'two five nine'

def test_sort_numbers_already_sorted():
    assert sort_numbers('zero one two') == 'zero one two'

def test_sort_numbers_reverse_order():
    assert sort_numbers('nine eight seven') == 'seven eight nine'

def test_sort_numbers_mixed_order():
    assert sort_numbers('five three one') == 'one three five'

def test_sort_numbers_single_number():
    assert sort_numbers('seven') == 'seven'

def test_sort_numbers_empty_string():
    assert sort_numbers('') == ''

def test_sort_numbers_multiple_spaces():
    assert sort_numbers('nine  five   two') == 'two five nine'

@pytest.mark.parametrize("input_str,expected", [
    ('nine five two', 'two five nine'),
    ('zero one two', 'zero one two'),
    ('nine eight seven', 'seven eight nine'),
    ('five three one', 'one three five'),
    ('seven', 'seven'),
    ('', ''),
    ('nine  five   two', 'two five nine')
])
def test_sort_numbers_parametrized(input_str, expected):
    assert sort_numbers(input_str) == expected

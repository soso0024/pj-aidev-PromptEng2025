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
from typing import List


def test_sort_numbers_basic():
    assert sort_numbers('three one five') == 'one three five'
    assert sort_numbers('nine five two') == 'two five nine'


def test_sort_numbers_single_number():
    assert sort_numbers('one') == 'one'


def test_sort_numbers_empty():
    assert sort_numbers('') == ''


def test_sort_numbers_with_spaces():
    assert sort_numbers('  three  one  five  ') == 'one three five'


@pytest.mark.parametrize("input_str,expected", [
    ("zero one two", "zero one two"),
    ("nine eight seven", "seven eight nine"),
    ("one one one", "one one one"),
    ("nine zero", "zero nine"),
    ("eight five two one zero", "zero one two five eight")
])
def test_sort_numbers_parametrized(input_str, expected):
    assert sort_numbers(input_str) == expected


def test_sort_numbers_all_numbers():
    input_str = "nine eight seven six five four three two one zero"
    expected = "zero one two three four five six seven eight nine"
    assert sort_numbers(input_str) == expected


@pytest.mark.xfail(raises=KeyError)
def test_sort_numbers_invalid_input():
    sort_numbers('three one ten')


@pytest.mark.xfail(raises=KeyError)
def test_sort_numbers_invalid_words():
    sort_numbers('three hello five')


def test_sort_numbers_multiple_spaces():
    assert sort_numbers('three   one     five') == 'one three five'


def test_sort_numbers_leading_trailing_spaces():
    assert sort_numbers('   three one five   ') == 'one three five'

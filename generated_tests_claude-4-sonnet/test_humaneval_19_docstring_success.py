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

def sort_numbers(numbers: str) -> str:
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

def test_sort_numbers_basic():
    assert sort_numbers('three one five') == 'one three five'

def test_sort_numbers_single():
    assert sort_numbers('seven') == 'seven'

def test_sort_numbers_already_sorted():
    assert sort_numbers('one two three') == 'one two three'

def test_sort_numbers_reverse_order():
    assert sort_numbers('nine eight seven') == 'seven eight nine'

def test_sort_numbers_all_digits():
    assert sort_numbers('nine eight seven six five four three two one zero') == 'zero one two three four five six seven eight nine'

def test_sort_numbers_duplicates():
    assert sort_numbers('three one three five one') == 'one one three three five'

def test_sort_numbers_empty_string():
    assert sort_numbers('') == ''

def test_sort_numbers_single_space():
    assert sort_numbers(' ') == ''

def test_sort_numbers_multiple_spaces():
    assert sort_numbers('three  one   five') == 'one three five'

def test_sort_numbers_leading_trailing_spaces():
    assert sort_numbers(' three one five ') == 'one three five'

def test_sort_numbers_zero_included():
    assert sort_numbers('zero five two') == 'zero two five'

def test_sort_numbers_nine_included():
    assert sort_numbers('nine one four') == 'one four nine'

@pytest.mark.parametrize("input_str,expected", [
    ("zero", "zero"),
    ("one", "one"),
    ("two", "two"),
    ("three", "three"),
    ("four", "four"),
    ("five", "five"),
    ("six", "six"),
    ("seven", "seven"),
    ("eight", "eight"),
    ("nine", "nine")
])
def test_sort_numbers_individual_digits(input_str, expected):
    assert sort_numbers(input_str) == expected

@pytest.mark.parametrize("input_str,expected", [
    ("two one", "one two"),
    ("five three", "three five"),
    ("eight zero", "zero eight"),
    ("nine four", "four nine")
])
def test_sort_numbers_pairs(input_str, expected):
    assert sort_numbers(input_str) == expected

def test_sort_numbers_invalid_word():
    with pytest.raises(KeyError):
        sort_numbers('ten')

def test_sort_numbers_mixed_valid_invalid():
    with pytest.raises(KeyError):
        sort_numbers('one two eleven')

def test_sort_numbers_random_order():
    assert sort_numbers('six two nine one') == 'one two six nine'

def test_sort_numbers_complex_case():
    assert sort_numbers('eight three zero nine one four seven two six five') == 'zero one two three four five six seven eight nine'

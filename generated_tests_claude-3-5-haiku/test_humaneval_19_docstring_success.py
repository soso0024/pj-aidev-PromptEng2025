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

def test_sort_numbers_all_numbers():
    assert sort_numbers('zero one two three four five six seven eight nine') == 'zero one two three four five six seven eight nine'

def test_sort_numbers_reverse_order():
    assert sort_numbers('nine eight seven six five four three two one zero') == 'zero one two three four five six seven eight nine'

def test_sort_numbers_mixed_order():
    assert sort_numbers('five two eight one six') == 'one two five six eight'

def test_sort_numbers_duplicate_numbers():
    assert sort_numbers('three three one five one') == 'one one three three five'

def test_sort_numbers_empty_string():
    assert sort_numbers('') == ''

def test_sort_numbers_single_number():
    assert sort_numbers('seven') == 'seven'

@pytest.mark.parametrize("input_str,expected", [
    ('three one five', 'one three five'),
    ('nine eight seven', 'seven eight nine'),
    ('zero', 'zero'),
    ('', ''),
    ('two two one', 'one two two')
])
def test_sort_numbers_parametrized(input_str, expected):
    assert sort_numbers(input_str) == expected

def test_sort_numbers_case_sensitivity():
    with pytest.raises(KeyError):
        sort_numbers('Three One Five')

def test_sort_numbers_invalid_word():
    with pytest.raises(KeyError):
        sort_numbers('three one ten')

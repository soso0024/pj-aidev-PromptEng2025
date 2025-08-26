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

def test_sort_numbers_basic():
    assert sort_numbers('nine eight seven six five four three two one zero') == 'zero one two three four five six seven eight nine'

def test_sort_numbers_mixed_order():
    assert sort_numbers('five two eight one zero') == 'zero one two five eight'

def test_sort_numbers_repeated_numbers():
    assert sort_numbers('one one two two three') == 'one one two two three'

def test_sort_numbers_empty_string():
    assert sort_numbers('') == ''

def test_sort_numbers_single_number():
    assert sort_numbers('five') == 'five'

@pytest.mark.parametrize("input_str,expected", [
    ('nine eight seven', 'seven eight nine'),
    ('zero', 'zero'),
    ('three one nine', 'zero one three nine'),
    ('', '')
])
def test_sort_numbers_parametrized(input_str, expected):
    assert sort_numbers(input_str) == expected

def test_sort_numbers_with_extra_spaces():
    assert sort_numbers('  one   two   three  ') == 'one two three'

def test_sort_numbers_case_sensitive():
    with pytest.raises(KeyError):
        sort_numbers('One Two Three')
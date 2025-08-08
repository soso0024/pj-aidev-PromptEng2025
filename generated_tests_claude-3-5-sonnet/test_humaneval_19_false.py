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
from typing import Optional

@pytest.mark.parametrize("input_str,expected", [
    ("one two three", "one two three"),
    ("three one zero", "zero one three"),
    ("zero nine five two", "zero two five nine"),
    ("", ""),
    ("one", "one"),
    ("nine eight seven six five four three two one zero", "zero one two three four five six seven eight nine"),
    ("five five five", "five five five"),
    ("eight five eight", "five eight eight"),
])
def test_sort_numbers_valid_inputs(input_str: str, expected: str):
    from sort_numbers import sort_numbers
    assert sort_numbers(input_str) == expected

@pytest.mark.parametrize("input_str", [
    "one two invalid",
    "invalid",
    "123",
    "one 123",
    "one TWO three",
])
def test_sort_numbers_invalid_inputs(input_str: str):
    with pytest.raises(KeyError):
        sort_numbers(input_str)

def test_sort_numbers_whitespace():
    assert sort_numbers("   one    two    three   ") == "one two three"
    assert sort_numbers("\tone\ntwo\tthree") == "one two three"

def test_sort_numbers_multiple_spaces():
    assert sort_numbers("one     two     three") == "one two three"

def test_sort_numbers_leading_trailing_spaces():
    assert sort_numbers("  one two three  ") == "one two three"

def test_sort_numbers_only_spaces():
    assert sort_numbers("   ") == ""

def test_sort_numbers_mixed_valid_and_spaces():
    assert sort_numbers("  one    two  three   ") == "one two three"
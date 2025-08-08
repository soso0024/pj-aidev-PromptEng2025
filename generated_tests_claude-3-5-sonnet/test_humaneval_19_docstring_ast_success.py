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


@pytest.mark.parametrize("input_str,expected", [
    ("three one five", "one three five"),
    ("zero one two three", "zero one two three"),
    ("nine eight seven", "seven eight nine"),
    ("one one one", "one one one"),
    ("nine zero", "zero nine"),
    ("five", "five"),
    ("", ""),
    ("   ", ""),
    ("zero zero zero", "zero zero zero"),
    ("nine eight seven six five four three two one zero",
     "zero one two three four five six seven eight nine"),
])
def test_sort_numbers_valid_inputs(input_str, expected):
    assert sort_numbers(input_str) == expected


@pytest.mark.parametrize("input_str", [
    "ten",
    "eleven",
    "one two THREE",
    "1 2 3",
    "invalid",
    "one two invalid",
    "zero one 2",
])
def test_sort_numbers_invalid_inputs(input_str):
    with pytest.raises(KeyError):
        sort_numbers(input_str)


def test_sort_numbers_multiple_spaces():
    assert sort_numbers("one   two     three") == "one two three"


def test_sort_numbers_leading_trailing_spaces():
    assert sort_numbers("  one  two  three  ") == "one two three"


def test_sort_numbers_single_number():
    for num in ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]:
        assert sort_numbers(num) == num


def test_sort_numbers_repeated_numbers():
    assert sort_numbers("one one one two two three") == "one one one two two three"


def test_sort_numbers_reverse_order():
    assert sort_numbers("nine eight seven six five four three two one zero") == \
           "zero one two three four five six seven eight nine"


def test_sort_numbers_empty_input():
    assert sort_numbers("") == ""
    assert sort_numbers(" ") == ""
    assert sort_numbers("  ") == ""

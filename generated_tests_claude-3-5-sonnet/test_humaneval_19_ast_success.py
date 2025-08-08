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
    assert sort_numbers("one two three") == "one two three"
    assert sort_numbers("three one two") == "one two three"

def test_sort_numbers_with_zeros():
    assert sort_numbers("zero one two three") == "zero one two three"
    assert sort_numbers("three two one zero") == "zero one two three"

def test_sort_numbers_with_duplicates():
    assert sort_numbers("one one two two") == "one one two two"

def test_sort_numbers_single_number():
    assert sort_numbers("one") == "one"

def test_sort_numbers_empty():
    assert sort_numbers("") == ""

def test_sort_numbers_with_spaces():
    assert sort_numbers("  one  two  ") == "one two"
    assert sort_numbers(" one   two three  ") == "one two three"

@pytest.mark.parametrize("input_str,expected", [
    ("one two three four five", "one two three four five"),
    ("nine eight seven six", "six seven eight nine"),
    ("zero one zero one", "zero zero one one"),
    ("five four three two one zero", "zero one two three four five"),
])
def test_sort_numbers_parametrized(input_str, expected):
    assert sort_numbers(input_str) == expected

@pytest.mark.parametrize("invalid_input", [
    "ten",
    "one two ten",
    "invalid",
    "1 2 3",
    "one two THREE"
])
def test_sort_numbers_invalid_input(invalid_input):
    with pytest.raises(KeyError):
        sort_numbers(invalid_input)

def test_sort_numbers_all_numbers():
    input_str = "zero one two three four five six seven eight nine"
    expected = "zero one two three four five six seven eight nine"
    assert sort_numbers(input_str) == expected

def test_sort_numbers_reverse():
    input_str = "nine eight seven six five four three two one zero"
    expected = "zero one two three four five six seven eight nine"
    assert sort_numbers(input_str) == expected
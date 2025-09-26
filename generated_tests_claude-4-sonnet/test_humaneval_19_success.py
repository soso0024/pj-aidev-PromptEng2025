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

def sort_numbers(numbers: str):
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

@pytest.mark.parametrize("input_str,expected", [
    ("three one five", "one three five"),
    ("nine eight seven six five four three two one zero", "zero one two three four five six seven eight nine"),
    ("zero", "zero"),
    ("five four three two one", "one two three four five"),
    ("one two three", "one two three"),
    ("nine zero five", "zero five nine"),
    ("eight seven six", "six seven eight"),
    ("two four six eight", "two four six eight"),
    ("one three five seven nine", "one three five seven nine"),
    ("zero two four six eight", "zero two four six eight")
])
def test_sort_numbers_normal_cases(input_str, expected):
    assert sort_numbers(input_str) == expected

def test_sort_numbers_empty_string():
    assert sort_numbers("") == ""

def test_sort_numbers_single_spaces():
    assert sort_numbers(" ") == ""

def test_sort_numbers_multiple_spaces():
    assert sort_numbers("   ") == ""

def test_sort_numbers_with_extra_spaces():
    assert sort_numbers("  three   one   five  ") == "one three five"

def test_sort_numbers_with_multiple_consecutive_spaces():
    assert sort_numbers("three  one    five") == "one three five"

def test_sort_numbers_all_same():
    assert sort_numbers("five five five") == "five five five"

def test_sort_numbers_duplicates_mixed():
    assert sort_numbers("three one three five one") == "one one three three five"

def test_sort_numbers_reverse_order():
    assert sort_numbers("nine eight seven") == "seven eight nine"

def test_sort_numbers_already_sorted():
    assert sort_numbers("one two three") == "one two three"

def test_sort_numbers_invalid_word():
    with pytest.raises(KeyError):
        sort_numbers("one two eleven")

def test_sort_numbers_mixed_valid_invalid():
    with pytest.raises(KeyError):
        sort_numbers("one two invalid three")

def test_sort_numbers_case_sensitive():
    with pytest.raises(KeyError):
        sort_numbers("One Two Three")

def test_sort_numbers_partial_match():
    with pytest.raises(KeyError):
        sort_numbers("on tw thre")

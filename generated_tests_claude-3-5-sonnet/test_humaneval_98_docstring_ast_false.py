# Test cases for HumanEval/98
# Generated using Claude API


def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """

    count = 0
    for i in range(0,len(s),2):
        if s[i] in "AEIOU":
            count += 1
    return count


# Generated test cases:
import pytest

def test_empty_string():
    assert count_upper("") == 0

def test_no_uppercase_vowels():
    assert count_upper("hello") == 0
    assert count_upper("bcdfgh") == 0

def test_uppercase_vowels_at_even_indices():
    assert count_upper("AbcdE") == 2
    assert count_upper("AEIOU") == 3

def test_uppercase_vowels_at_odd_indices():
    assert count_upper("bAbEbI") == 0

@pytest.mark.parametrize("input_str, expected", [
    ("AbcdEfghIj", 3),
    ("AAAAAA", 3),
    ("aEiOu", 0),
    ("A", 1),
    ("a", 0),
    ("AeIoUa", 3),
    ("HELLO", 1),
    ("hello", 0),
    ("hEllO", 1),
    ("", 0),
    ("12345", 0),
    ("A E I", 2),
    ("aEiOu", 0),
    ("AeIoU", 3)
])
def test_parametrized_cases(input_str, expected):
    assert count_upper(input_str) == expected

def test_single_char():
    assert count_upper("A") == 1
    assert count_upper("E") == 1
    assert count_upper("x") == 0

def test_special_characters():
    assert count_upper("A#E#I") == 3
    assert count_upper("#A#E#") == 0
    assert count_upper(" A E ") == 2

def test_mixed_case_string():
    assert count_upper("aAeEiIoOuU") == 0
    assert count_upper("AaEeIiOoUu") == 5

def test_numbers_and_letters():
    assert count_upper("A1E2I3O4U5") == 5
    assert count_upper("1A2E3I4O5U") == 0
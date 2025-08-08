# Test cases for HumanEval/16
# Generated using Claude API



def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    return len(set(string.lower()))


# Generated test cases:
import pytest

def test_basic_string():
    assert count_distinct_characters("hello") == 4

def test_case_insensitive():
    assert count_distinct_characters("hElLo") == 4

def test_empty_string():
    assert count_distinct_characters("") == 0

def test_single_character():
    assert count_distinct_characters("a") == 1

def test_all_same_character():
    assert count_distinct_characters("aaaa") == 1

def test_all_different_characters():
    assert count_distinct_characters("abcde") == 5

def test_mixed_case_same_letters():
    assert count_distinct_characters("aAaA") == 1

@pytest.mark.parametrize("input_str,expected", [
    ("xyzXYZ", 3),
    ("Jerry", 4),
    ("aAbBcC", 3),
    ("12345", 5),
    ("a1b2c3", 6),
    ("    ", 1),
    ("!@#$%", 5),
    ("Hello World", 8),
    ("Mississippi", 4),
    ("AaAaAa", 1)
])
def test_various_strings(input_str, expected):
    assert count_distinct_characters(input_str) == expected

def test_special_characters():
    assert count_distinct_characters("!@#!@#") == 3

def test_numbers_and_letters():
    assert count_distinct_characters("a1A1b2B2") == 4

def test_whitespace():
    assert count_distinct_characters("  \t\n  ") == 3

def test_unicode_characters():
    assert count_distinct_characters("üüÜÜööÖÖ") == 2

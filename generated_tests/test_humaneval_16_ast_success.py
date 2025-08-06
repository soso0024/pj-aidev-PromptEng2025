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

def test_empty_string():
    assert count_distinct_characters("") == 0

def test_single_character():
    assert count_distinct_characters("a") == 1

def test_repeated_characters():
    assert count_distinct_characters("aaa") == 1

def test_case_insensitive():
    assert count_distinct_characters("aAaA") == 1

@pytest.mark.parametrize("input_str,expected", [
    ("hello", 4),
    ("Hello World", 8),
    ("aabbccdd", 4),
    ("AbCdEfGh", 8),
    ("   ", 1),
    ("123", 3),
    ("!@#$%", 5),
    ("a1B2c3", 6),
    ("Python Programming", 12),
    ("UPPER lower MIXED", 12)
])
def test_various_strings(input_str, expected):
    assert count_distinct_characters(input_str) == expected

def test_special_characters():
    assert count_distinct_characters("!@#!@#") == 3

def test_numbers_and_letters():
    assert count_distinct_characters("a1a1b2b2") == 4

def test_whitespace():
    assert count_distinct_characters("   \t\n") == 3

def test_unicode_characters():
    assert count_distinct_characters("üüüñññ") == 2

@pytest.mark.parametrize("input_str", [None, 123, [], {}])
def test_invalid_input_type(input_str):
    with pytest.raises(AttributeError):
        count_distinct_characters(input_str)

def test_very_long_string():
    long_string = "abcdefghijklmnopqrstuvwxyz" * 1000
    assert count_distinct_characters(long_string) == 26

def test_all_ascii_printable():
    import string
    assert count_distinct_characters(string.printable) == len(set(string.printable.lower()))
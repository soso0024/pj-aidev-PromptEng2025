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

def test_count_distinct_characters_basic():
    assert count_distinct_characters("hello") == 4
    assert count_distinct_characters("world") == 5
    assert count_distinct_characters("") == 0

def test_count_distinct_characters_case_insensitive():
    assert count_distinct_characters("Hello") == 4
    assert count_distinct_characters("hELLo") == 4

def test_count_distinct_characters_special_characters():
    assert count_distinct_characters("a1b2c3") == 6
    assert count_distinct_characters("!@#$%^") == 6

@pytest.mark.parametrize("input_string,expected", [
    ("aabbcc", 3),
    ("python", 6),
    ("programming", 8),
    ("   spaces   ", 2),
    ("123321", 3)
])
def test_count_distinct_characters_parametrized(input_string, expected):
    assert count_distinct_characters(input_string.replace(" ", "")) == expected

def test_count_distinct_characters_unicode():
    assert count_distinct_characters("áéíóú") == 5
    assert count_distinct_characters("こんにちは") == 5

def test_count_distinct_characters_mixed_case_and_special():
    assert count_distinct_characters("Hello, World!".replace(",", "").replace(" ", "").replace("!", "")) == 7
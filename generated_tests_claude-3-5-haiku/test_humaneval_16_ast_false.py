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

def test_count_distinct_characters_normal_cases():
    assert count_distinct_characters("hello") == 4
    assert count_distinct_characters("world") == 5
    assert count_distinct_characters("python") == 5

def test_count_distinct_characters_case_insensitive():
    assert count_distinct_characters("Hello") == 4
    assert count_distinct_characters("hELLo") == 4

def test_count_distinct_characters_empty_string():
    assert count_distinct_characters("") == 0

def test_count_distinct_characters_repeated_characters():
    assert count_distinct_characters("aaaaaa") == 1
    assert count_distinct_characters("abcabcabc") == 3

def test_count_distinct_characters_special_characters():
    assert count_distinct_characters("!@#$%^") == 6
    assert count_distinct_characters("hello!") == 5

def test_count_distinct_characters_mixed_characters():
    assert count_distinct_characters("Hello, World!") == 7

@pytest.mark.parametrize("input_string,expected", [
    ("hello", 4),
    ("world", 5),
    ("python", 5),
    ("Hello", 4),
    ("", 0),
    ("aaaaaa", 1),
    ("!@#$%^", 6),
    ("Hello, World!", 7)
])
def test_count_distinct_characters_parametrized(input_string, expected):
    assert count_distinct_characters(input_string) == expected

def test_count_distinct_characters_unicode():
    assert count_distinct_characters("áéíóú") == 5
    assert count_distinct_characters("こんにちは") == 5
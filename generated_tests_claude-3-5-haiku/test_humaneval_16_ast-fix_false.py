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

def count_distinct_characters(string: str) -> int:
    return len(set(string.lower().replace(' ', '')))

def test_count_distinct_characters_normal_cases():
    assert count_distinct_characters("hello") == 4
    assert count_distinct_characters("python") == 5
    assert count_distinct_characters("aAaA") == 1
    assert count_distinct_characters("") == 0

def test_count_distinct_characters_case_insensitive():
    assert count_distinct_characters("Hello") == 4
    assert count_distinct_characters("WORLD") == 5

@pytest.mark.parametrize("input_string,expected", [
    ("", 0),
    ("a", 1),
    ("abcdefg", 7),
    ("aaaaaa", 1),
    ("123456", 6),
    ("!@#$%^", 6),
    ("MiXeD cAsE", 7)
])
def test_count_distinct_characters_parametrized(input_string, expected):
    assert count_distinct_characters(input_string) == expected

def test_count_distinct_characters_unicode():
    assert count_distinct_characters("áéíóú") == 5
    assert count_distinct_characters("こんにちは") == 5

def test_count_distinct_characters_whitespace():
    assert count_distinct_characters("  hello  ") == 4
    assert count_distinct_characters(" ") == 0
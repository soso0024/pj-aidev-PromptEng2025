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

def test_same_character_repeated():
    assert count_distinct_characters("aaa") == 1

def test_case_insensitive():
    assert count_distinct_characters("aAaA") == 1

@pytest.mark.parametrize("input_str,expected", [
    ("hello", 4),
    ("Hello World", 8),
    ("aabbccdd", 4),
    ("123123", 3),
    ("!@#$%", 5),
    ("AbCdEf", 6),
    ("   ", 1),
    ("a1B2c3", 6),
    ("Hello!!!", 5),
    ("Python Programming", 12)
])
def test_various_strings(input_str, expected):
    assert count_distinct_characters(input_str) == expected

@pytest.mark.parametrize("input_str", [
    "ñáéíóú",
    "über",
    "café",
    "中文字"
])
def test_unicode_strings(input_str):
    result = count_distinct_characters(input_str)
    assert isinstance(result, int)
    assert result > 0

def test_type_error():
    with pytest.raises(AttributeError):
        count_distinct_characters(None)

def test_numeric_input():
    with pytest.raises(AttributeError):
        count_distinct_characters(12345)

def test_special_characters():
    assert count_distinct_characters("!@#$%^&*()") == 10

def test_mixed_whitespace():
    assert count_distinct_characters("a b\tc\n") == 6

def test_very_long_string():
    long_string = "x" * 1000000
    assert count_distinct_characters(long_string) == 1
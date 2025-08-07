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

def test_count_distinct_characters_empty_string():
    assert count_distinct_characters("") == 0

def test_count_distinct_characters_single_character():
    assert count_distinct_characters("a") == 1

def test_count_distinct_characters_all_unique_characters():
    assert count_distinct_characters("abcdefghijklmnopqrstuvwxyz") == 26

def test_count_distinct_characters_mixed_case():
    assert count_distinct_characters("AbCdEfGhIjKlMnOpQrStUvWxYz") == 26

def test_count_distinct_characters_with_spaces():
    assert count_distinct_characters("hello world") == 10

def test_count_distinct_characters_with_numbers():
    assert count_distinct_characters("abc123xyz") == 9

def test_count_distinct_characters_with_special_characters():
    assert count_distinct_characters("!@#$%^&*()_+") == 12

@pytest.mark.parametrize("input,expected", [
    ("", 0),
    ("a", 1),
    ("abcdefghijklmnopqrstuvwxyz", 26),
    ("AbCdEfGhIjKlMnOpQrStUvWxYz", 26),
    ("hello world", 10),
    ("abc123xyz", 9),
    ("!@#$%^&*()_+", 12)
])
def test_count_distinct_characters_parametrized(input, expected):
    assert count_distinct_characters(input) == expected

def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))
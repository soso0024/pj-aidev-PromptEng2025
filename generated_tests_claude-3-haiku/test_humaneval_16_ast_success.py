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
    assert count_distinct_characters('') == 0

def test_count_distinct_characters_single_character():
    assert count_distinct_characters('a') == 1

def test_count_distinct_characters_multiple_characters():
    assert count_distinct_characters('hello') == 4

def test_count_distinct_characters_case_insensitive():
    assert count_distinct_characters('AbCdE') == 5

def test_count_distinct_characters_whitespace():
    assert count_distinct_characters('  ') == 1

@pytest.mark.parametrize("input_string,expected", [
    ('', 0),
    ('a', 1),
    ('hello', 4),
    ('AbCdE', 5),
    ('  ', 1)
])
def test_count_distinct_characters_parametrized(input_string, expected):
    assert count_distinct_characters(input_string) == expected

def test_count_distinct_characters_type_error():
    with pytest.raises(TypeError):
        count_distinct_characters(123)

def count_distinct_characters(string: str) -> int:
    if not isinstance(string, str):
        raise TypeError("Input must be a string")
    return len(set(string.lower()))
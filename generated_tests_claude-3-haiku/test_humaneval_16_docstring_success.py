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

def test_count_distinct_characters_mixed_case():
    assert count_distinct_characters('xyzXYZ') == 3

def test_count_distinct_characters_duplicate_characters():
    assert count_distinct_characters('Jerry') == 4

@pytest.mark.parametrize("input_string,expected", [
    ('', 0),
    ('a', 1),
    ('xyzXYZ', 3),
    ('Jerry', 4),
    ('aBcDeFgHiJkLmNoPqRsTuVwXyZ', 26),
    ('123456789', 9),
    ('!@#$%^&*()_+', 12),
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
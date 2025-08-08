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

def test_count_upper_empty_string():
    assert count_upper("") == 0

def test_count_upper_all_uppercase():
    assert count_upper("AEIOU") == 4

def test_count_upper_all_lowercase():
    assert count_upper("aeiou") == 0

def test_count_upper_mixed_case():
    assert count_upper("AbCdEfGhIjK") == 5

@pytest.mark.parametrize("input,expected", [
    ("Hello, World!", 1),
    ("Python is awesome!", 2),
    ("The quick brown fox jumps over the lazy dog.", 3),
    ("1234567890", 0),
])
def test_count_upper_parametrized(input, expected):
    assert count_upper(input) == expected

def test_count_upper_non_string_input():
    with pytest.raises(TypeError):
        count_upper(123)

def test_count_upper_none_input():
    with pytest.raises(TypeError):
        count_upper(None)
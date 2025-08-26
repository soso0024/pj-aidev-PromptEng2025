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

def test_count_upper_no_vowels():
    assert count_upper("bcd") == 0

def test_count_upper_all_vowels():
    assert count_upper("AEIOU") == 3

def test_count_upper_mixed_case():
    assert count_upper("AbCdEfG") == 2

def test_count_upper_long_string():
    assert count_upper("HELLO WORLD IS AWESOME") == 5

def test_count_upper_special_characters():
    assert count_upper("A!B@C#D$E%") == 3

@pytest.mark.parametrize("input_str,expected", [
    ("", 0),
    ("bcd", 0),
    ("AEIOU", 3),
    ("AbCdEfG", 2),
    ("HELLO WORLD IS AWESOME", 5),
    ("A!B@C#D$E%", 3)
])
def test_count_upper_parametrized(input_str, expected):
    assert count_upper(input_str) == expected

def test_count_upper_non_string_input():
    with pytest.raises(TypeError):
        count_upper(123)
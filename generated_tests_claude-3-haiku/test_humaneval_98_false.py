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

def test_count_upper_all_vowels():
    assert count_upper("AEIOU") == 4

def test_count_upper_mixed_case():
    assert count_upper("AbEiOu") == 3

def test_count_upper_non_vowels():
    assert count_upper("BCDFGHJKLMNPQRSTVWXYZ") == 0

@pytest.mark.parametrize("input_str,expected", [
    ("Hello World", 1),
    ("Python is awesome", 3),
    ("The quick brown fox", 0),
    ("AeIoU", 4),
    ("aeiou", 0)
])
def test_count_upper_parametrized(input_str, expected):
    assert count_upper(input_str) == expected

def count_upper(s):
    count = 0
    for i in range(0, len(s), 1):
        if s[i].upper() in "AEIOU":
            count += 1
    return count
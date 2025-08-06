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

def test_empty_string():
    assert count_upper("") == 0

def test_no_uppercase_vowels():
    assert count_upper("abcdef") == 0

def test_one_uppercase_vowel_even_index():
    assert count_upper("AbcdEf") == 2

def test_multiple_uppercase_vowels_even_indices():
    assert count_upper("AEIOU") == 3

def test_uppercase_vowels_odd_indices():
    assert count_upper("bAbEbI") == 0

def test_single_char():
    assert count_upper("A") == 1
    assert count_upper("b") == 0

@pytest.mark.parametrize("input_str,expected", [
    ("AbcdEf", 2),
    ("AEIOU", 3),
    ("aEiOu", 0),
    ("bAbEbI", 0),
    ("A", 1),
    ("", 0),
    ("aA", 0),
    ("Aa", 1),
    ("AAAAA", 3),
    ("12345", 0),
    ("A E I", 3),
    ("aEiOuAeIoU", 0)
])
def test_count_upper_parametrized(input_str, expected):
    assert count_upper(input_str) == expected

def test_special_characters():
    assert count_upper("A#B$E%") == 2

def test_with_spaces():
    assert count_upper("A E I") == 3

def test_with_numbers():
    assert count_upper("A2E4I6") == 3

def test_mixed_case_string():
    assert count_upper("aAeEiIoOuU") == 0

def test_all_uppercase():
    assert count_upper("ABCDEFG") == 2

def test_all_lowercase():
    assert count_upper("abcdefg") == 0
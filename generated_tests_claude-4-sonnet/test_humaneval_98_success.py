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

def count_upper(s):
    count = 0
    for i in range(0,len(s),2):
        if s[i] in "AEIOU":
            count += 1
    return count

def test_empty_string():
    assert count_upper("") == 0

def test_single_uppercase_vowel():
    assert count_upper("A") == 1

def test_single_lowercase_vowel():
    assert count_upper("a") == 0

def test_single_uppercase_consonant():
    assert count_upper("B") == 0

def test_single_lowercase_consonant():
    assert count_upper("b") == 0

def test_all_uppercase_vowels_even_positions():
    assert count_upper("AEIOU") == 3

def test_all_uppercase_vowels_odd_positions():
    assert count_upper("bAeIoU") == 0

def test_mixed_case_vowels():
    assert count_upper("AeIoU") == 3

def test_no_vowels():
    assert count_upper("BCDFG") == 0

def test_no_uppercase_vowels():
    assert count_upper("aeiou") == 0

def test_long_string_with_mixed_content():
    assert count_upper("AbCdEfGhIjKlMnOpQrStUvWxYz") == 5

def test_only_consonants_even_positions():
    assert count_upper("BcDfGhJkLmNpQrStVwXyZ") == 0

def test_alternating_uppercase_vowels():
    assert count_upper("ABABAB") == 3

def test_uppercase_vowels_at_even_indices():
    assert count_upper("AxExIxOxU") == 5

def test_uppercase_vowels_at_odd_indices():
    assert count_upper("xAxExIxOxU") == 0

@pytest.mark.parametrize("input_str,expected", [
    ("A", 1),
    ("AA", 1),
    ("AAA", 2),
    ("AAAA", 2),
    ("AAAAA", 3),
    ("aA", 0),
    ("Aa", 1),
    ("aAa", 0),
    ("AaA", 2),
    ("HELLO", 1),
    ("hello", 0),
    ("Programming", 0),
    ("PROGRAMMING", 2),
    ("12345", 0),
    ("A1E2I3O4U5", 5),
    ("!@#$%", 0),
    ("A!E@I#O$U%", 5)
])
def test_parametrized_cases(input_str, expected):
    assert count_upper(input_str) == expected

def test_string_with_spaces():
    assert count_upper("A B C D E") == 2

def test_string_with_numbers():
    assert count_upper("A1B2C3D4E") == 2

def test_string_with_special_characters():
    assert count_upper("A!B@C#D$E") == 2

def test_very_long_string():
    long_str = "A" + "b" * 1000 + "E" + "c" * 1000
    assert count_upper(long_str) == 1

def test_all_same_uppercase_vowel():
    assert count_upper("AAAAAAAAAA") == 5

def test_all_same_lowercase_vowel():
    assert count_upper("aaaaaaaaaa") == 0
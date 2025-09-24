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

def test_count_upper_example_cases():
    assert count_upper('aBCdEf') == 1
    assert count_upper('abcdefg') == 0
    assert count_upper('dBBE') == 0

def test_count_upper_empty_string():
    assert count_upper('') == 0

def test_count_upper_single_character():
    assert count_upper('A') == 1
    assert count_upper('E') == 1
    assert count_upper('I') == 1
    assert count_upper('O') == 1
    assert count_upper('U') == 1
    assert count_upper('a') == 0
    assert count_upper('B') == 0
    assert count_upper('z') == 0

def test_count_upper_two_characters():
    assert count_upper('AB') == 1
    assert count_upper('aB') == 0
    assert count_upper('Ea') == 1
    assert count_upper('bE') == 0

def test_count_upper_all_uppercase_vowels_even_indices():
    assert count_upper('AEIOU') == 3
    assert count_upper('AEIOUA') == 3

def test_count_upper_all_uppercase_vowels_odd_indices():
    assert count_upper('bAeIoU') == 0
    assert count_upper('xAxExI') == 0

def test_count_upper_mixed_case_vowels():
    assert count_upper('AeIoU') == 3
    assert count_upper('aEiOu') == 0
    assert count_upper('AeIoUa') == 3

def test_count_upper_no_vowels():
    assert count_upper('BCDFG') == 0
    assert count_upper('bcdfg') == 0
    assert count_upper('BcDfGh') == 0

def test_count_upper_consonants_and_vowels():
    assert count_upper('ABCDEF') == 2
    assert count_upper('abcdef') == 0
    assert count_upper('AbCdEf') == 2

def test_count_upper_long_string():
    assert count_upper('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 5
    assert count_upper('abcdefghijklmnopqrstuvwxyz') == 0

@pytest.mark.parametrize("input_str,expected", [
    ("A", 1),
    ("AA", 1),
    ("AAA", 2),
    ("AAAA", 2),
    ("AAAAA", 3),
    ("E", 1),
    ("EE", 1),
    ("EEE", 2),
    ("I", 1),
    ("O", 1),
    ("U", 1),
    ("UUUUU", 3),
    ("bUbUbU", 0),
    ("UbUbUb", 3),
    ("", 0)
])
def test_count_upper_parametrized(input_str, expected):
    assert count_upper(input_str) == expected

def test_count_upper_special_characters():
    assert count_upper('A!B@C#') == 1
    assert count_upper('!A@E#I') == 0
    assert count_upper('123A456') == 0
    assert count_upper('1A3E5I') == 2

def test_count_upper_spaces():
    assert count_upper('A B C') == 1
    assert count_upper(' A E I') == 0
    assert count_upper('A E I ') == 3
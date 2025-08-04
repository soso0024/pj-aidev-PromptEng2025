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
    assert count_upper("hello") == 0

def test_one_uppercase_vowel():
    assert count_upper("APPLE") == 1

def test_multiple_uppercase_vowels():
    assert count_upper("AEIOU") == 3

def test_mixed_case():
    assert count_upper("AeIoU") == 2

def test_only_consonants():
    assert count_upper("BCDFG") == 0

@pytest.mark.parametrize("input_str, expected", [
    ("A", 1),
    ("AA", 1),
    ("AAA", 2),
    ("AAAA", 2),
    ("aEiOu", 0),
    ("AEIOU", 3),
    ("aEiOuA", 1),
    ("BCDEFGHIJK", 0),
    ("abcdefghijk", 0),
    ("A E I O U", 3)
])
def test_parametrized_cases(input_str, expected):
    assert count_upper(input_str) == expected

def test_special_characters():
    assert count_upper("A#E$I") == 2

def test_numbers():
    assert count_upper("A1E2I3") == 2

def test_spaces():
    assert count_upper("A E I") == 2

@pytest.mark.parametrize("invalid_input", [
    None,
    123,
    3.14
])
def test_invalid_input_type(invalid_input):
    with pytest.raises((TypeError, AttributeError)):
        count_upper(invalid_input)
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

def test_no_vowels():
    assert count_upper("bcdfg") == 0

def test_all_vowels():
    assert count_upper("AEIOU") == 3

def test_mixed_case():
    assert count_upper("aEiOu") == 0

def test_single_char():
    assert count_upper("A") == 1

@pytest.mark.parametrize("input_str, expected", [
    ("APPLE", 2),
    ("ELEPHANT", 2),
    ("hello", 0),
    ("AaAaA", 3),
    ("AABBCC", 1),
    ("aEiOu", 0),
    ("AEIOUAEIOU", 5),
    ("B", 0),
    ("EA", 1),
    ("EeAaIiOoUu", 5)
])
def test_various_strings(input_str, expected):
    assert count_upper(input_str) == expected

@pytest.mark.parametrize("input_str", [
    "A E I O U",
    "AEIOU\n",
    "AEIOU\t",
    "AE IOU"
])
def test_strings_with_whitespace(input_str):
    result = count_upper(input_str)
    assert isinstance(result, int)
    assert result >= 0

def test_special_characters():
    assert count_upper("A#E$I") == 3

def test_numbers_mixed():
    assert count_upper("A1E2I3") == 3

def test_very_long_string():
    long_string = "AEIOU" * 1000
    assert count_upper(long_string) == 2500

@pytest.mark.parametrize("invalid_input", [
    None,
    123,
    3.14
])
def test_invalid_input_types(invalid_input):
    with pytest.raises((TypeError, AttributeError)):
        count_upper(invalid_input)
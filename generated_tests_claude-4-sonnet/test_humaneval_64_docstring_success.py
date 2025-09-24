# Test cases for HumanEval/64
# Generated using Claude API


FIX = """
Add more test cases.
"""

def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """

    vowels = "aeiouAEIOU"
    n_vowels = sum(c in vowels for c in s)
    if s[-1] == 'y' or s[-1] == 'Y':
        n_vowels += 1
    return n_vowels


# Generated test cases:
import pytest

def vowels_count(s):
    vowels = "aeiouAEIOU"
    n_vowels = sum(c in vowels for c in s)
    if s and (s[-1] == 'y' or s[-1] == 'Y'):
        n_vowels += 1
    return n_vowels

def test_vowels_count_basic_cases():
    assert vowels_count("abcde") == 2
    assert vowels_count("ACEDY") == 3

def test_vowels_count_empty_string():
    assert vowels_count("") == 0

def test_vowels_count_single_character():
    assert vowels_count("a") == 1
    assert vowels_count("A") == 1
    assert vowels_count("e") == 1
    assert vowels_count("i") == 1
    assert vowels_count("o") == 1
    assert vowels_count("u") == 1
    assert vowels_count("y") == 1
    assert vowels_count("Y") == 1
    assert vowels_count("b") == 0
    assert vowels_count("z") == 0

def test_vowels_count_y_at_end():
    assert vowels_count("happy") == 2
    assert vowels_count("HAPPY") == 2
    assert vowels_count("cry") == 1
    assert vowels_count("CRY") == 1
    assert vowels_count("sky") == 1

def test_vowels_count_y_not_at_end():
    assert vowels_count("yes") == 1
    assert vowels_count("YES") == 1
    assert vowels_count("yellow") == 2
    assert vowels_count("YELLOW") == 2
    assert vowels_count("gym") == 0
    assert vowels_count("GYM") == 0

def test_vowels_count_no_vowels():
    assert vowels_count("bcdfg") == 0
    assert vowels_count("BCDFG") == 0
    assert vowels_count("xyz") == 0
    assert vowels_count("XYZ") == 0

def test_vowels_count_all_vowels():
    assert vowels_count("aeiou") == 5
    assert vowels_count("AEIOU") == 5
    assert vowels_count("aeiouy") == 6
    assert vowels_count("AEIOUY") == 6

def test_vowels_count_mixed_case():
    assert vowels_count("AbCdE") == 2
    assert vowels_count("HeLLo") == 2
    assert vowels_count("WoRlD") == 1
    assert vowels_count("PytHoN") == 1

def test_vowels_count_repeated_vowels():
    assert vowels_count("aaa") == 3
    assert vowels_count("eee") == 3
    assert vowels_count("yyy") == 1
    assert vowels_count("aeiouaeiou") == 10

def test_vowels_count_long_words():
    assert vowels_count("beautiful") == 5
    assert vowels_count("BEAUTIFUL") == 5
    assert vowels_count("programming") == 3
    assert vowels_count("PROGRAMMING") == 3
    assert vowels_count("university") == 5
    assert vowels_count("UNIVERSITY") == 5

@pytest.mark.parametrize("word,expected", [
    ("hello", 2),
    ("HELLO", 2),
    ("world", 1),
    ("WORLD", 1),
    ("python", 1),
    ("PYTHON", 1),
    ("happy", 2),
    ("HAPPY", 2),
    ("try", 1),
    ("TRY", 1),
    ("rhythm", 0),
    ("RHYTHM", 0),
    ("fly", 1),
    ("FLY", 1),
    ("byte", 1),
    ("BYTE", 1)
])
def test_vowels_count_parametrized(word, expected):
    assert vowels_count(word) == expected
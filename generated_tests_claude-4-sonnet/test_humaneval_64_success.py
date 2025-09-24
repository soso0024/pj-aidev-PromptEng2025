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
    if s[-1] == 'y' or s[-1] == 'Y':
        n_vowels += 1
    return n_vowels

def test_empty_string():
    with pytest.raises(IndexError):
        vowels_count("")

def test_single_vowel():
    assert vowels_count("a") == 1
    assert vowels_count("A") == 1
    assert vowels_count("e") == 1
    assert vowels_count("i") == 1
    assert vowels_count("o") == 1
    assert vowels_count("u") == 1

def test_single_consonant():
    assert vowels_count("b") == 0
    assert vowels_count("z") == 0
    assert vowels_count("B") == 0
    assert vowels_count("Z") == 0

def test_single_y():
    assert vowels_count("y") == 1
    assert vowels_count("Y") == 1

def test_word_ending_with_y():
    assert vowels_count("happy") == 2
    assert vowels_count("Happy") == 2
    assert vowels_count("HAPPY") == 2
    assert vowels_count("cry") == 1
    assert vowels_count("sky") == 1

def test_word_ending_with_Y():
    assert vowels_count("happY") == 2
    assert vowels_count("crY") == 1
    assert vowels_count("skY") == 1

def test_word_with_y_not_at_end():
    assert vowels_count("yes") == 1
    assert vowels_count("yellow") == 2
    assert vowels_count("gym") == 0
    assert vowels_count("myth") == 0

def test_all_vowels():
    assert vowels_count("aeiou") == 5
    assert vowels_count("AEIOU") == 5
    assert vowels_count("aEiOu") == 5

def test_no_vowels():
    assert vowels_count("bcdfg") == 0
    assert vowels_count("BCDFG") == 0
    assert vowels_count("xyz") == 0

def test_mixed_case():
    assert vowels_count("Hello") == 2
    assert vowels_count("WoRlD") == 1
    assert vowels_count("PyThOn") == 1

def test_repeated_vowels():
    assert vowels_count("aaa") == 3
    assert vowels_count("eee") == 3
    assert vowels_count("aaay") == 4

def test_long_words():
    assert vowels_count("beautiful") == 5
    assert vowels_count("programming") == 3
    assert vowels_count("university") == 5

def test_words_with_numbers():
    assert vowels_count("a1e2i3") == 3
    assert vowels_count("test123") == 1
    assert vowels_count("123y") == 1

def test_words_with_special_characters():
    assert vowels_count("hello!") == 2
    assert vowels_count("a@e#i$") == 3
    assert vowels_count("test@y") == 2

@pytest.mark.parametrize("input_str,expected", [
    ("a", 1),
    ("hello", 2),
    ("happy", 2),
    ("cry", 1),
    ("bcdfg", 0),
    ("aeiou", 5),
    ("y", 1),
    ("yes", 1),
    ("gym", 0),
    ("HELLO", 2),
    ("HappY", 2)
])
def test_parametrized_cases(input_str, expected):
    assert vowels_count(input_str) == expected

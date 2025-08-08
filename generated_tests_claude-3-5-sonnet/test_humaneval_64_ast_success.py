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

@pytest.mark.parametrize("input_str,expected", [
    ("hello", 2),
    ("HELLO", 2),
    ("rhythm", 0),
    ("RHYTHM", 0),
    ("aeiou", 5),
    ("AEIOU", 5),
    ("sky", 1),
    ("SKY", 1),
    ("xyz", 0),
    ("XYZ", 0),
    ("AeIoUy", 6),
    ("aEiOuY", 6),
    ("programming", 3),
    ("PROGRAMMING", 3),
    ("aaa", 3),
    ("y", 1),
    ("Y", 1),
    ("bcdfg", 0),
    ("BCDFG", 0),
    ("AaEeIiOoUu", 10),
    ("aeiouY", 6),
    ("AEIOUY", 6),
    ("PyThOn", 1),
    ("python", 1),
    ("PYTHON", 1)
])
def test_vowels_count_parametrized(input_str, expected):
    assert vowels_count(input_str) == expected

def test_vowels_count_empty_string():
    with pytest.raises(IndexError):
        vowels_count("")

def test_vowels_count_single_char():
    assert vowels_count("a") == 1
    assert vowels_count("b") == 0
    assert vowels_count("y") == 1
    assert vowels_count("Y") == 1

def test_vowels_count_special_chars():
    assert vowels_count("a!e@i#o$u%") == 5
    assert vowels_count("123y") == 1
    assert vowels_count("a1e2i3o4u5y") == 6

def test_vowels_count_mixed_case():
    assert vowels_count("aEiOuY") == 6
    assert vowels_count("PyThOn") == 1
    assert vowels_count("HELLO") == 2

def test_vowels_count_consecutive_vowels():
    assert vowels_count("aeiouaeiou") == 10
    assert vowels_count("AEIOUAEIOU") == 10
    assert vowels_count("aaaaay") == 6
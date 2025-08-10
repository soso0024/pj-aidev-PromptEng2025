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

def test_vowels_count_empty_string():
    assert vowels_count("") == 0

def test_vowels_count_all_vowels():
    assert vowels_count("aeiouAEIOU") == 10

def test_vowels_count_mixed_case():
    assert vowels_count("Hello World") == 3

def test_vowels_count_with_y():
    assert vowels_count("sky") == 2

def test_vowels_count_with_uppercase_y():
    assert vowels_count("icy") == 2

@pytest.mark.parametrize("input,expected", [
    ("apple", 2),
    ("banana", 3),
    ("hello", 2),
    ("world", 1),
    ("rhythm", 0),
    ("queue", 3),
    ("aeiou", 5),
    ("AEIOU", 5),
    ("AEIOUaeiou", 10),
    ("yay", 2),
    ("Yay", 2),
    ("", 0)
])
def test_vowels_count_parametrized(input, expected):
    assert vowels_count(input) == expected
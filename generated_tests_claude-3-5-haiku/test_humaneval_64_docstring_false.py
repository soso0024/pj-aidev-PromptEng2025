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

def test_vowels_count_basic_lowercase():
    assert vowels_count("hello") == 2
    assert vowels_count("world") == 1
    assert vowels_count("python") == 1

def test_vowels_count_uppercase():
    assert vowels_count("HELLO") == 2
    assert vowels_count("WORLD") == 1
    assert vowels_count("PYTHON") == 1

def test_vowels_count_mixed_case():
    assert vowels_count("HeLLo") == 2
    assert vowels_count("WoRlD") == 1

def test_vowels_count_with_y_at_end():
    assert vowels_count("sky") == 1
    assert vowels_count("SKY") == 1
    assert vowels_count("happy") == 2

def test_vowels_count_no_vowels():
    assert vowels_count("rhythm") == 0
    assert vowels_count("cry") == 1

def test_vowels_count_all_vowels():
    assert vowels_count("aeiou") == 5
    assert vowels_count("AEIOU") == 5

def test_vowels_count_empty_string():
    assert vowels_count("") == 0

@pytest.mark.parametrize("input_str,expected", [
    ("hello", 2),
    ("WORLD", 1),
    ("PytHon", 1),
    ("sky", 1),
    ("rhythm", 0),
    ("aEiOu", 5),
    ("", 0)
])
def test_vowels_count_parametrized(input_str, expected):
    assert vowels_count(input_str) == expected
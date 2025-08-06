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

def test_empty_string():
    assert vowels_count("") == 0

def test_single_vowel():
    assert vowels_count("a") == 1

def test_single_consonant():
    assert vowels_count("b") == 0

def test_y_at_end():
    assert vowels_count("happy") == 2

def test_y_not_at_end():
    assert vowels_count("yellow") == 2

@pytest.mark.parametrize("input_str, expected", [
    ("hello", 2),
    ("HELLO", 2),
    ("aeiou", 5),
    ("AEIOU", 5),
    ("rhythm", 0),
    ("sky", 1),
    ("SKY", 1),
    ("aEiOu", 5),
    ("python", 1),
    ("PYTHON", 1),
    ("syzygy", 1),
    ("SYZYGY", 1),
    ("AaEeIiOoUu", 10),
    ("xyzY", 1),
    ("ayyy", 2),
    ("AYYY", 2)
])
def test_vowels_count_parametrized(input_str, expected):
    assert vowels_count(input_str) == expected

def test_special_characters():
    assert vowels_count("he!!o") == 2

def test_numbers():
    assert vowels_count("h3ll0") == 2

def test_mixed_case():
    assert vowels_count("hElLo") == 2

def test_all_vowels():
    assert vowels_count("aeiouAEIOU") == 10

def test_no_vowels():
    assert vowels_count("bcdfg") == 0

def test_only_y():
    assert vowels_count("y") == 1

def test_multiple_y():
    assert vowels_count("yyyy") == 1

def test_spaces():
    assert vowels_count("a e") == 2
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
from FIX import vowels_count
import pytest

@pytest.mark.parametrize("input,expected", [
    ("abcde", 2),
    ("ACEDY", 3),
    ("hello", 2),
    ("world", 1),
    ("aeiou", 5),
    ("AEIOU", 5),
    ("Python", 2),
    ("", 0),
    ("y", 1),
    ("Y", 1),
    ("Py thon", 2),
    ("HeLlO", 2),
    ("aEiOu", 5),
    ("AeIoU", 5),
    ("HaPpY", 3),
    ("yay", 2),
    ("YAY", 3),
    ("pYthon", 2),
    ("PyThon", 3),
    ("pYtHoN", 3),
])
def test_vowels_count(input, expected):
    assert vowels_count(input) == expected

def test_vowels_count_edge_cases():
    assert vowels_count("") == 0
    assert vowels_count("y") == 1
    assert vowels_count("Y") == 1

def test_vowels_count_error_handling():
    with pytest.raises(TypeError):
        vowels_count(123)
    with pytest.raises(TypeError):
        vowels_count(None)
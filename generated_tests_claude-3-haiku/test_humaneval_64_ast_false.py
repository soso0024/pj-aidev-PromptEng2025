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
from your_module import vowels_count
import pytest

@pytest.mark.parametrize("input_str, expected", [
    ("hello", 2),
    ("aeiou", 5),
    ("AEIOU", 5),
    ("hello world", 3),
    ("y", 1),
    ("Y", 1),
    ("", 0),
    ("HeLlO", 2),
    ("hello, how are you?", 3),
    ("Python is awesome!", 3),
])
def test_vowels_count(input_str, expected):
    assert vowels_count(input_str) == expected

def test_vowels_count_edge_cases():
    assert vowels_count("y") == 1
    assert vowels_count("Y") == 1
    assert vowels_count("") == 0

def test_vowels_count_error():
    with pytest.raises(TypeError):
        vowels_count(123)
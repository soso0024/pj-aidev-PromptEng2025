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

def test_vowels_count_empty_string():
    assert vowels_count("") == 0

def test_vowels_count_all_vowels():
    assert vowels_count("aeiouAEIOU") == 10

def test_vowels_count_mixed_case():
    assert vowels_count("Hello World") == 3

def test_vowels_count_with_y():
    assert vowels_count("sky") == 2

@pytest.mark.parametrize("input,expected", [
    ("apple", 2),
    ("banana", 3),
    ("hello", 2),
    ("rhythm", 2),
    ("strength", 2),
    ("syzygy", 3)
])
def test_vowels_count_various_inputs(input, expected):
    assert vowels_count(input) == expected

def test_vowels_count_non_string_input():
    with pytest.raises(TypeError):
        vowels_count(123)
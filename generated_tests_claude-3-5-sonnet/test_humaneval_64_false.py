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

def test_basic_vowels():
    assert vowels_count("hello") == 2
    assert vowels_count("world") == 1

def test_all_vowels():
    assert vowels_count("aeiou") == 5
    assert vowels_count("AEIOU") == 5

def test_no_vowels():
    assert vowels_count("rhythm") == 0
    assert vowels_count("crypt") == 0

def test_y_ending():
    assert vowels_count("happy") == 2
    assert vowels_count("sky") == 1
    assert vowels_count("HAPPY") == 2
    assert vowels_count("SKY") == 1

@pytest.mark.parametrize("input_str,expected", [
    ("hello", 2),
    ("HELLO", 2),
    ("aeiou", 5),
    ("AEIOU", 5),
    ("rhythm", 0),
    ("crypt", 0),
    ("happy", 2),
    ("sky", 1),
    ("HAPPY", 2),
    ("SKY", 1),
    ("xyz", 0),
    ("aEiOu", 5),
    ("AeIoU", 5),
    ("programming", 3),
    ("PROGRAMMING", 3),
    ("aY", 2),
    ("Ay", 2)
])
def test_vowels_parametrized(input_str, expected):
    assert vowels_count(input_str) == expected

def test_empty_string():
    with pytest.raises(IndexError):
        vowels_count("")

def test_mixed_case():
    assert vowels_count("hElLo") == 2
    assert vowels_count("wOrLd") == 1

@pytest.mark.parametrize("input_str", [
    None,
    123,
    3.14
])
def test_invalid_inputs(input_str):
    with pytest.raises((AttributeError, TypeError)):
        vowels_count(input_str)

def test_invalid_sequence_inputs():
    with pytest.raises((AttributeError, TypeError, IndexError)):
        vowels_count(["h", "e", "l", "l", "o"])
    with pytest.raises((AttributeError, TypeError, IndexError)):
        vowels_count({"hello": "world"})
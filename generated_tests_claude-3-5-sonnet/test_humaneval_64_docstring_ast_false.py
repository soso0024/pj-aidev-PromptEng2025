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
    assert vowels_count("cry") == 1

def test_y_at_end():
    assert vowels_count("happy") == 2
    assert vowels_count("HAPPY") == 2
    assert vowels_count("yearly") == 3

def test_y_not_at_end():
    assert vowels_count("yellow") == 2
    assert vowels_count("yesterday") == 4

@pytest.mark.parametrize("input_str,expected", [
    ("hello", 2),
    ("HELLO", 2),
    ("aEiOu", 5),
    ("rhythm", 0),
    ("happy", 2),
    ("HAPPY", 2),
    ("yellow", 2),
    ("cry", 1),
    ("sky", 1),
    ("python", 2),
    ("PYTHON", 2),
    ("aaa", 3),
    ("xyz", 0),
    ("AeIoUy", 6),
    ("yay", 2),
    ("YAY", 2)
])
def test_parametrized_cases(input_str, expected):
    assert vowels_count(input_str) == expected

def test_single_letter():
    assert vowels_count("a") == 1
    assert vowels_count("y") == 1
    assert vowels_count("x") == 0

def test_empty_string():
    with pytest.raises(IndexError):
        vowels_count("")

def test_mixed_case():
    assert vowels_count("AbCdEiOuY") == 6
    assert vowels_count("mIxEdCaSe") == 4

def test_repeated_vowels():
    assert vowels_count("aaa") == 3
    assert vowels_count("eee") == 3
    assert vowels_count("ooo") == 3

def test_special_y_cases():
    assert vowels_count("yyy") == 1
    assert vowels_count("YYY") == 1
    assert vowels_count("yay") == 2
    assert vowels_count("YAY") == 2
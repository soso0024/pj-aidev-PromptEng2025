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
    ("abcde", 2),
    ("ACEDY", 3),
    ("hello", 2),
    ("world", 1),
    ("Python", 2),
    ("aeiou", 5),
    ("AEIOU", 5),
    ("", 0),
    ("y", 1),
    ("Y", 1),
    ("Aye", 2),
    ("Eyrie", 3),
    ("Iota", 3),
    ("Oahu", 3),
    ("Ugli", 2),
    ("Rhythm", 0),
    ("Hymn", 1),
    ("Crypt", 0),
    ("Myrrh", 1),
    ("Syzygy", 2)
])
def test_vowels_count(input_str, expected):
    from vowels_count import vowels_count
    assert vowels_count(input_str) == expected

def test_vowels_count_raises_error():
    with pytest.raises(TypeError):
        vowels_count(123)
# Test cases for HumanEval/51
# Generated using Claude API



def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """

    return "".join([s for s in text if s.lower() not in ["a", "e", "i", "o", "u"]])


# Generated test cases:
import pytest
import unicodedata

def remove_vowels(text):
    return "".join([s for s in text if s.lower() not in ["a", "e", "i", "o", "u"]])

def test_remove_vowels_basic():
    assert remove_vowels("hello") == "hll"
    assert remove_vowels("world") == "wrld"

def test_remove_vowels_empty_string():
    assert remove_vowels("") == ""

def test_remove_vowels_no_vowels():
    assert remove_vowels("rhythm") == "rhythm"

def test_remove_vowels_all_vowels():
    assert remove_vowels("aeiou") == ""

def test_remove_vowels_mixed_case():
    assert remove_vowels("HeLLo WoRLd") == "HLL WRLd"

def test_remove_vowels_with_numbers_and_symbols():
    assert remove_vowels("h3ll0 w0rld!") == "h3ll0 w0rld!"

def test_remove_vowels_unicode():
    assert remove_vowels("áéíóú") == ""

@pytest.mark.parametrize("input_text,expected", [
    ("hello", "hll"),
    ("world", "wrld"),
    ("", ""),
    ("rhythm", "rhythm"),
    ("aeiou", ""),
    ("HeLLo WoRLd", "HLL WRLd"),
    ("h3ll0 w0rld!", "h3ll0 w0rld!")
])
def test_remove_vowels_parametrized(input_text, expected):
    assert remove_vowels(input_text) == expected
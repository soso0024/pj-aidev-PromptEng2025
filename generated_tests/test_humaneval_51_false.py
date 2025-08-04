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

@pytest.mark.parametrize("text,expected", [
    ("hello", "hll"),
    ("HELLO", "HLL"),
    ("Python", "Pythn"),
    ("aeiou", ""),
    ("AEIOU", ""),
    ("", ""),
    ("xyz", "xyz"),
    ("AeIoU", ""),
    ("Hello World!", "Hll Wrld!"),
    ("123", "123"),
    ("a1e2i3o4u5", "12345"),
    ("Mixed CASE vOwEls", "Mxd CS vwls"),
    (" spaces ", " spcs "),
    ("!@#$%^&*()", "!@#$%^&*()"),
    ("aEiOu12345AeIoU", "12345"),
])
def test_remove_vowels_parametrized(text, expected):
    assert remove_vowels(text) == expected

def test_remove_vowels_none_input():
    with pytest.raises(TypeError):
        remove_vowels(None)

def test_remove_vowels_number_input():
    with pytest.raises(TypeError):
        remove_vowels(12345)

def test_remove_vowels_list_input():
    with pytest.raises(AttributeError):
        remove_vowels(['h', 'e', 'l', 'l', 'o'])

def test_remove_vowels_empty_string():
    assert remove_vowels("") == ""

def test_remove_vowels_only_vowels():
    assert remove_vowels("aeiouAEIOU") == ""

def test_remove_vowels_only_consonants():
    assert remove_vowels("bcdfghjklmnpqrstvwxyz") == "bcdfghjklmnpqrstvwxyz"

def test_remove_vowels_special_characters():
    assert remove_vowels("!@#$%^&*()_+") == "!@#$%^&*()_+"

def test_remove_vowels_whitespace():
    assert remove_vowels("   ") == "   "
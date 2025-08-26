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

def test_remove_vowels_basic_string():
    assert remove_vowels("hello") == "hll"
    assert remove_vowels("world") == "wrld"

def test_remove_vowels_uppercase():
    assert remove_vowels("HELLO") == "HLL"
    assert remove_vowels("WORLD") == "WRLD"

def test_remove_vowels_mixed_case():
    assert remove_vowels("HeLLo") == "HLL"
    assert remove_vowels("WoRlD") == "WRlD"

def test_remove_vowels_with_spaces():
    assert remove_vowels("hello world") == "hll wrld"

def test_remove_vowels_with_punctuation():
    assert remove_vowels("hello, world!") == "hll, wrld!"

def test_remove_vowels_empty_string():
    assert remove_vowels("") == ""

def test_remove_vowels_only_vowels():
    assert remove_vowels("aeiou") == ""
    assert remove_vowels("AEIOU") == ""

@pytest.mark.parametrize("input_text,expected", [
    ("hello", "hll"),
    ("WORLD", "WRLD"),
    ("MiXeD CaSe", "MxD Cs"),
    ("a1e2i3o4u5", "12345"),
    ("No Vowels", "N Vwls")
])
def test_remove_vowels_parametrized(input_text, expected):
    assert remove_vowels(input_text) == expected
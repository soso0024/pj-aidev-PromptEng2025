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

def remove_vowels(text):
    return "".join([s for s in text if s.lower() not in ["a", "e", "i", "o", "u"]])

def test_remove_vowels_empty_string():
    assert remove_vowels("") == ""

def test_remove_vowels_string_with_vowels():
    assert remove_vowels("abcdef\nghijklm") == "bcdf\nghjklm"

def test_remove_vowels_string_without_vowels():
    assert remove_vowels("zbcd") == "zbcd"

def test_remove_vowels_string_with_all_vowels():
    assert remove_vowels("aaaaa") == ""

def test_remove_vowels_string_with_mixed_case_vowels():
    assert remove_vowels("aaBAA") == "B"

@pytest.mark.parametrize("input,expected", [
    ("", ""),
    ("abcdef\nghijklm", "bcdf\nghjklm"),
    ("abcdef", "bcdf"),
    ("aaaaa", ""),
    ("aaBAA", "B"),
    ("zbcd", "zbcd")
])
def test_remove_vowels_parametrized(input, expected):
    assert remove_vowels(input) == expected

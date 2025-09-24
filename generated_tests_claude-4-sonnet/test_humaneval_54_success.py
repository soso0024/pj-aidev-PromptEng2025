# Test cases for HumanEval/54
# Generated using Claude API



def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars('abcd', 'dddddddabc')
    True
    >>> same_chars('dddddddabc', 'abcd')
    True
    >>> same_chars('eabcd', 'dddddddabc')
    False
    >>> same_chars('abcd', 'dddddddabce')
    False
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """

    return set(s0) == set(s1)


# Generated test cases:
import pytest

def same_chars(s0: str, s1: str):
    return set(s0) == set(s1)

def test_same_chars_identical_strings():
    assert same_chars("abc", "abc") == True

def test_same_chars_different_order():
    assert same_chars("abc", "bca") == True

def test_same_chars_different_characters():
    assert same_chars("abc", "def") == False

def test_same_chars_empty_strings():
    assert same_chars("", "") == True

def test_same_chars_one_empty_one_not():
    assert same_chars("", "a") == False
    assert same_chars("a", "") == False

def test_same_chars_repeated_characters():
    assert same_chars("aab", "ab") == True
    assert same_chars("aaa", "a") == True
    assert same_chars("abc", "aabbcc") == True

def test_same_chars_different_lengths_same_chars():
    assert same_chars("hello", "helo") == True
    assert same_chars("programming", "grampoin") == True

def test_same_chars_case_sensitive():
    assert same_chars("Abc", "abc") == False
    assert same_chars("ABC", "abc") == False

def test_same_chars_special_characters():
    assert same_chars("!@#", "#@!") == True
    assert same_chars("a!b@", "@!ba") == True
    assert same_chars("123", "321") == True

def test_same_chars_whitespace():
    assert same_chars("a b", "ba ") == True
    assert same_chars(" ", "  ") == True
    assert same_chars("a b", "ab") == False

def test_same_chars_unicode():
    assert same_chars("αβγ", "γβα") == True
    assert same_chars("αβγ", "αβδ") == False

@pytest.mark.parametrize("s0,s1,expected", [
    ("", "", True),
    ("a", "a", True),
    ("ab", "ba", True),
    ("abc", "def", False),
    ("hello", "world", False),
    ("listen", "silent", True),
    ("aab", "aba", True),
    ("abc", "abcd", False),
    ("123", "321", True),
    ("!@#$", "$#@!", True)
])
def test_same_chars_parametrized(s0, s1, expected):
    assert same_chars(s0, s1) == expected

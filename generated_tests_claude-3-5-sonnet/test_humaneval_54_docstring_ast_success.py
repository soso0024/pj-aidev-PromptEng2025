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

def test_same_chars_basic():
    assert same_chars('abc', 'cba') == True
    assert same_chars('abc', 'abc') == True
    assert same_chars('', '') == True

@pytest.mark.parametrize("s0,s1,expected", [
    ("eabcdzzzz", "dddzzzzzzzddeddabc", True),
    ("abcd", "dddddddabc", True),
    ("dddddddabc", "abcd", True),
    ("eabcd", "dddddddabc", False),
    ("abcd", "dddddddabce", False),
    ("eabcdzzzz", "dddzzzzzzzddddabc", False),
    ("", "", True),
    ("a", "a", True),
    ("aaa", "a", True),
    ("abc", "def", False),
    ("  ", " ", True),
    ("!@#", "#@!", True),
    ("aB", "Ba", True),
    ("aB", "BA", False)
])
def test_same_chars_parametrized(s0, s1, expected):
    assert same_chars(s0, s1) == expected

def test_same_chars_special_characters():
    assert same_chars("!@#$%", "%$#@!") == True
    assert same_chars("\n\t\r", "\r\t\n") == True
    assert same_chars("αβγ", "γβα") == True

def test_same_chars_empty_and_spaces():
    assert same_chars("", "") == True
    assert same_chars(" ", " ") == True
    assert same_chars("   ", " ") == True
    assert same_chars("", " ") == False

def test_same_chars_case_sensitivity():
    assert same_chars("ABC", "abc") == False
    assert same_chars("aA", "Aa") == True
    assert same_chars("AbC", "CAb") == True

def test_same_chars_numbers():
    assert same_chars("123", "321") == True
    assert same_chars("111", "1") == True
    assert same_chars("123", "1234") == False

def test_same_chars_mixed_content():
    assert same_chars("a1B2", "B2a1") == True
    assert same_chars("a1B2!", "!B2a1") == True
    assert same_chars("a1B2", "B2a1C") == False

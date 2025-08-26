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

def test_same_chars_basic_match():
    assert same_chars("abc", "cab") == True

def test_same_chars_basic_no_match():
    assert same_chars("abc", "def") == False

def test_same_chars_empty_strings():
    assert same_chars("", "") == True

def test_same_chars_different_lengths():
    assert same_chars("abc", "abcd") == False

def test_same_chars_case_sensitive():
    assert same_chars("abc", "ABC") == False

def test_same_chars_repeated_chars():
    assert same_chars("aabbcc", "abcabc") == True

@pytest.mark.parametrize("s0,s1,expected", [
    ("hello", "olleh", True),
    ("python", "typhon", True),
    ("test", "best", False),
    ("", "", True),
    ("a", "a", True),
    ("abc", "cab", True),
    ("abc", "def", False)
])
def test_same_chars_parametrized(s0, s1, expected):
    assert same_chars(s0, s1) == expected

def test_same_chars_unicode():
    assert same_chars("résumé", "sumér") == True

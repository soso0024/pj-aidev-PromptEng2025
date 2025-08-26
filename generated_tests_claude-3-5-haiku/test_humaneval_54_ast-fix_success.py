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

def test_same_chars_identical_strings():
    assert same_chars("hello", "hello") == True

def test_same_chars_different_order():
    assert same_chars("abc", "cab") == True

def test_same_chars_different_lengths():
    assert same_chars("abc", "abcd") == False

def test_same_chars_empty_strings():
    assert same_chars("", "") == True

def test_same_chars_one_empty_string():
    assert same_chars("abc", "") == False

def test_same_chars_case_sensitive():
    assert same_chars("ABC", "abc") == False

def test_same_chars_repeated_chars():
    assert same_chars("aabbcc", "abcabc") == True

@pytest.mark.parametrize("s0,s1,expected", [
    ("hello", "olleh", True),
    ("python", "typhon", True),
    ("test", "best", False),
    ("", "", True),
    ("a", "a", True),
    ("abc", "def", False)
])
def test_same_chars_parametrized(s0, s1, expected):
    assert same_chars(s0, s1) == expected

def test_same_chars_unicode():
    assert same_chars("café", "ecaf") == False

def test_same_chars_whitespace():
    assert same_chars("a b c", "c a b") == True

def test_same_chars_special_chars():
    assert same_chars("!@#", "#@!") == True

def test_same_chars_mixed_chars():
    assert same_chars("a1b2c3", "3c2b1a") == True
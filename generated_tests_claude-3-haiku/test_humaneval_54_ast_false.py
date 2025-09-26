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

def test_same_chars_empty_strings():
    assert same_chars("", "")

def test_same_chars_single_char_strings():
    assert same_chars("a", "a")
    assert not same_chars("a", "b")

def test_same_chars_different_length_strings():
    assert not same_chars("abc", "ab")
    assert not same_chars("abc", "abcd")

@pytest.mark.parametrize("s0,s1,expected", [
    ("hello", "world", False),
    ("python", "java", False),
    ("listen", "silent", True),
    ("debit card", "bad credit", True),
    ("A gentleman", "Elegant man", True),
    ("python", "ythonp", True),
    ("aabbcc", "bbccaa", True)
])
def test_same_chars_various_inputs(s0, s1, expected):
    assert same_chars(s0, s1) == expected

def test_same_chars_with_non_string_inputs():
    with pytest.raises(TypeError):
        same_chars(123, "abc")
    with pytest.raises(TypeError):
        same_chars("abc", 123)

def same_chars(s0: str, s1: str):
    return set(str(s0).lower()) == set(str(s1).lower())
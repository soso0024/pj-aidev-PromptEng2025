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
    assert same_chars("", "") == True

def test_same_chars_single_char():
    assert same_chars("a", "a") == True

def test_same_chars_different_order():
    assert same_chars("abc", "cba") == True

def test_same_chars_different_strings():
    assert same_chars("abc", "def") == False

def test_same_chars_repeated_chars():
    assert same_chars("aabb", "abab") == True

@pytest.mark.parametrize("s0, s1, expected", [
    ("hello", "olleh", True),
    ("python", "typhon", True),
    ("test", "best", False),
    ("", "", True),
    ("aaa", "a", True),
    ("abc", "abcd", False),
    ("12345", "54321", True),
    ("!@#", "#@!", True),
    ("aabbcc", "abcabc", True),
    ("space test", "test space", True),
])
def test_same_chars_parametrized(s0, s1, expected):
    assert same_chars(s0, s1) == expected

def test_same_chars_case_sensitive():
    assert same_chars("ABC", "abc") == False

def test_same_chars_special_chars():
    assert same_chars("!@#$%", "%$#@!") == True

def test_same_chars_whitespace():
    assert same_chars("  ", " ") == True

def test_same_chars_numbers():
    assert same_chars("123", "321") == True

@pytest.mark.parametrize("invalid_input", [
    None,
    123,
    3.14,
    True
])
def test_same_chars_invalid_input(invalid_input):
    with pytest.raises(TypeError):
        same_chars(invalid_input, "test")
    with pytest.raises(TypeError):
        same_chars("test", invalid_input)

def test_same_chars_list_input():
    with pytest.raises(AttributeError):
        same_chars([], "test")
    with pytest.raises(AttributeError):
        same_chars("test", [])

def test_same_chars_dict_input():
    with pytest.raises(AttributeError):
        same_chars({}, "test")
    with pytest.raises(AttributeError):
        same_chars("test", {})
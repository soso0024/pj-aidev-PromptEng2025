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

def test_same_chars_single_character():
    assert same_chars("a", "a") == True

def test_same_chars_different_order():
    assert same_chars("abc", "cba") == True

def test_same_chars_different_strings():
    assert same_chars("abc", "def") == False

@pytest.mark.parametrize("s0, s1, expected", [
    ("hello", "olleh", True),
    ("python", "typhon", True),
    ("test", "best", False),
    ("aaa", "a", True),
    ("", "a", False),
    ("a", "", False),
    ("aabbcc", "abc", True),
    ("abc", "abcc", True),
    ("  ", "  ", True),
    ("!@#", "#@!", True),
    ("case", "Case", False),
    ("12345", "54321", True),
    ("aabbcc", "aabbcc", True),
    ("ab\n", "a\nb", True),
    ("", "", True)
])
def test_same_chars_parametrized(s0, s1, expected):
    assert same_chars(s0, s1) == expected

def test_same_chars_special_characters():
    assert same_chars("!@#$%", "%$#@!") == True

def test_same_chars_spaces():
    assert same_chars("a b c", "c b a") == True

def test_same_chars_case_sensitive():
    assert same_chars("Hello", "hello") == False

def test_same_chars_numbers():
    assert same_chars("123", "321") == True

def test_same_chars_mixed_types():
    assert same_chars("a1b2", "2b1a") == True

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
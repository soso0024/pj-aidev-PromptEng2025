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

def test_same_chars_equal_strings():
    assert same_chars("hello", "hello")

def test_same_chars_different_strings():
    assert not same_chars("hello", "world")

@pytest.mark.parametrize("s0,s1,expected", [
    ("", "", True),
    ("a", "a", True),
    ("abc", "cba", True),
    ("hello", "world", False),
    ("Python", "java", False),
    ("  ", "   ", True),
    ("123", "321", True),
    ("AaBbCc", "aabbcc", False)
])
def test_same_chars_parametrized(s0, s1, expected):
    assert same_chars(s0, s1) == expected

def test_same_chars_with_non_string_input():
    with pytest.raises(TypeError):
        same_chars(123, 456)
    with pytest.raises(TypeError):
        same_chars([1, 2, 3], [4, 5, 6])

def same_chars(s0: str, s1: str):
    return set(s0) == set(s1)
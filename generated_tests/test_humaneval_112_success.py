# Test cases for HumanEval/112
# Generated using Claude API


def reverse_delete(s,c):
    """Task
    We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.
    Example
    For s = "abcde", c = "ae", the result should be ('bcd',False)
    For s = "abcdef", c = "b"  the result should be ('acdef',False)
    For s = "abcdedcba", c = "ab", the result should be ('cdedc',True)
    """

    s = ''.join([char for char in s if char not in c])
    return (s,s[::-1] == s)


# Generated test cases:
import pytest

@pytest.mark.parametrize("input_str, chars_to_remove, expected", [
    ("hello", "l", ("heo", False)),
    ("radar", "d", ("raar", True)),
    ("", "", ("", True)),
    ("abcba", "ac", ("bb", True)),
    ("python", "p", ("ython", False)),
    ("   ", " ", ("", True)),
    ("aaa", "a", ("", True)),
    ("12321", "2", ("131", True)),
    ("test!!test", "!", ("testtest", False)),
    ("abc123", "123", ("abc", False)),
    ("$#@$#@", "@#", ("$$", True)),
    ("Hello World", " ", ("HelloWorld", False)),
    ("αβγαβ", "β", ("αγα", True)),
    ("abcdef", "xyz", ("abcdef", False)),
    ("", "abc", ("", True)),
    ("mississippi", "si", ("mpp", False))
])
def test_reverse_delete(input_str, chars_to_remove, expected):
    assert reverse_delete(input_str, chars_to_remove) == expected

@pytest.mark.parametrize("input_str, chars_to_remove", [
    (None, "abc"),
    ("abc", None),
    (123, "abc"),
    ("abc", 123),
    (True, "abc"),
    ("abc", True)
])
def test_reverse_delete_invalid_inputs(input_str, chars_to_remove):
    with pytest.raises((TypeError, AttributeError)):
        reverse_delete(input_str, chars_to_remove)

def test_reverse_delete_empty_inputs():
    assert reverse_delete("", "") == ("", True)
    assert reverse_delete(" ", "") == (" ", True)

def test_reverse_delete_special_characters():
    assert reverse_delete("!@#$%^", "#%") == ("!@$^", False)
    assert reverse_delete("\n\t\r", "\n") == ("\t\r", False)
    assert reverse_delete("\\\\", "\\") == ("", True)
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

def test_basic_palindrome():
    assert reverse_delete("abcdedcba", "ab") == ("cdedc", True)

def test_non_palindrome():
    assert reverse_delete("abcde", "ae") == ("bcd", False)

def test_single_char_removal():
    assert reverse_delete("abcdef", "b") == ("acdef", False)

@pytest.mark.parametrize("s,c,expected", [
    ("", "", ("", True)),
    ("a", "a", ("", True)),
    ("abc", "", ("abc", False)),
    ("racecar", "e", ("raccar", True)),
    ("hello", "l", ("heo", False)),
    ("aaa", "a", ("", True)),
    ("abcba", "ac", ("bb", True)),
    ("12321", "2", ("131", True)),
    ("python", "python", ("", True)),
    ("   ", " ", ("", True)),
    ("a b c", " ", ("abc", False)),
    ("!@#$%", "#%", ("!@$", False)),
    ("aabbcc", "ac", ("bb", True)),
    ("xyzzyx", "xyz", ("", True)),
])
def test_multiple_cases(s, c, expected):
    assert reverse_delete(s, c) == expected

def test_special_characters():
    assert reverse_delete("a!b@c#", "!@#") == ("abc", False)

def test_numbers_and_letters():
    assert reverse_delete("a1b2c1a", "123") == ("abca", False)

def test_case_sensitivity():
    assert reverse_delete("AbCdE", "ac") == ("AbCdE", False)
    assert reverse_delete("AbCdE", "AC") == ("bdE", False)

def test_unicode_characters():
    assert reverse_delete("αβγβα", "γ") == ("αββα", True)

def test_repeated_characters():
    assert reverse_delete("aabbccbbaa", "ac") == ("bbbb", True)

def test_all_same_characters():
    assert reverse_delete("aaaaa", "a") == ("", True)

def test_no_matches():
    assert reverse_delete("abcde", "xyz") == ("abcde", False)
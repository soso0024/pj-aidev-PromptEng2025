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

def test_reverse_delete_basic_case():
    assert reverse_delete("abcde", "bc") == ("ade", False)

def test_reverse_delete_palindrome():
    assert reverse_delete("racecar", "x") == ("racecar", True)

def test_reverse_delete_empty_string():
    assert reverse_delete("", "abc") == ("", True)

def test_reverse_delete_remove_all_chars():
    assert reverse_delete("hello", "helo") == ("", True)

def test_reverse_delete_remove_no_chars():
    assert reverse_delete("python", "xyz") == ("python", False)

@pytest.mark.parametrize("s,c,expected", [
    ("abcde", "bc", ("ade", False)),
    ("racecar", "x", ("racecar", True)),
    ("", "abc", ("", True)),
    ("hello", "helo", ("", True)),
    ("python", "xyz", ("python", False)),
    ("aabbaa", "ab", ("", True)),
    ("programming", "pro", ("gramming", False))
])
def test_reverse_delete_parametrized(s, c, expected):
    assert reverse_delete(s, c) == expected

def test_reverse_delete_case_sensitive():
    assert reverse_delete("AbCdE", "ac") == ("AbCdE", False)

def test_reverse_delete_unicode_chars():
    assert reverse_delete("héllö", "é") == ("hllö", False)
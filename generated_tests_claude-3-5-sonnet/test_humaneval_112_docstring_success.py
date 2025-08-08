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

@pytest.mark.parametrize("s, c, expected", [
    ("abcde", "ae", ("bcd", False)),
    ("abcdef", "b", ("acdef", False)),
    ("abcdedcba", "ab", ("cdedc", True)),
    ("", "", ("", True)),
    ("hello", "", ("hello", False)),
    ("", "abc", ("", True)),
    ("racecar", "e", ("raccar", True)),
    ("python", "python", ("", True)),
    ("aaa", "b", ("aaa", True)),
    ("abcba", "ac", ("bb", True)),
    ("xyz", "xyz", ("", True)),
    ("12321", "2", ("131", True)),
    ("!@#@!", "#", ("!@@!", True)),
    ("abcdef", "xyz", ("abcdef", False)),
    ("    ", " ", ("", True)),
])
def test_reverse_delete(s, c, expected):
    assert reverse_delete(s, c) == expected

def test_reverse_delete_with_special_chars():
    assert reverse_delete("a!b@c#", "!@#") == ("abc", False)
    assert reverse_delete("a\nb\nc", "\n") == ("abc", False)
    assert reverse_delete("a\tb\tc", "\t") == ("abc", False)

def test_reverse_delete_with_numbers():
    assert reverse_delete("123321", "2") == ("1331", True)
    assert reverse_delete("12345", "123") == ("45", False)

def test_reverse_delete_case_sensitive():
    assert reverse_delete("AbCdE", "ae") == ("AbCdE", False)
    assert reverse_delete("AbCdE", "AE") == ("bCd", False)

def test_reverse_delete_unicode():
    assert reverse_delete("αβγγβα", "β") == ("αγγα", True)
    assert reverse_delete("Hello世界", "世") == ("Hello界", False)
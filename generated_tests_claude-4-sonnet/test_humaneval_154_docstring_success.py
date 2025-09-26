# Test cases for HumanEval/154
# Generated using Claude API


def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    l = len(b)
    pat = b + b
    for i in range(len(a) - l + 1):
        for j in range(l + 1):
            if a[i:i+l] == pat[j:j+l]:
                return True
    return False


# Generated test cases:
import pytest

def cycpattern_check(a , b):
    l = len(b)
    pat = b + b
    for i in range(len(a) - l + 1):
        for j in range(l + 1):
            if a[i:i+l] == pat[j:j+l]:
                return True
    return False

@pytest.mark.parametrize("a,b,expected", [
    ("abcd", "abd", False),
    ("hello", "ell", True),
    ("whassup", "psus", False),
    ("abab", "baa", True),
    ("efef", "eeff", False),
    ("himenss", "simen", True),
    ("", "", True),
    ("abc", "", True),
    ("", "abc", False),
    ("a", "a", True),
    ("ab", "ba", True),
    ("abc", "bca", True),
    ("abc", "cab", True),
    ("abc", "abc", True),
    ("abcdef", "def", True),
    ("abcdef", "fed", False),
    ("abcdef", "cde", True),
    ("abcdef", "edc", False),
    ("programming", "gram", True),
    ("programming", "marg", False),
    ("programming", "argm", False),
    ("test", "sets", False),
    ("rotation", "tionro", False),
    ("rotation", "onrota", False),
    ("rotation", "ationr", False),
    ("single", "elgnis", False),
    ("aaa", "aa", True),
    ("aaa", "aaa", True),
    ("abcabc", "cab", True),
    ("abcabc", "bca", True),
    ("xyz", "zyx", False),
    ("abcdefg", "xyz", False),
    ("longstring", "short", False),
    ("short", "longstring", False),
    ("abcdefghijklmnop", "nopabcd", False),
    ("circular", "larc", False),
    ("circular", "rcul", True),
    ("banana", "ana", True),
    ("banana", "nan", True),
    ("banana", "nab", False)
])
def test_cycpattern_check(a, b, expected):
    assert cycpattern_check(a, b) == expected

def test_cycpattern_check_empty_strings():
    assert cycpattern_check("", "") == True
    assert cycpattern_check("nonempty", "") == True
    assert cycpattern_check("", "nonempty") == False

def test_cycpattern_check_single_character():
    assert cycpattern_check("a", "a") == True
    assert cycpattern_check("a", "b") == False
    assert cycpattern_check("ab", "a") == True
    assert cycpattern_check("ab", "b") == True

def test_cycpattern_check_same_length():
    assert cycpattern_check("abc", "abc") == True
    assert cycpattern_check("abc", "bca") == True
    assert cycpattern_check("abc", "cab") == True
    assert cycpattern_check("abc", "acb") == False
    assert cycpattern_check("abc", "bac") == False
    assert cycpattern_check("abc", "cba") == False

def test_cycpattern_check_longer_pattern():
    assert cycpattern_check("short", "verylongpattern") == False
    assert cycpattern_check("a", "ab") == False
    assert cycpattern_check("ab", "abc") == False
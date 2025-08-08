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

def test_cycpattern_check_basic():
    assert cycpattern_check("abcd", "abc") == True
    assert cycpattern_check("hello", "ell") == True
    assert cycpattern_check("whassup", "psus") == False

@pytest.mark.parametrize("a, b, expected", [
    ("abcd", "abd", False),
    ("hello", "ell", True),
    ("whassup", "psus", False),
    ("abab", "baa", True),
    ("efef", "eeff", False),
    ("himenss", "simen", True),
    ("", "", True),
    ("abc", "", True),
    ("", "abc", False),
    ("abcde", "cde", True),
    ("abcde", "edc", False),
    ("aaa", "aa", True),
    ("aaaa", "aaa", True),
    ("test", "test", True),
    ("test", "tset", False),
    ("python", "thon", True),
    ("python", "pyth", True),
    ("short", "longer", False),
    ("repeated", "pete", False),
    ("single", "s", True)
])
def test_cycpattern_check_parametrized(a, b, expected):
    assert cycpattern_check(a, b) == expected

def test_cycpattern_check_case_sensitive():
    assert cycpattern_check("Hello", "hello") == False
    assert cycpattern_check("Python", "python") == False

def test_cycpattern_check_special_chars():
    assert cycpattern_check("!@#$", "#$!@") == True
    assert cycpattern_check("12345", "234") == True
    assert cycpattern_check("a b c", "b c") == True

def test_cycpattern_check_single_char():
    assert cycpattern_check("a", "a") == True
    assert cycpattern_check("a", "b") == False

def test_cycpattern_check_identical_strings():
    assert cycpattern_check("test", "test") == True
    assert cycpattern_check("", "") == True

def test_cycpattern_check_longer_pattern():
    assert cycpattern_check("short", "shorter") == False
    assert cycpattern_check("abc", "abcd") == False
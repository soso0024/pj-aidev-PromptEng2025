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
    assert cycpattern_check("abcde", "cde") == True
    assert cycpattern_check("hello", "ell") == True
    assert cycpattern_check("python", "thon") == True

def test_cycpattern_check_full_string():
    assert cycpattern_check("hello", "hello") == True
    assert cycpattern_check("test", "test") == True

def test_cycpattern_check_no_match():
    assert cycpattern_check("hello", "world") == False
    assert cycpattern_check("python", "java") == False

def test_cycpattern_check_empty():
    assert cycpattern_check("", "") == True
    assert cycpattern_check("hello", "") == True
    assert cycpattern_check("", "test") == False

@pytest.mark.parametrize("string,pattern,expected", [
    ("hello world", "world", True),
    ("programming", "gram", True),
    ("testing", "xyz", False),
    ("abcdef", "def", True),
    ("python3", "hon3", True),
    ("short", "longer", False),
    ("test", "t", True),
    ("single", "le", True)
])
def test_cycpattern_check_parametrized(string, pattern, expected):
    assert cycpattern_check(string, pattern) == expected

def test_cycpattern_check_case_sensitive():
    assert cycpattern_check("Hello", "hello") == False
    assert cycpattern_check("Python", "python") == False

def test_cycpattern_check_special_chars():
    assert cycpattern_check("test!@#", "!@#") == True
    assert cycpattern_check("123456", "345") == True
    assert cycpattern_check("@#$%^&", "#$%") == True

def test_cycpattern_check_repeated_chars():
    assert cycpattern_check("aaaa", "aa") == True
    assert cycpattern_check("abababab", "abab") == True

def test_cycpattern_check_single_char():
    assert cycpattern_check("a", "a") == True
    assert cycpattern_check("abc", "b") == True

def test_cycpattern_check_spaces():
    assert cycpattern_check("hello world", " ") == True
    assert cycpattern_check("  test  ", "  ") == True
    assert cycpattern_check("a b c", " b ") == True

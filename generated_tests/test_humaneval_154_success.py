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

def test_cycpattern_check_negative():
    assert cycpattern_check("hello", "xyz") == False
    assert cycpattern_check("python", "java") == False

def test_cycpattern_check_empty():
    assert cycpattern_check("", "") == True
    assert cycpattern_check("abc", "") == True
    assert cycpattern_check("", "abc") == False

def test_cycpattern_check_same_length():
    assert cycpattern_check("hello", "hello") == True
    assert cycpattern_check("hello", "elloh") == True
    assert cycpattern_check("hello", "world") == False

@pytest.mark.parametrize("a,b,expected", [
    ("abcde", "cde", True),
    ("hello", "llo", True),
    ("python", "hon", True),
    ("test", "xyz", False),
    ("programming", "ming", True),
    ("short", "longer", False),
    ("", "", True),
    ("abc", "", True),
    ("", "x", False),
    ("hello", "hello", True),
    ("hello", "elloh", True),
    ("aaa", "aa", True),
    ("abcdef", "def", True),
    ("test", "est", True),
    ("circular", "ular", True),
    ("python", "py", True),
    ("testing", "xyz", False),
    ("sample", "mple", True)
])
def test_cycpattern_check_parametrized(a, b, expected):
    assert cycpattern_check(a, b) == expected

def test_cycpattern_check_single_char():
    assert cycpattern_check("a", "a") == True
    assert cycpattern_check("abc", "a") == True
    assert cycpattern_check("abc", "b") == True
    assert cycpattern_check("abc", "c") == True
    assert cycpattern_check("abc", "d") == False

def test_cycpattern_check_repeated_chars():
    assert cycpattern_check("aaaa", "aa") == True
    assert cycpattern_check("aaaaaa", "aaa") == True
    assert cycpattern_check("abababab", "abab") == True

def test_cycpattern_check_case_sensitive():
    assert cycpattern_check("Hello", "hello") == False
    assert cycpattern_check("Python", "python") == False
    assert cycpattern_check("TEST", "test") == False
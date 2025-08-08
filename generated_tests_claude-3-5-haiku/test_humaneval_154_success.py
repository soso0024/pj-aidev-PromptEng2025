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

def cycpattern_check(a, b):
    if not b:
        return False
    l = len(b)
    pat = b + b
    for i in range(len(a) - l + 1):
        for j in range(l + 1):
            if a[i:i+l] == pat[j:j+l]:
                return True
    return False

def test_cycpattern_check_basic_match():
    assert cycpattern_check("abcde", "bcd") == True
    assert cycpattern_check("abcde", "cde") == True

def test_cycpattern_check_no_match():
    assert cycpattern_check("abcde", "xyz") == False
    assert cycpattern_check("hello", "world") == False

def test_cycpattern_check_edge_cases():
    assert cycpattern_check("", "") == False
    assert cycpattern_check("a", "a") == True
    assert cycpattern_check("abc", "") == False

def test_cycpattern_check_full_match():
    assert cycpattern_check("abcabc", "abc") == True
    assert cycpattern_check("xyxyxy", "xy") == True

def test_cycpattern_check_partial_match():
    assert cycpattern_check("abcdefg", "def") == True
    assert cycpattern_check("abcdefg", "efg") == True

@pytest.mark.parametrize("a,b,expected", [
    ("abcde", "bcd", True),
    ("hello", "lo", True),
    ("python", "thon", True),
    ("programming", "gram", True),
    ("abcde", "xyz", False),
    ("", "", False),
    ("a", "a", True),
    ("abcabc", "abc", True),
    ("xyxyxy", "xy", True)
])
def test_cycpattern_check_parametrized(a, b, expected):
    assert cycpattern_check(a, b) == expected
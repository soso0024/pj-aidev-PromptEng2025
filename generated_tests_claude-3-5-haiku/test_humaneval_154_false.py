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
    if not a or not b:
        return False
    l = len(b)
    pat = b + b
    for i in range(len(a) - l + 1):
        for j in range(l + 1):
            if a[i:i+l] == pat[j:j+l]:
                return True
    return False

def test_cycpattern_check_basic_match():
    assert cycpattern_check("helloworld", "lowo") == True

def test_cycpattern_check_no_match():
    assert cycpattern_check("helloworld", "xyz") == False

def test_cycpattern_check_exact_match():
    assert cycpattern_check("hello", "hello") == True

def test_cycpattern_check_empty_strings():
    assert cycpattern_check("", "") == False

def test_cycpattern_check_pattern_longer_than_string():
    assert cycpattern_check("abc", "abcd") == False

@pytest.mark.parametrize("a,b,expected", [
    ("abcde", "cde", True),
    ("abcde", "eab", True),
    ("abcde", "bcd", True),
    ("abcde", "def", False),
    ("hello", "ell", True),
    ("hello", "loh", True),
    ("", "a", False),
    ("a", "", False)
])
def test_cycpattern_check_parametrized(a, b, expected):
    assert cycpattern_check(a, b) == expected

def test_cycpattern_check_case_sensitive():
    assert cycpattern_check("Hello", "llo") == True
    assert cycpattern_check("Hello", "LLO") == False

def test_cycpattern_check_single_character():
    assert cycpattern_check("abcde", "c") == True
    assert cycpattern_check("abcde", "x") == False
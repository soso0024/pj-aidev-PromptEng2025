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
    l = len(b)
    pat = b + b
    for i in range(len(a) - l + 1):
        if a[i:i+l] in pat:
            return True
    return False

def test_cycpattern_check_empty_a():
    assert cycpattern_check("", "abc") is False

def test_cycpattern_check_empty_b():
    assert cycpattern_check("abc", "") is False

def test_cycpattern_check_single_char_a_b():
    assert cycpattern_check("a", "a") is True
    assert cycpattern_check("a", "b") is False

@pytest.mark.parametrize("a,b,expected", [
    ("abcabc", "abc", True),
    ("abcabcabc", "abc", True),
    ("abcabcdef", "abc", True),
    ("abcdef", "abc", False),
    ("abcabcabc", "ab", True),
    ("abcabcabc", "bc", True),
    ("abcabcabc", "abcabc", True),
    ("abcabcabc", "abcabcabc", True),
    ("abcabcabc", "abcabcd", False),
    ("abcabcabc", "abcabcab", False),
])
def test_cycpattern_check_various_inputs(a, b, expected):
    assert cycpattern_check(a, b) is expected

def test_cycpattern_check_long_inputs():
    a = "a" * 10000
    b = "abc"
    assert cycpattern_check(a, b) is True

    a = "a" * 10000
    b = "def"
    assert cycpattern_check(a, b) is False
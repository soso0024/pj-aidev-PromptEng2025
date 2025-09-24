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
    ("abcabcabc", "abc", True),
    ("hello", "ell", True),
    ("abcdef", "def", True),
    ("abcdef", "fed", False),
    ("abcdef", "xyz", False),
    ("", "abc", False),
    ("abc", "", True),
    ("", "", True),
    ("a", "a", True),
    ("ab", "ba", True),
    ("abc", "bca", True),
    ("abc", "cab", True),
    ("abc", "acb", False),
    ("abcd", "cdab", True),
    ("abcd", "bcda", True),
    ("abcd", "dabc", True),
    ("hello world", "world", True),
    ("hello world", "dlrow", False),
    ("programming", "gram", True),
    ("programming", "ming", True),
    ("programming", "prog", True),
    ("programming", "garp", False),
    ("abcdefg", "efgabc", False),
    ("abcdefg", "defgab", False),
    ("abcdefg", "cdefga", False),
    ("test", "testtest", False),
    ("short", "verylongstring", False),
    ("aaa", "aa", True),
    ("aaa", "aaa", True),
    ("abab", "ab", True),
    ("abab", "ba", True),
    ("abcabc", "bca", True),
    ("xyzxyz", "zxy", True),
    ("single", "elgnis", False),
    ("racecar", "car", True),
    ("racecar", "ace", True),
    ("racecar", "era", False)
])
def test_cycpattern_check_parametrized(a, b, expected):
    assert cycpattern_check(a, b) == expected

def test_cycpattern_check_empty_strings():
    assert cycpattern_check("", "") == True
    assert cycpattern_check("nonempty", "") == True
    assert cycpattern_check("", "nonempty") == False

def test_cycpattern_check_single_character():
    assert cycpattern_check("a", "a") == True
    assert cycpattern_check("a", "b") == False
    assert cycpattern_check("ab", "a") == True
    assert cycpattern_check("ba", "a") == True

def test_cycpattern_check_same_length():
    assert cycpattern_check("abc", "abc") == True
    assert cycpattern_check("abc", "bca") == True
    assert cycpattern_check("abc", "cab") == True
    assert cycpattern_check("abc", "acb") == False
    assert cycpattern_check("abc", "xyz") == False

def test_cycpattern_check_pattern_longer():
    assert cycpattern_check("ab", "abc") == False
    assert cycpattern_check("x", "xyz") == False
    assert cycpattern_check("short", "muchlongerpattern") == False

def test_cycpattern_check_repeated_patterns():
    assert cycpattern_check("ababab", "ab") == True
    assert cycpattern_check("ababab", "ba") == True
    assert cycpattern_check("abcabcabc", "abc") == True
    assert cycpattern_check("abcabcabc", "bca") == True
    assert cycpattern_check("abcabcabc", "cab") == True

def test_cycpattern_check_no_match():
    assert cycpattern_check("abcdef", "xyz") == False
    assert cycpattern_check("hello", "world") == False
    assert cycpattern_check("test", "exam") == False
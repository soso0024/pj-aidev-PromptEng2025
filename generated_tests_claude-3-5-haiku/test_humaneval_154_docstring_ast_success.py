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
        return True
    if len(b) > len(a):
        return False
    
    l = len(b)
    pat = b + b
    for i in range(len(a) - l + 1):
        for j in range(l + 1):
            if a[i:i+l].lower() == pat[j:j+l].lower():
                return True
    return False

def test_cycpattern_check_normal_cases():
    assert cycpattern_check("hello", "ell") == True
    assert cycpattern_check("abcd", "abd") == False
    assert cycpattern_check("whassup", "psus") == False
    assert cycpattern_check("abab", "baa") == True
    assert cycpattern_check("efef", "eeff") == False
    assert cycpattern_check("himenss", "simen") == True

@pytest.mark.parametrize("a,b,expected", [
    ("hello", "ell", True),
    ("abcd", "abd", False),
    ("whassup", "psus", False),
    ("abab", "baa", True),
    ("efef", "eeff", False),
    ("himenss", "simen", True),
    ("", "", True),
    ("abc", "", True),
    ("", "abc", False)
])
def test_cycpattern_check_parametrized(a, b, expected):
    assert cycpattern_check(a, b) == expected

def test_cycpattern_check_edge_cases():
    assert cycpattern_check("a", "a") == True
    assert cycpattern_check("ab", "ba") == True
    assert cycpattern_check("abc", "cab") == True
    assert cycpattern_check("longstring", "short") == False

def test_cycpattern_check_case_sensitive():
    assert cycpattern_check("Hello", "ell") == True
    assert cycpattern_check("hello", "Ell") == True
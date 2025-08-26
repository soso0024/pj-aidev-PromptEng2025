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

def test_cycpattern_check_empty_a():
    assert cycpattern_check("", "abc") == False

def test_cycpattern_check_empty_b():
    assert cycpattern_check("abc", "") == False

@pytest.mark.parametrize("a,b,expected", [
    ("abcabc", "abc", True),
    ("abcabcabc", "abc", True),
    ("abcdef", "abc", False),
    ("abcabcdef", "abc", True),
    ("abcabcabc", "abcabc", True),
    ("abcabcabc", "abcabcd", False),
    ("a", "a", True),
    ("aa", "a", True),
    ("aaa", "aa", True)
])
def test_cycpattern_check_normal_cases(a, b, expected):
    assert cycpattern_check(a, b) == expected

def test_cycpattern_check_type_error():
    with pytest.raises(TypeError):
        cycpattern_check(123, "abc")
    with pytest.raises(TypeError):
        cycpattern_check("abc", 123)

def cycpattern_check(a, b):
    l = len(b)
    pat = b + b
    for i in range(len(a) - l + 1):
        if a[i:i+l] in pat:
            return True
    return False
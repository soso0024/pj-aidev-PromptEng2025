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

@pytest.mark.parametrize("a, b, expected", [
    ("abab", "ab", True),
    ("abcabcabc", "abc", True),
    ("ababab", "ab", True),
    ("abcdef", "abc", False),
    ("", "", True),
    ("a", "a", True),
    ("a", "b", False),
    ("abc", "", False),
    ("123", "abc", TypeError),
    (["a", "b"], "ab", TypeError)
])
def test_cycpattern_check(a, b, expected):
    if isinstance(a, (int, list)):
        with pytest.raises(TypeError):
            cycpattern_check(a, b)
    else:
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                cycpattern_check(a, b)
        else:
            assert cycpattern_check(a, b) == expected

def cycpattern_check(a, b):
    l = len(b)
    pat = b + b
    for i in range(len(a) - l + 1):
        if a[i:i+l] in pat:
            return True
    return False
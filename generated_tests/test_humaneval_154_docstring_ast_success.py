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
])
def test_cycpattern_check_parametrized(a, b, expected):
    assert cycpattern_check(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    ("", "", True),
    ("a", "", True),
    ("", "a", False),
    ("a", "a", True),
    ("aa", "a", True),
    ("abc", "cba", False),
])
def test_cycpattern_check_edge_cases(a, b, expected):
    assert cycpattern_check(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    ("hello world", "world", True),
    ("python programming", "gram", True),
    ("aaaaaa", "aaa", True),
    ("abcdef", "def", True),
    ("testing", "xyz", False),
    ("rotations", "tation", True),
])
def test_cycpattern_check_longer_strings(a, b, expected):
    assert cycpattern_check(a, b) == expected

def test_cycpattern_check_case_sensitivity():
    assert cycpattern_check("Hello", "hello") == False
    assert cycpattern_check("Python", "python") == False
    assert cycpattern_check("TEST", "test") == False

@pytest.mark.parametrize("a, b, expected", [
    ("12345", "123", True),
    ("12345", "345", True),
    ("12345", "451", False),
    ("11111", "11", True),
])
def test_cycpattern_check_numbers_as_strings(a, b, expected):
    assert cycpattern_check(a, b) == expected

def test_cycpattern_check_special_characters():
    assert cycpattern_check("!@#$%", "@#$") == True
    assert cycpattern_check("***---", "**-") == True
    assert cycpattern_check("!@#$%", "!%@") == False

@pytest.mark.parametrize("a, b", [
    (None, "test"),
    ("test", None),
    (123, "test"),
    ("test", 123),
])
def test_cycpattern_check_invalid_inputs(a, b):
    with pytest.raises((AttributeError, TypeError)):
        cycpattern_check(a, b)

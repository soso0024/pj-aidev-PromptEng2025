# Test cases for HumanEval/80
# Generated using Claude API


def is_happy(s):
    """You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
    For example:
    is_happy(a) => False
    is_happy(aa) => False
    is_happy(abcd) => True
    is_happy(aabb) => False
    is_happy(adb) => True
    is_happy(xyy) => False
    """

    if len(s) < 3:
      return False

    for i in range(len(s) - 2):
      
      if s[i] == s[i+1] or s[i+1] == s[i+2] or s[i] == s[i+2]:
        return False
    return True


# Generated test cases:
import pytest

def test_empty_string():
    assert not is_happy("")
    
def test_single_char():
    assert not is_happy("a")
    
def test_two_chars():
    assert not is_happy("ab")

@pytest.mark.parametrize("input_str,expected", [
    ("abc", True),
    ("abca", True),
    ("abcb", True),
    ("abbc", False),
    ("aabc", False),
    ("abcc", False),
    ("abac", False),
    ("xyz", True),
    ("xyza", True),
    ("xyzx", True),
    ("aaa", False),
    ("abcdef", True),
    ("abcdea", True),
    ("abcabc", True)
])
def test_happy_strings(input_str, expected):
    assert is_happy(input_str) == expected

@pytest.mark.parametrize("input_str", [
    "123",
    "456",
    "789",
    "147"
])
def test_numeric_strings(input_str):
    assert is_happy(input_str)

@pytest.mark.parametrize("input_str", [
    "112",
    "122",
    "121",
    "111"
])
def test_unhappy_numeric_strings(input_str):
    assert not is_happy(input_str)

def test_special_characters():
    assert is_happy("!@#")
    assert is_happy("$%^")
    assert not is_happy("!!@")
    assert not is_happy("!@@")

def test_mixed_characters():
    assert is_happy("a1b")
    assert is_happy("1a2")
    assert not is_happy("a1a")
    assert not is_happy("1aa")

def test_spaces():
    assert is_happy("a b")
    assert not is_happy("a a")
    assert not is_happy("  a")
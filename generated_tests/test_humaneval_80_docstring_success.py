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

@pytest.mark.parametrize("input_str,expected", [
    ("a", False),
    ("aa", False),
    ("aaa", False),
    ("abcd", True),
    ("aabb", False),
    ("adb", True),
    ("xyy", False),
    ("xyz", True),
    ("", False),
    ("ab", False),
    ("aba", False),
    ("abc", True),
    ("abcde", True),
    ("aabcc", False),
    ("aabbcc", False),
    ("abcabc", True),
    ("   ", False),
    ("123", True),
    ("112", False),
    ("1122", False)
])
def test_is_happy(input_str, expected):
    assert is_happy(input_str) == expected

def test_is_happy_with_none():
    with pytest.raises(TypeError):
        is_happy(None)

def test_is_happy_with_non_string():
    with pytest.raises(TypeError):
        is_happy(123)

def test_is_happy_with_special_chars():
    assert is_happy("!@#") == True
    assert is_happy("!@@") == False

def test_is_happy_with_mixed_chars():
    assert is_happy("a1b") == True
    assert is_happy("a11") == False

def test_is_happy_with_spaces():
    assert is_happy("abc") == True
    assert is_happy("a b") == True

def test_is_happy_with_unicode():
    assert is_happy("αβγ") == True
    assert is_happy("ααβ") == False
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

def is_happy(s):
    if len(s) < 3:
      return False

    for i in range(len(s) - 2):
      
      if s[i] == s[i+1] or s[i+1] == s[i+2] or s[i] == s[i+2]:
        return False
    return True

@pytest.mark.parametrize("input_str,expected", [
    ("", False),
    ("a", False),
    ("ab", False),
    ("abc", True),
    ("abcd", True),
    ("abcde", True),
    ("aab", False),
    ("abb", False),
    ("aba", False),
    ("aaa", False),
    ("abcc", False),
    ("abbc", False),
    ("abac", False),
    ("abcabc", True),
    ("abcdef", True),
    ("abcaab", False),
    ("abcabb", False),
    ("abcaba", False),
    ("xyz", True),
    ("xyza", True),
    ("xyzx", True),
    ("xyzy", False),
    ("xyzz", False),
    ("xxyz", False),
    ("xyyz", False),
    ("xxyy", False),
    ("123", True),
    ("1234", True),
    ("1123", False),
    ("1223", False),
    ("1213", False),
    ("abcdefghijk", True),
    ("abcdefghijka", True),
    ("abcdefghijkk", False),
    ("abcdefghijkj", False),
    ("abcdefghijki", True)
])
def test_is_happy(input_str, expected):
    assert is_happy(input_str) == expected

def test_is_happy_empty_string():
    assert is_happy("") == False

def test_is_happy_single_char():
    assert is_happy("x") == False

def test_is_happy_two_chars():
    assert is_happy("xy") == False

def test_is_happy_three_chars_all_different():
    assert is_happy("xyz") == True

def test_is_happy_three_chars_adjacent_same():
    assert is_happy("xxy") == False
    assert is_happy("xyy") == False

def test_is_happy_three_chars_first_third_same():
    assert is_happy("xyx") == False

def test_is_happy_three_chars_all_same():
    assert is_happy("xxx") == False

def test_is_happy_long_valid_string():
    assert is_happy("abcdefghijklmnopqrstuvw") == True

def test_is_happy_long_invalid_string_adjacent():
    assert is_happy("abcdefghijklmnopqrstuvww") == False

def test_is_happy_long_invalid_string_gap():
    assert is_happy("abcdefghijklmnopqrstuvwa") == True
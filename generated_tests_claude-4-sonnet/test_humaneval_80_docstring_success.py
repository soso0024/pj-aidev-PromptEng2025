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

@pytest.mark.parametrize("input_string,expected", [
    ("a", False),
    ("aa", False),
    ("abcd", True),
    ("aabb", False),
    ("adb", True),
    ("xyy", False),
    ("", False),
    ("ab", False),
    ("abc", True),
    ("aaa", False),
    ("aba", False),
    ("bab", False),
    ("abcdef", True),
    ("abcabc", True),
    ("abccba", False),
    ("abcdefg", True),
    ("xyzxyz", True),
    ("aabbcc", False),
    ("abcaab", False),
    ("abcbca", False),
    ("abcdefghijk", True),
    ("abcdefghijka", True),
    ("abcdefghijaa", False),
    ("xyz", True),
    ("xyx", False),
    ("yxy", False),
    ("zyx", True),
    ("abcdefghijklmnop", True),
    ("abcdefghijklmnoo", False),
    ("abcdefghijklmoop", False),
])
def test_is_happy(input_string, expected):
    assert is_happy(input_string) == expected

def test_is_happy_empty_string():
    assert is_happy("") == False

def test_is_happy_single_char():
    assert is_happy("x") == False

def test_is_happy_two_chars():
    assert is_happy("xy") == False
    assert is_happy("xx") == False

def test_is_happy_three_chars_all_different():
    assert is_happy("abc") == True
    assert is_happy("xyz") == True

def test_is_happy_three_chars_with_duplicates():
    assert is_happy("aab") == False
    assert is_happy("abb") == False
    assert is_happy("aba") == False
    assert is_happy("aaa") == False

def test_is_happy_long_strings():
    assert is_happy("abcdefghijklmnopqrstuvwxyz") == True
    assert is_happy("abcdefghijklmnopqrstuvwxyza") == True

def test_is_happy_repeating_patterns():
    assert is_happy("abcabc") == True
    assert is_happy("abcabcabc") == True
    assert is_happy("abcabcabca") == True

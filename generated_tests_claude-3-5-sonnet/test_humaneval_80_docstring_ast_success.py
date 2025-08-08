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

@pytest.mark.parametrize("input_str, expected", [
    ("abc", True),
    ("abcd", True),
    ("adb", True),
    ("xyy", False),
    ("aabb", False),
    ("abcde", True),
    ("aabbc", False),
    ("abcabc", True),
    ("aaa", False),
    ("aba", False),
    ("xyz", True),
    ("aabc", False),
    ("abcc", False),
    ("abcdefg", True),
    ("aabbcc", False),
])
def test_happy_strings(input_str, expected):
    assert is_happy(input_str) == expected

@pytest.mark.parametrize("input_str", [
    "123",
    "!@#",
    "a1b",
    "   ",
])
def test_non_letter_strings(input_str):
    result = is_happy(input_str)
    assert isinstance(result, bool)

def test_special_chars():
    assert is_happy("!@#") == True

def test_mixed_case():
    assert is_happy("AbC") == True
    assert is_happy("aAa") == False

def test_numbers():
    assert is_happy("123") == True
    assert is_happy("111") == False

def test_spaces():
    assert is_happy("abc") == True
    assert is_happy("a  a") == False

def test_long_string():
    assert is_happy("abcdefghijklmnop") == True
    assert is_happy("abcdefaghijklmnop") == True

def test_repeating_pattern():
    assert is_happy("abcabc") == True
    assert is_happy("aabbcc") == False
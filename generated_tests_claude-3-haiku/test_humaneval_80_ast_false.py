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

@pytest.mark.parametrize("input,expected", [
    ("abc", True),
    ("aa", False),
    ("aba", False),
    ("abab", False),
    ("", False),
    ("a", False),
    ("ab", False),
    ("abcabc", True),
    ("abcabcabc", True),
    ("abcabcabcabc", True),
    ("abcabcabcabcab", True),
    ("abcabcabcabca", True),
    ("abcabcabcabc", True),
    ("abcabcabcabc ", False),
    (" abcabcabcabc", False),
    ("abc abc abc", True),
    ("abc abc abc ", False),
    (" abc abc abc", False),
    ("123456", True),
    ("123456789", True),
    ("12345678901", False),
    ("1234567890123", True),
    ("12345678901234", False),
    ("abcdefghijklmnopqrstuvwxyz", True),
    ("abcdefghijklmnopqrstuvwxyz ", False),
    (" abcdefghijklmnopqrstuvwxyz", False)
])
def test_is_happy(input, expected):
    assert is_happy(input) == expected
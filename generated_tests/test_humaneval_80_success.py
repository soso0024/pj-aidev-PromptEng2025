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

def test_is_happy_empty_string():
    assert not is_happy("")

def test_is_happy_single_char():
    assert not is_happy("a")

def test_is_happy_two_chars():
    assert not is_happy("ab")

@pytest.mark.parametrize("input_str,expected", [
    ("abc", True),
    ("abca", True),
    ("abcb", False),
    ("aaa", False),
    ("aba", False),
    ("abba", False),
    ("abbc", False),
    ("abac", False),
    ("abcde", True),
    ("zabcd", True),
    ("azbcd", True),
    ("aaabc", False),
    ("abccc", False),
    ("abcabc", True),
    ("xyzxyz", True),
    ("aabbcc", False),
    ("123123", True),
    ("112233", False),
    ("abcdef", True),
    ("aabbccdd", False)
])
def test_is_happy_parametrized(input_str, expected):
    assert is_happy(input_str) == expected

def test_is_happy_special_chars():
    assert is_happy("!@#")
    assert not is_happy("!!@")

def test_is_happy_numbers():
    assert is_happy("123")
    assert not is_happy("112")

def test_is_happy_mixed():
    assert is_happy("1a2")
    assert not is_happy("1aa")

def test_is_happy_spaces():
    assert is_happy("a b")
    assert not is_happy("a a")

def test_is_happy_case_sensitive():
    assert is_happy("aBC")
    assert is_happy("AbC")
    assert not is_happy("ABB")

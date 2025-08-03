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
    ("abc", True),
    ("aba", False),
    ("abca", True),
    ("abbc", False),
    ("abab", False),
    ("", False),
    ("a", False),
    ("ab", False),
    ("aaa", False),
    ("abcde", True),
    ("abbcde", False),
    ("abcabc", True),
    ("aabbcc", False),
    ("abcdef", True),
    ("xyzzyx", False),
    ("aabbccdd", False),
    ("abcabcabc", True),
    ("   ", False),
    ("123", True),
    ("121", False)
])
def test_is_happy_parametrized(input_str, expected):
    assert is_happy(input_str) == expected

def test_is_happy_none():
    with pytest.raises(TypeError):
        is_happy(None)

def test_is_happy_non_string():
    with pytest.raises(TypeError):
        is_happy(123)

def test_is_happy_empty_string():
    assert is_happy("") == False

def test_is_happy_single_char():
    assert is_happy("a") == False

def test_is_happy_two_chars():
    assert is_happy("ab") == False

def test_is_happy_special_chars():
    assert is_happy("!@#") == True
    assert is_happy("!@@") == False

def test_is_happy_spaces():
    assert is_happy("a b c") == True
    assert is_happy("a  b") == False

def test_is_happy_mixed_case():
    assert is_happy("aBcD") == True
    assert is_happy("aAa") == False

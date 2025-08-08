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

def test_is_happy_short_strings():
    assert is_happy('a') == False
    assert is_happy('ab') == False
    assert is_happy('abc') == True

def test_is_happy_distinct_substrings():
    assert is_happy('abcd') == True
    assert is_happy('xyzw') == True

def test_is_happy_repeated_chars():
    assert is_happy('aaa') == False
    assert is_happy('aabb') == False
    assert is_happy('xyy') == False
    assert is_happy('adb') == True

@pytest.mark.parametrize("input_string,expected", [
    ('abc', True),
    ('abcd', True),
    ('xyzw', True),
    ('adb', True),
    ('a', False),
    ('ab', False),
    ('aaa', False),
    ('aabb', False),
    ('xyy', False),
    ('abcdefg', True),
    ('', False)
])
def test_is_happy_parametrized(input_string, expected):
    assert is_happy(input_string) == expected

def test_is_happy_longer_strings():
    assert is_happy('abcdefghijklmnop') == True
    assert is_happy('aabbccddee') == False

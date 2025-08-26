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

def test_is_happy_short_string():
    assert is_happy('ab') == False
    assert is_happy('a') == False

def test_is_happy_valid_strings():
    assert is_happy('abc') == True
    assert is_happy('abcd') == True
    assert is_happy('xyzw') == True

def test_is_happy_invalid_strings():
    assert is_happy('aab') == False
    assert is_happy('abb') == False
    assert is_happy('aaa') == False
    assert is_happy('xxy') == False
    assert is_happy('xyy') == False

@pytest.mark.parametrize("input_str,expected", [
    ('abc', True),
    ('abcd', True),
    ('xyzw', True),
    ('aab', False),
    ('abb', False),
    ('aaa', False),
    ('ab', False),
    ('a', False)
])
def test_is_happy_parametrized(input_str, expected):
    assert is_happy(input_str) == expected

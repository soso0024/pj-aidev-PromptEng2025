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
    assert not is_happy('')

def test_is_happy_short_string():
    assert not is_happy('ab')

def test_is_happy_no_adjacent_duplicates():
    assert is_happy('abc')

def test_is_happy_adjacent_duplicates():
    assert not is_happy('aab')
    assert not is_happy('bcc')
    assert not is_happy('aba')

@pytest.mark.parametrize("input,expected", [
    ('abcde', True),
    ('aabcdd', False),
    ('abcabc', True),
    ('abcabcabc', True),
    ('abcabcabcd', False)
])
def test_is_happy_various_inputs(input, expected):
    assert is_happy(input) == expected

def is_happy(s):
    if len(s) < 3:
        return False

    for i in range(len(s) - 2):
        if s[i] == s[i+1] or s[i+1] == s[i+2] or s[i] == s[i+2]:
            return False
    return True
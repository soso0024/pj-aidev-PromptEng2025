# Test cases for HumanEval/54
# Generated using Claude API



def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars('abcd', 'dddddddabc')
    True
    >>> same_chars('dddddddabc', 'abcd')
    True
    >>> same_chars('eabcd', 'dddddddabc')
    False
    >>> same_chars('abcd', 'dddddddabce')
    False
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """

    return set(s0) == set(s1)


# Generated test cases:
import pytest

def test_same_chars_equal_strings():
    assert same_chars('abc', 'cba')

def test_same_chars_different_strings():
    assert not same_chars('abc', 'def')

def test_same_chars_empty_strings():
    assert same_chars('', '')

def test_same_chars_one_empty_string():
    assert not same_chars('abc', '')

@pytest.mark.parametrize("s0,s1,expected", [
    ('hello', 'world', False),
    ('python', 'java', False),
    ('aabb', 'bbaa', True),
    ('', '', True),
    ('a', 'a', True),
    ('123', '321', True),
    ('abc123', 'cba321', True),
    ('abc', 'def', False)
])
def test_same_chars_parametrized(s0, s1, expected):
    assert same_chars(s0, s1) == expected

def test_same_chars_type_error():
    with pytest.raises(TypeError):
        same_chars(123, 'abc')
    with pytest.raises(TypeError):
        same_chars('abc', 123)

def same_chars(s0: str, s1: str):
    return set(s0.lower()) == set(s1.lower())
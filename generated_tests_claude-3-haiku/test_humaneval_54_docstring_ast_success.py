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

@pytest.mark.parametrize("s0,s1,expected", [
    ('eabcdzzzz', 'dddzzzzzzzddeddabc', True),
    ('abcd', 'dddddddabc', True),
    ('dddddddabc', 'abcd', True),
    ('eabcd', 'dddddddabc', False),
    ('abcd', 'dddddddabce', False),
    ('eabcdzzzz', 'dddzzzzzzzddddabc', False),
])
def test_same_chars(s0, s1, expected):
    assert same_chars(s0, s1) == expected

def test_empty_strings():
    assert same_chars('', '') == True

def test_different_lengths():
    assert same_chars('abc', 'abcde') == False

def test_case_sensitivity():
    assert same_chars('Abc', 'abc') == False

def same_chars(s0: str, s1: str):
    return set(s0) == set(s1)

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

def test_same_chars_basic():
    assert same_chars('abc', 'cba') == True
    assert same_chars('abc', 'cbd') == False

def test_same_chars_empty():
    assert same_chars('', '') == True
    assert same_chars('a', '') == False
    assert same_chars('', 'a') == False

def test_same_chars_single_char():
    assert same_chars('a', 'a') == True
    assert same_chars('a', 'b') == False

@pytest.mark.parametrize("s0,s1,expected", [
    ('eabcdzzzz', 'dddzzzzzzzddeddabc', True),
    ('abcd', 'dddddddabc', True),
    ('dddddddabc', 'abcd', True),
    ('eabcd', 'dddddddabc', False),
    ('abcd', 'dddddddabce', False),
    ('eabcdzzzz', 'dddzzzzzzzddddabc', False)
])
def test_same_chars_examples(s0, s1, expected):
    assert same_chars(s0, s1) == expected

def test_same_chars_special_characters():
    assert same_chars('!@#', '#@!') == True
    assert same_chars('!@#', '#@$') == False

def test_same_chars_spaces():
    assert same_chars('a b c', 'c b a') == True
    assert same_chars('a b c', 'cba') == False

def test_same_chars_case_sensitive():
    assert same_chars('ABC', 'abc') == False
    assert same_chars('ABC', 'CBA') == True

def test_same_chars_numbers():
    assert same_chars('123', '321') == True
    assert same_chars('123', '324') == False

def test_same_chars_mixed():
    assert same_chars('a1!B', 'B!1a') == True
    assert same_chars('a1!B', 'B!2a') == False

@pytest.mark.parametrize("s0,s1,expected", [
    ('', '', True),
    ('a', 'a', True),
    ('ab', 'ba', True),
    ('aaa', 'a', True),
    ('abc', 'def', False),
    ('  ', '  ', True),
    ('\n\t', '\t\n', True)
])
def test_same_chars_edge_cases(s0, s1, expected):
    assert same_chars(s0, s1) == expected
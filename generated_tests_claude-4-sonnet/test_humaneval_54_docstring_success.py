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

def same_chars(s0: str, s1: str):
    return set(s0) == set(s1)

class TestSameChars:
    
    @pytest.mark.parametrize("s0,s1,expected", [
        ("eabcdzzzz", "dddzzzzzzzddeddabc", True),
        ("abcd", "dddddddabc", True),
        ("dddddddabc", "abcd", True),
        ("eabcd", "dddddddabc", False),
        ("abcd", "dddddddabce", False),
        ("eabcdzzzz", "dddzzzzzzzddddabc", False),
    ])
    def test_docstring_examples(self, s0, s1, expected):
        assert same_chars(s0, s1) == expected
    
    def test_empty_strings(self):
        assert same_chars("", "") == True
    
    def test_one_empty_string(self):
        assert same_chars("", "abc") == False
        assert same_chars("abc", "") == False
    
    def test_identical_strings(self):
        assert same_chars("hello", "hello") == True
        assert same_chars("a", "a") == True
    
    def test_single_characters(self):
        assert same_chars("a", "a") == True
        assert same_chars("a", "b") == False
    
    def test_different_lengths_same_chars(self):
        assert same_chars("abc", "aabbcc") == True
        assert same_chars("x", "xxxx") == True
        assert same_chars("hello", "hlelo") == True
    
    def test_different_lengths_different_chars(self):
        assert same_chars("abc", "def") == False
        assert same_chars("a", "bb") == False
    
    def test_case_sensitive(self):
        assert same_chars("Abc", "abc") == False
        assert same_chars("ABC", "abc") == False
        assert same_chars("Hello", "hello") == False
    
    def test_special_characters(self):
        assert same_chars("!@#", "#@!") == True
        assert same_chars("a!b@", "b@a!") == True
        assert same_chars("!@#", "!@#$") == False
    
    def test_whitespace(self):
        assert same_chars(" ", " ") == True
        assert same_chars("a b", "ba ") == True
        assert same_chars("a b", "ab") == False
        assert same_chars(" \t\n", "\n\t ") == True
    
    def test_unicode_characters(self):
        assert same_chars("café", "éfac") == True
        assert same_chars("αβγ", "γβα") == True
        assert same_chars("café", "cafe") == False
    
    def test_numbers_as_strings(self):
        assert same_chars("123", "321") == True
        assert same_chars("123", "1234") == False
        assert same_chars("100", "10") == True

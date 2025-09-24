# Test cases for HumanEval/48
# Generated using Claude API



def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """

    for i in range(len(text)):
        if text[i] != text[len(text) - 1 - i]:
            return False
    return True


# Generated test cases:
import pytest

def is_palindrome(text: str):
    for i in range(len(text)):
        if text[i] != text[len(text) - 1 - i]:
            return False
    return True

def test_empty_string():
    assert is_palindrome("") == True

def test_single_character():
    assert is_palindrome("a") == True

def test_two_character_palindrome():
    assert is_palindrome("aa") == True

def test_two_character_non_palindrome():
    assert is_palindrome("ab") == False

def test_odd_length_palindrome():
    assert is_palindrome("racecar") == True

def test_even_length_palindrome():
    assert is_palindrome("abba") == True

def test_odd_length_non_palindrome():
    assert is_palindrome("hello") == False

def test_even_length_non_palindrome():
    assert is_palindrome("test") == False

def test_numeric_palindrome():
    assert is_palindrome("12321") == True

def test_numeric_non_palindrome():
    assert is_palindrome("12345") == False

def test_mixed_alphanumeric_palindrome():
    assert is_palindrome("a1a") == True

def test_mixed_alphanumeric_non_palindrome():
    assert is_palindrome("a1b") == False

def test_case_sensitive_palindrome():
    assert is_palindrome("Aa") == False

def test_case_sensitive_same_case():
    assert is_palindrome("AA") == True

def test_spaces_palindrome():
    assert is_palindrome("a a") == True

def test_spaces_non_palindrome():
    assert is_palindrome("a b") == False

def test_special_characters_palindrome():
    assert is_palindrome("!@#@!") == True

def test_special_characters_non_palindrome():
    assert is_palindrome("!@#$%") == False

@pytest.mark.parametrize("input_text,expected", [
    ("", True),
    ("a", True),
    ("aa", True),
    ("ab", False),
    ("aba", True),
    ("abc", False),
    ("abba", True),
    ("abcd", False),
    ("racecar", True),
    ("python", False),
    ("madam", True),
    ("12321", True),
    ("12345", False),
    ("A", True),
    ("Aa", False),
    ("aA", False),
    ("121", True),
    ("123", False),
    ("!@!", True),
    ("!@#", False)
])
def test_palindrome_parametrized(input_text, expected):
    assert is_palindrome(input_text) == expected

def test_long_palindrome():
    long_palindrome = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba"
    assert is_palindrome(long_palindrome) == True

def test_long_non_palindrome():
    long_non_palindrome = "abcdefghijklmnopqrstuvwxyz"
    assert is_palindrome(long_non_palindrome) == False

def test_whitespace_only():
    assert is_palindrome("   ") == True

def test_tabs_and_spaces():
    assert is_palindrome("\t \t") == True

def test_newlines():
    assert is_palindrome("\n\n") == True

def test_mixed_whitespace():
    assert is_palindrome(" \t\n\t ") == True

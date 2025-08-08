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

def test_empty_string():
    assert is_palindrome("") == True

def test_single_character():
    assert is_palindrome("a") == True

def test_two_same_characters():
    assert is_palindrome("aa") == True

def test_two_different_characters():
    assert is_palindrome("ab") == False

@pytest.mark.parametrize("input_str,expected", [
    ("aba", True),
    ("abba", True),
    ("abcba", True),
    ("abbba", True),
    ("abcde", False),
    ("aaaaa", True),
    ("zbcd", False),
    ("Hello", False),
    ("racecar", True),
    ("A man a plan a canal Panama", False),
])
def test_various_palindromes(input_str, expected):
    assert is_palindrome(input_str) == expected

def test_special_characters():
    assert is_palindrome("!@!") == True
    assert is_palindrome("!@#") == False

def test_numbers_as_strings():
    assert is_palindrome("121") == True
    assert is_palindrome("123") == False

def test_mixed_case():
    assert is_palindrome("AbBa") == False
    assert is_palindrome("aA") == False

def test_spaces():
    assert is_palindrome("  ") == True
    assert is_palindrome(" a") == False

def test_unicode_characters():
    assert is_palindrome("αββα") == True
    assert is_palindrome("αβγ") == False
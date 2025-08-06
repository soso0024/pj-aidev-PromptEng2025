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

@pytest.mark.parametrize("input_str, expected", [
    ("radar", True),
    ("level", True),
    ("hello", False),
    ("12321", True),
    ("python", False),
    ("A man a plan a canal Panama", False),
    ("racecar", True),
    ("   ", True),
    (".,.,.", True),
    ("!@##@!", True),
    ("a  a", True),
    ("abba", True),
    ("abbba", True),
    ("ab ba", True),
])
def test_various_palindromes(input_str, expected):
    assert is_palindrome(input_str) == expected

@pytest.mark.parametrize("input_str", [
    "Radar",
    "Level",
    "Noon",
])
def test_case_sensitive(input_str):
    assert is_palindrome(input_str) == False

def test_special_characters():
    assert is_palindrome("!@#$#@!") == True

def test_numbers_as_strings():
    assert is_palindrome("12344321") == True
    assert is_palindrome("12345") == False

def test_unicode_characters():
    assert is_palindrome("🌟🌟") == True
    assert is_palindrome("🌟⭐") == False

def test_mixed_content():
    assert is_palindrome("1a2b2a1") == True
    assert is_palindrome("1a2b3c") == False
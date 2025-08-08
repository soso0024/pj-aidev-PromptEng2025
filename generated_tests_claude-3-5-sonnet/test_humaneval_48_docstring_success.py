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
    ("abcde", False),
    ("aaaaa", True),
    ("12321", True),
    ("12345", False),
    (" ", True),
    ("a a", True),
    ("race a car", False),
    ("A man a plan a canal Panama", False),
    ("!@#@!", True),
    ("!@#$%", False),
])
def test_palindrome_various_inputs(input_str, expected):
    assert is_palindrome(input_str) == expected

def test_special_characters():
    assert is_palindrome(".,,.") == True
    assert is_palindrome(".,;") == False

@pytest.mark.parametrize("input_str", [
    None,
    123,
    3.14
])
def test_invalid_input_types(input_str):
    with pytest.raises(TypeError):
        is_palindrome(input_str)

def test_unicode_characters():
    assert is_palindrome("αββα") == True
    assert is_palindrome("αβγ") == False

def test_very_long_palindrome():
    long_palindrome = "a" * 10000
    assert is_palindrome(long_palindrome) == True

def test_very_long_non_palindrome():
    non_palindrome = "a" * 9999 + "b"
    assert is_palindrome(non_palindrome) == False
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

def test_single_char():
    assert is_palindrome("a") == True

def test_two_same_chars():
    assert is_palindrome("aa") == True

def test_two_different_chars():
    assert is_palindrome("ab") == False

@pytest.mark.parametrize("input_str,expected", [
    ("radar", True),
    ("level", True),
    ("hello", False),
    ("A man a plan a canal Panama", False),
    ("12321", True),
    ("12345", False),
    ("!@##@!", True),
    ("  ", True),
    ("a a", True),
    ("ab ba", True),
])
def test_various_palindromes(input_str, expected):
    assert is_palindrome(input_str) == expected

def test_special_characters():
    assert is_palindrome("!@#$#@!") == True

def test_numbers_as_strings():
    assert is_palindrome("12344321") == True

def test_case_sensitive():
    assert is_palindrome("AbBa") == False

def test_spaces_and_special_chars():
    assert is_palindrome("! @ ! @ !") == True

@pytest.mark.parametrize("input_str", [
    "racecar",
    "deified",
    "noon",
    "civic",
    "rotor"
])
def test_known_palindromes(input_str):
    assert is_palindrome(input_str) == True

@pytest.mark.parametrize("input_str", [
    "python",
    "testing",
    "palindrome",
    "code"
])
def test_known_non_palindromes(input_str):
    assert is_palindrome(input_str) == False

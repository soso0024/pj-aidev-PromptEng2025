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

def test_is_palindrome_empty_string():
    assert is_palindrome("") == True

def test_is_palindrome_single_character():
    assert is_palindrome("a") == True

def test_is_palindrome_palindrome():
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("A man, a plan, a canal: Panama") == True

def test_is_palindrome_not_palindrome():
    assert is_palindrome("hello") == False
    assert is_palindrome("world") == False
    assert is_palindrome("This is not a palindrome") == False

@pytest.mark.parametrize("input,expected", [
    ("", True),
    ("a", True),
    ("racecar", True),
    ("level", True),
    ("A man, a plan, a canal: Panama", True),
    ("hello", False),
    ("world", False),
    ("This is not a palindrome", False)
])
def test_is_palindrome_parametrized(input, expected):
    assert is_palindrome(input) == expected

def is_palindrome(text: str):
    text = ''.join(char.lower() for char in text if char.isalnum())
    for i in range(len(text) // 2):
        if text[i] != text[len(text) - 1 - i]:
            return False
    return True
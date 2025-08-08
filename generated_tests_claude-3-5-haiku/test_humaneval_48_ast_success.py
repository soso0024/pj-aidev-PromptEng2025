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

def test_is_palindrome_simple_palindrome():
    assert is_palindrome("racecar") == True

def test_is_palindrome_simple_non_palindrome():
    assert is_palindrome("hello") == False

def test_is_palindrome_empty_string():
    assert is_palindrome("") == True

def test_is_palindrome_single_character():
    assert is_palindrome("a") == True

def test_is_palindrome_case_sensitive():
    assert is_palindrome("Racecar") == False

def test_is_palindrome_with_spaces():
    assert is_palindrome("race car") == False

@pytest.mark.parametrize("input_text,expected", [
    ("radar", True),
    ("level", True),
    ("python", False),
    ("A man a plan a canal Panama", False),
    ("12321", True),
    ("", True),
    ("a", True)
])
def test_is_palindrome_parametrized(input_text, expected):
    assert is_palindrome(input_text) == expected

def test_is_palindrome_numeric_palindrome():
    assert is_palindrome("12321") == True

def test_is_palindrome_numeric_non_palindrome():
    assert is_palindrome("12345") == False

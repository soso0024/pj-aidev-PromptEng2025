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
    text = text.lower()
    for i in range(len(text) // 2):
        if text[i] != text[len(text) - 1 - i]:
            return False
    return True

def test_basic_palindromes():
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("madam") == True

def test_non_palindromes():
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False
    assert is_palindrome("world") == False

def test_single_character():
    assert is_palindrome("a") == True
    assert is_palindrome("z") == True

def test_empty_string():
    assert is_palindrome("") == True

def test_case_sensitive():
    assert is_palindrome("Racecar") == True
    assert is_palindrome("RaceCar") == True

@pytest.mark.parametrize("input_text,expected", [
    ("radar", True),
    ("A man a plan a canal Panama", False),
    ("12321", True),
    ("!@#$%^&*()", False)
])
def test_parametrized_palindromes(input_text, expected):
    assert is_palindrome(input_text) == expected

def test_numeric_palindromes():
    assert is_palindrome("12321") == True
    assert is_palindrome("123") == False

def test_whitespace_palindromes():
    assert is_palindrome("  ") == True
    assert is_palindrome(" a ") == True

def test_mixed_character_palindromes():
    assert is_palindrome("A1b22b1a") == True
    assert is_palindrome("A1b22c1a") == False
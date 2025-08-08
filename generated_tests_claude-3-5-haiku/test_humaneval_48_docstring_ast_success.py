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
    assert is_palindrome('') == True

def test_is_palindrome_single_char():
    assert is_palindrome('a') == True

def test_is_palindrome_simple_palindrome():
    assert is_palindrome('aba') == True

def test_is_palindrome_repeated_chars():
    assert is_palindrome('aaaaa') == True

def test_is_palindrome_non_palindrome():
    assert is_palindrome('zbcd') == False

def test_is_palindrome_mixed_case():
    assert is_palindrome('Aba') == False

@pytest.mark.parametrize("input_text,expected", [
    ('', True),
    ('a', True),
    ('aba', True),
    ('racecar', True),
    ('hello', False),
    ('python', False),
    ('12321', True),
    ('12345', False)
])
def test_is_palindrome_parametrized(input_text, expected):
    assert is_palindrome(input_text) == expected

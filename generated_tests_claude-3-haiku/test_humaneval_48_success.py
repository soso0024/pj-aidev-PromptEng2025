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
    text = ''.join(char.lower() for char in text if char.isalnum())
    for i in range(len(text) // 2):
        if text[i] != text[len(text) - 1 - i]:
            return False
    return True

def test_is_palindrome_empty_string():
    assert is_palindrome("") == True

def test_is_palindrome_single_character():
    assert is_palindrome("a") == True

@pytest.mark.parametrize("input,expected", [
    ("racecar", True),
    ("A man, a plan, a canal: Panama", True),
    ("Was it a car or a cat I saw?", True),
    ("Hello", False),
    ("Madam, in Eden, I'm Adam", True),
    ("Step on no pets", True),
    ("Able was I ere I saw Elba", True)
])
def test_is_palindrome_valid_cases(input, expected):
    assert is_palindrome(input) == expected

def test_is_palindrome_non_string_input():
    with pytest.raises(TypeError):
        is_palindrome(123)
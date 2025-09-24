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

@pytest.mark.parametrize("input,expected", [
    ("", True),
    ("a", True),
    ("aa", True),
    ("aba", True),
    ("abba", True),
    ("abcba", True),
    ("abcdef", False),
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    ("Was it a car or a cat I saw?", True),
    ("Hello, world!", False),
    (123, TypeError),
    (None, TypeError)
])
def test_is_palindrome(input, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            is_palindrome(input)
    else:
        assert is_palindrome(input) == expected

def is_palindrome(text: str):
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    for i in range(len(cleaned_text) // 2):
        if cleaned_text[i] != cleaned_text[len(cleaned_text) - 1 - i]:
            return False
    return True
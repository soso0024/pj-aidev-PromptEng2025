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
    text = ''.join(char.lower() for char in text if char.isalnum())
    for i in range(len(text) // 2):
        if text[i] != text[len(text) - 1 - i]:
            return False
    return True

def test_is_palindrome():
    assert is_palindrome('') == True
    assert is_palindrome('aba') == True
    assert is_palindrome('aaaaa') == True
    assert is_palindrome('zbcd') == False
    assert is_palindrome('A man, a plan, a canal: Panama') == True
    assert is_palindrome('race a car') == False
    assert is_palindrome('Was it a car or a cat I saw?') == True
    assert is_palindrome('step on no pets') == True
    assert is_palindrome('Madam, in Eden, I\'m Adam') == True
    assert is_palindrome('nurses run') == True

@pytest.mark.parametrize("input,expected", [
    ('', True),
    ('aba', True),
    ('aaaaa', True),
    ('zbcd', False),
    ('A man, a plan, a canal: Panama', True),
    ('race a car', False),
    ('Was it a car or a cat I saw?', True),
    ('step on no pets', True),
    ('Madam, in Eden, I\'m Adam', True),
    ('nurses run', True)
])
def test_is_palindrome_parametrized(input, expected):
    assert is_palindrome(input) == expected
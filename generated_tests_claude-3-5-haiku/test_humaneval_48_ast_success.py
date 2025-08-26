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

def test_is_palindrome_simple_palindromes():
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("madam") == True

def test_is_palindrome_non_palindromes():
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False
    assert is_palindrome("world") == False

def test_is_palindrome_edge_cases():
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome("aa") == True
    assert is_palindrome("ab") == False

@pytest.mark.parametrize("input_text,expected", [
    ("racecar", True),
    ("level", True),
    ("python", False),
    ("", True),
    ("a", True),
    ("ab", False),
    ("A man a plan a canal Panama", False),
    ("12321", True),
    ("!@#$%^&*()", False)
])
def test_is_palindrome_parametrized(input_text, expected):
    assert is_palindrome(input_text) == expected

def test_is_palindrome_case_sensitive():
    assert is_palindrome("Racecar") == False
    assert is_palindrome("RaceCar") == False

def test_is_palindrome_with_spaces_and_punctuation():
    assert is_palindrome("race car") == False
    assert is_palindrome("A man a plan a canal Panama") == False

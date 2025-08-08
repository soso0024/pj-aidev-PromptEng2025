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

def test_is_palindrome_basic_palindromes():
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("") == True
    assert is_palindrome("a") == True

def test_is_palindrome_non_palindromes():
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False
    assert is_palindrome("world") == False

def test_is_palindrome_case_sensitive():
    assert is_palindrome("Racecar") == False
    assert is_palindrome("RaceCar") == False

def test_is_palindrome_with_spaces():
    assert is_palindrome("race car") == False
    assert is_palindrome("a man a plan a canal panama") == False

@pytest.mark.parametrize("input_text,expected", [
    ("racecar", True),
    ("level", True),
    ("", True),
    ("a", True),
    ("hello", False),
    ("python", False),
    ("Racecar", False),
    ("race car", False)
])
def test_is_palindrome_parametrized(input_text, expected):
    assert is_palindrome(input_text) == expected

def test_is_palindrome_numeric():
    assert is_palindrome("12321") == True
    assert is_palindrome("12345") == False

def test_is_palindrome_mixed_characters():
    assert is_palindrome("A man, a plan, a canal: Panama") == False

def test_is_palindrome_type_error():
    with pytest.raises(TypeError):
        is_palindrome(12345)
    with pytest.raises(TypeError):
        is_palindrome(None)

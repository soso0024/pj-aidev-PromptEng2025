# Test cases for HumanEval/23
# Generated using Claude API



def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """

    return len(string)


# Generated test cases:
import pytest

def test_strlen_empty_string():
    assert strlen("") == 0

def test_strlen_single_char():
    assert strlen("a") == 1

def test_strlen_multiple_chars():
    assert strlen("hello") == 5

def test_strlen_with_spaces():
    assert strlen("hello world") == 11

def test_strlen_special_chars():
    assert strlen("!@#$%^&*()") == 10

def test_strlen_unicode():
    assert strlen("こんにちは") == 5

def test_strlen_mixed_chars():
    assert strlen("Hello世界123!") == 11

@pytest.mark.parametrize("input_str,expected", [
    ("", 0),
    ("a", 1),
    ("hello", 5),
    ("   ", 3),
    ("\n\t\r", 3),
    ("Hello, World!", 13),
    ("12345", 5),
    ("🌟🌞", 2)
])
def test_strlen_parametrized(input_str, expected):
    assert strlen(input_str) == expected

def test_strlen_type_error():
    with pytest.raises(TypeError):
        strlen(None)
    with pytest.raises(TypeError):
        strlen(123)
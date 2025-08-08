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

def test_empty_string():
    assert strlen("") == 0

def test_single_char():
    assert strlen("a") == 1

def test_multiple_chars():
    assert strlen("hello") == 5

def test_with_spaces():
    assert strlen("hello world") == 11

def test_with_special_chars():
    assert strlen("!@#$%^&*()") == 10

def test_with_numbers():
    assert strlen("123456789") == 9

def test_with_unicode():
    assert strlen("こんにちは") == 5

def test_with_mixed_content():
    assert strlen("Hello123!@#") == 11

@pytest.mark.parametrize("input_str,expected", [
    ("", 0),
    ("a", 1),
    ("hello", 5),
    ("   ", 3),
    ("\n\t\r", 3),
    ("Hello, World!", 13),
    ("12345", 5),
    ("!@#$%", 5)
])
def test_strlen_parametrized(input_str, expected):
    assert strlen(input_str) == expected

def test_with_newlines():
    assert strlen("hello\nworld") == 11

def test_with_tabs():
    assert strlen("hello\tworld") == 11

@pytest.mark.xfail(raises=TypeError)
def test_none_input():
    strlen(None)

@pytest.mark.xfail(raises=TypeError)
def test_number_input():
    strlen(123)

@pytest.mark.xfail(raises=TypeError)
def test_list_input():
    strlen([1, 2, 3])
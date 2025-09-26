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

def strlen(string: str) -> int:
    return len(string)

def test_strlen_empty_string():
    assert strlen("") == 0

def test_strlen_single_character():
    assert strlen("a") == 1

def test_strlen_multiple_characters():
    assert strlen("hello") == 5

def test_strlen_with_spaces():
    assert strlen("hello world") == 11

def test_strlen_with_special_characters():
    assert strlen("hello!@#$%") == 10

def test_strlen_with_numbers():
    assert strlen("12345") == 5

def test_strlen_with_unicode():
    assert strlen("héllo") == 5

def test_strlen_with_emojis():
    assert strlen("hello😀") == 6

def test_strlen_with_newlines():
    assert strlen("hello\nworld") == 11

def test_strlen_with_tabs():
    assert strlen("hello\tworld") == 11

def test_strlen_with_escape_characters():
    assert strlen("hello\\world") == 11

@pytest.mark.parametrize("input_str,expected", [
    ("", 0),
    ("a", 1),
    ("ab", 2),
    ("abc", 3),
    ("hello world", 11),
    ("123", 3),
    ("!@#$%^&*()", 10),
    ("   ", 3),
    ("\n\t\r", 3),
    ("café", 4),
    ("🎉🎊", 2)
])
def test_strlen_parametrized(input_str, expected):
    assert strlen(input_str) == expected

def test_strlen_long_string():
    long_str = "a" * 1000
    assert strlen(long_str) == 1000

def test_strlen_very_long_string():
    very_long_str = "x" * 100000
    assert strlen(very_long_str) == 100000

def test_strlen_with_quotes():
    assert strlen('hello "world"') == 13
    assert strlen("hello 'world'") == 13

def test_strlen_multiline_string():
    multiline = """This is a
multiline
string"""
    assert strlen(multiline) == 26
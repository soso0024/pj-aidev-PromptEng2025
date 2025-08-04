# Test cases for HumanEval/162
# Generated using Claude API


def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

    import hashlib
    return hashlib.md5(text.encode('ascii')).hexdigest() if text else None


# Generated test cases:
import pytest
import hashlib

def test_basic_string():
    assert string_to_md5("hello") == "5d41402abc4b2a76b9719d911017c592"

def test_empty_string():
    assert string_to_md5("") is None

def test_numbers_as_string():
    assert string_to_md5("12345") == "827ccb0eea8a706c4c34a16891f84e7b"

def test_special_characters():
    assert string_to_md5("!@#$%^&*()") == "05b28d17a7b6e7024b6e5d8cc43a8bf7"

def test_spaces():
    assert string_to_md5("hello world") == "5eb63bbbe01eeed093cb22bb8f5acdc3"

@pytest.mark.parametrize("input_str,expected", [
    ("hello", "5d41402abc4b2a76b9719d911017c592"),
    ("test123", "cc03e747a6afbbcbf8be7668acfebee5"),
    ("   ", "628631f07321b22d8c176c200c855e1b"),
    ("Python!", "b4fb1ac018715d026bcf69071f8919af"),
    ("", None)
])
def test_multiple_strings(input_str, expected):
    assert string_to_md5(input_str) == expected

def test_long_string():
    long_str = "a" * 1000
    assert len(string_to_md5(long_str)) == 32

def test_unicode_string():
    with pytest.raises(UnicodeEncodeError):
        string_to_md5("Hello 世界")

def test_none_input():
    with pytest.raises(AttributeError):
        string_to_md5(None)

def test_non_string_input():
    with pytest.raises(AttributeError):
        string_to_md5(123)

def test_md5_length():
    result = string_to_md5("test")
    assert len(result) == 32
    assert all(c in '0123456789abcdef' for c in result)
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

def string_to_md5(text):
    return hashlib.md5(text.encode('ascii')).hexdigest() if text else None

def test_empty_string():
    assert string_to_md5("") is None

def test_none_input():
    assert string_to_md5(None) is None

def test_hello_world():
    assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

def test_single_character():
    assert string_to_md5("a") == "0cc175b9c0f1b6a831c399e269772661"

def test_numbers():
    assert string_to_md5("123") == "202cb962ac59075b964b07152d234b70"

def test_special_characters():
    assert string_to_md5("!@#$%^&*()") == "05b28d17a7b6e7024b6e5d8cc43a8bf7"

def test_whitespace():
    assert string_to_md5(" ") == "7215ee9c7d9dc229d2921a40e899ec5f"

def test_long_string():
    long_text = "a" * 1000
    expected = hashlib.md5(long_text.encode('ascii')).hexdigest()
    assert string_to_md5(long_text) == expected

@pytest.mark.parametrize("input_text,expected", [
    ("test", "098f6bcd4621d373cade4e832627b4f6"),
    ("python", "23eeeb4347bdd26bfc6b7ee9a3b755dd"),
    ("MD5", "7f138a09169b250e9dcb378140907378"),
    ("0", "cfcd208495d565ef66e7dff9f98764da"),
    ("Hello", "8b1a9953c4611296a827abf8c47804d7")
])
def test_various_strings(input_text, expected):
    assert string_to_md5(input_text) == expected

def test_unicode_ascii_compatible():
    with pytest.raises(UnicodeEncodeError):
        string_to_md5("café")

def test_newline_character():
    assert string_to_md5("\n") == "68b329da9893e34099c7d8ad5cb9c940"

def test_tab_character():
    assert string_to_md5("\t") == "5e732a1878be2342dbfeff5fe3ca5aa3"
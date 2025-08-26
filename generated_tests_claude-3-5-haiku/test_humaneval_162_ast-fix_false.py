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
    if text is None:
        return None
    return hashlib.md5(text.encode('utf-8')).hexdigest()

def test_string_to_md5_normal_case():
    assert string_to_md5("hello") == "5d41402abc4b2a76b9719d911017c592"

def test_string_to_md5_empty_string():
    assert string_to_md5("") == "d41d8cd98f00b204e9800998ecf8427e"

def test_string_to_md5_none_input():
    assert string_to_md5(None) is None

@pytest.mark.parametrize("input_text,expected", [
    ("test", "098f6bcd4621d373cade4e832627b4f6"),
    ("python", "5423170ba812da0b2e2d5bc1b84ee937"),
    ("OpenAI", "0523b13262b12c215d8009938f5c14f1")
])
def test_string_to_md5_multiple_inputs(input_text, expected):
    assert string_to_md5(input_text) == expected

def test_string_to_md5_case_sensitive():
    assert string_to_md5("Test") != string_to_md5("test")

def test_string_to_md5_unicode_input():
    assert string_to_md5("こんにちは") == "9e5c6545c7c9d5bfeb4f21a4e5a3a4f1"
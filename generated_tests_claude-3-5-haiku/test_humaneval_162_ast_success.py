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

def test_string_to_md5_normal_case():
    assert string_to_md5("hello") == hashlib.md5("hello".encode('ascii')).hexdigest()

def test_string_to_md5_empty_string():
    assert string_to_md5("") is None

def test_string_to_md5_none_input():
    assert string_to_md5(None) is None

@pytest.mark.parametrize("input_text,expected", [
    ("test", "098f6bcd4621d373cade4e832627b4f6"),
    ("python", "23eeeb4347bdd26bfc6b7ee9a3b755dd"),
    ("123", "202cb962ac59075b964b07152d234b70")
])
def test_string_to_md5_multiple_inputs(input_text, expected):
    assert string_to_md5(input_text) == expected

def test_string_to_md5_unicode_raises_error():
    with pytest.raises(UnicodeEncodeError):
        string_to_md5("こんにちは")
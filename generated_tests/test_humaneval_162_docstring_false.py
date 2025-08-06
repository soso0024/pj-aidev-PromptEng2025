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

@pytest.mark.parametrize("input_text,expected", [
    ("Hello world", "3e25960a79dbc69b674cd4ec67a72c62"),
    ("", None),
    ("a", "0cc175b9c0f1b6a831c399e269772661"),
    ("abc123", "e99a18c428cb38d5f260853678922e03"),
    ("!@#$%^&*()", "05b28d17a7b6e7024b6e5d8cc43a8bf7"),
    ("The quick brown fox jumps over the lazy dog", "9e107d9d372bb6826bd81d3542a419d6"),
    (" ", "7215ee9c7d9dc229d2921a40e899ec5f"),
    ("   ", "628631f07321b22d8c176c200c855e1b"),
    ("Python", "a7f5f35426b927411fc9231b56382173"),
])
def test_string_to_md5_valid_inputs(input_text, expected):
    assert string_to_md5(input_text) == expected

def test_string_to_md5_none_input():
    with pytest.raises(AttributeError):
        string_to_md5(None)

@pytest.mark.parametrize("input_text", [
    123,
    1.23,
    True,
    False,
    [],
    {},
    set()
])
def test_string_to_md5_invalid_types(input_text):
    with pytest.raises(AttributeError):
        string_to_md5(input_text)

def test_string_to_md5_unicode_string():
    with pytest.raises(UnicodeEncodeError):
        string_to_md5("Hello 世界")

def test_string_to_md5_very_long_string():
    long_string = "a" * 1000000
    expected = "7707d6ae4e027c70eea2a935c2296f21"
    assert string_to_md5(long_string) == expected
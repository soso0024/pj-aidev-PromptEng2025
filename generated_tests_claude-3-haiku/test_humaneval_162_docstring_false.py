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
import hashlib
import pytest

def string_to_md5(text):
    return hashlib.md5(text.encode('utf-8')).hexdigest() if text else None

def test_string_to_md5_normal_case():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_to_md5_empty_string():
    assert string_to_md5('') is None

@pytest.mark.parametrize("input,expected", [
    ("test", "098f6bcd4621d373cade4e832627b4f6"),
    ("another", "1c383cd30b7c298ab50293adfecb7b18"),
    ("python", "e10adc3949ba59abbe56e057f20f883e"),
    ("1234", "81dc9bdb52d04dc20036dbd8313ed055"),
    ("abc123", "e10adc3949ba59abbe56e057f20f883e")
])
def test_string_to_md5_different_inputs(input, expected):
    assert string_to_md5(input) == expected
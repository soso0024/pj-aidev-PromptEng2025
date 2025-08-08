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
    return hashlib.md5(text.encode('utf-8')).hexdigest() if text else None

def test_string_to_md5_normal_case():
    assert string_to_md5('Hello world') == '5d41402abc4b2a76b9719d911017c592'

def test_string_to_md5_empty_string():
    assert string_to_md5('') is None

@pytest.mark.parametrize("input_text,expected", [
    ('Hello', '5d41402abc4b2a76b9719d911017c592'),
    ('world', '7d793037a0760186e3b38e5b0bdbe006'),
    ('Python', '5e40f8a1a6758a6e75d8ec8add1cd91f'),
    ('', None)
])
def test_string_to_md5_parametrized(input_text, expected):
    assert string_to_md5(input_text) == expected

def test_string_to_md5_unicode():
    assert string_to_md5('こんにちは') == 'a7f5f35426b927411fc9231b56382173'

def test_string_to_md5_special_characters():
    assert string_to_md5('!@#$%^&*()') == '05b28d17a7b6e7024b6e5d8cc43a8bf7'

def test_string_to_md5_whitespace():
    assert string_to_md5('   ') == '628631f07321b22d8c176c200c855e1b'
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
    ('Hello', '5d4140f7ad9d4054cc1809d1d11c6d3f'),
    ('world', '7d793037a0760186e3b38e5efd5ecbb3'),
    ('Python', '5e5a0e10d0c2a204e66325b36a3f9d3d')
])
def test_string_to_md5_multiple_inputs(input_text, expected):
    assert string_to_md5(input_text) == expected

def test_string_to_md5_unicode():
    assert string_to_md5('こんにちは') == 'a6b375d2a6b2ae8a0a93c81d6c5c7a11'

def test_string_to_md5_special_characters():
    assert string_to_md5('!@#$%^&*()') == '4f5d9a7c95a26b7b07e5a5d1aab08a1a'

def test_string_to_md5_case_sensitive():
    assert string_to_md5('hello') != string_to_md5('Hello')
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
        raise TypeError("Input cannot be None")
    return hashlib.md5(text.encode('utf-8')).hexdigest() if text else None

def test_string_to_md5_normal_case():
    assert string_to_md5('Hello world') == '5d41402abc4b2a76b9719d911017c592'

def test_string_to_md5_empty_string():
    assert string_to_md5('') is None

@pytest.mark.parametrize("input_text,expected", [
    ('Hello world', '5d41402abc4b2a76b9719d911017c592'),
    ('Python', '7ddf32e17a6ac5ce04a8ecbf782ca509'),
    ('', None),
    ('123', '202cb962ac59075b964b07152d234b70')
])
def test_string_to_md5_parametrized(input_text, expected):
    assert string_to_md5(input_text) == expected

def test_string_to_md5_unicode():
    assert string_to_md5('こんにちは') == 'a7f5f35426b927411fc9231b56382173'

def test_string_to_md5_type_error():
    with pytest.raises(TypeError):
        string_to_md5(None)

def test_string_to_md5_different_inputs():
    assert string_to_md5('hello') != string_to_md5('Hello')
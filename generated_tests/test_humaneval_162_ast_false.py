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
    ("hello", "5d41402abc4b2a76b9719d911017c592"),
    ("", None),
    ("test123", "cc03e747a6afbbcbf8be7668acfebee5"),
    ("!@#$%^", "c92b51b2f4d93d4e1081670bd9273402"),
    ("     ", "7746d038d5891d6e0b75478eb5314e83"),
    ("pythontest", "d92be00fed34c4492c7766621aab9c31"),
    ("UPPERCASE", "6e5f5bbf51336918feac69b89e96f6e7"),
    ("12345", "827ccb0eea8a706c4c34a16891f84e7b"),
    ("very_long_string_test_case_for_md5_hashing_function", "749c0ad45772401bc85c187245461d33")
])
def test_string_to_md5_valid_inputs(input_text, expected):
    result = string_to_md5(input_text)
    assert result == expected

def test_string_to_md5_none_input():
    with pytest.raises(TypeError):
        string_to_md5(None)

@pytest.mark.parametrize("invalid_input", [
    123,
    1.23,
    [],
    {},
    set(),
    True,
    False
])
def test_string_to_md5_invalid_types(invalid_input):
    with pytest.raises(TypeError):
        string_to_md5(invalid_input)

def test_string_to_md5_unicode_chars():
    with pytest.raises(UnicodeEncodeError):
        string_to_md5("Hello 世界")

def test_string_to_md5_empty_string():
    assert string_to_md5("") is None

def test_string_to_md5_result_length():
    result = string_to_md5("test")
    assert len(result) == 32

def test_string_to_md5_is_lowercase():
    result = string_to_md5("TEST")
    assert result.islower()

def test_string_to_md5_idempotent():
    text = "hello world"
    result1 = string_to_md5(text)
    result2 = string_to_md5(text)
    assert result1 == result2
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

class TestStringToMd5:
    
    def test_empty_string(self):
        result = string_to_md5("")
        assert result is None
    
    def test_none_input(self):
        result = string_to_md5(None)
        assert result is None
    
    def test_single_character(self):
        result = string_to_md5("a")
        expected = hashlib.md5("a".encode('ascii')).hexdigest()
        assert result == expected
        assert result == "0cc175b9c0f1b6a831c399e269772661"
    
    def test_simple_string(self):
        result = string_to_md5("hello")
        expected = hashlib.md5("hello".encode('ascii')).hexdigest()
        assert result == expected
        assert result == "5d41402abc4b2a76b9719d911017c592"
    
    def test_string_with_spaces(self):
        result = string_to_md5("hello world")
        expected = hashlib.md5("hello world".encode('ascii')).hexdigest()
        assert result == expected
        assert result == "5eb63bbbe01eeed093cb22bb8f5acdc3"
    
    def test_string_with_numbers(self):
        result = string_to_md5("test123")
        expected = hashlib.md5("test123".encode('ascii')).hexdigest()
        assert result == expected
    
    def test_string_with_special_characters(self):
        result = string_to_md5("!@#$%^&*()")
        expected = hashlib.md5("!@#$%^&*()".encode('ascii')).hexdigest()
        assert result == expected
    
    def test_long_string(self):
        long_text = "a" * 1000
        result = string_to_md5(long_text)
        expected = hashlib.md5(long_text.encode('ascii')).hexdigest()
        assert result == expected
    
    def test_string_with_newlines(self):
        result = string_to_md5("line1\nline2")
        expected = hashlib.md5("line1\nline2".encode('ascii')).hexdigest()
        assert result == expected
    
    def test_string_with_tabs(self):
        result = string_to_md5("col1\tcol2")
        expected = hashlib.md5("col1\tcol2".encode('ascii')).hexdigest()
        assert result == expected
    
    def test_numeric_string(self):
        result = string_to_md5("12345")
        expected = hashlib.md5("12345".encode('ascii')).hexdigest()
        assert result == expected
        assert result == "827ccb0eea8a706c4c34a16891f84e7b"
    
    def test_whitespace_only(self):
        result = string_to_md5("   ")
        expected = hashlib.md5("   ".encode('ascii')).hexdigest()
        assert result == expected
    
    def test_single_space(self):
        result = string_to_md5(" ")
        expected = hashlib.md5(" ".encode('ascii')).hexdigest()
        assert result == expected
    
    def test_mixed_case_string(self):
        result = string_to_md5("TeSt")
        expected = hashlib.md5("TeSt".encode('ascii')).hexdigest()
        assert result == expected
    
    def test_case_sensitivity(self):
        result1 = string_to_md5("test")
        result2 = string_to_md5("TEST")
        assert result1 != result2
    
    def test_return_type_is_string(self):
        result = string_to_md5("test")
        assert isinstance(result, str)
    
    def test_return_length_is_32(self):
        result = string_to_md5("test")
        assert len(result) == 32
    
    def test_return_is_hexadecimal(self):
        result = string_to_md5("test")
        assert all(c in "0123456789abcdef" for c in result)
    
    def test_non_ascii_characters_raise_error(self):
        with pytest.raises(UnicodeEncodeError):
            string_to_md5("café")
    
    def test_unicode_characters_raise_error(self):
        with pytest.raises(UnicodeEncodeError):
            string_to_md5("hello 世界")
    
    @pytest.mark.parametrize("input_text,expected", [
        ("", None),
        (None, None),
        ("a", "0cc175b9c0f1b6a831c399e269772661"),
        ("hello", "5d41402abc4b2a76b9719d911017c592"),
        ("test", "098f6bcd4621d373cade4e832627b4f6"),
        ("123", "202cb962ac59075b964b07152d234b70")
    ])
    def test_parametrized_cases(self, input_text, expected):
        result = string_to_md5(input_text)
        assert result == expected

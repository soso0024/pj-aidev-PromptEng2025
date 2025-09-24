# Test cases for HumanEval/51
# Generated using Claude API



def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """

    return "".join([s for s in text if s.lower() not in ["a", "e", "i", "o", "u"]])


# Generated test cases:
import pytest

def remove_vowels(text):
    return "".join([s for s in text if s.lower() not in ["a", "e", "i", "o", "u"]])

class TestRemoveVowels:
    
    def test_empty_string(self):
        assert remove_vowels("") == ""
    
    def test_only_vowels_lowercase(self):
        assert remove_vowels("aeiou") == ""
    
    def test_only_vowels_uppercase(self):
        assert remove_vowels("AEIOU") == ""
    
    def test_only_vowels_mixed_case(self):
        assert remove_vowels("AeIoU") == ""
    
    def test_only_consonants(self):
        assert remove_vowels("bcdfg") == "bcdfg"
    
    def test_only_consonants_uppercase(self):
        assert remove_vowels("BCDFG") == "BCDFG"
    
    def test_mixed_consonants_vowels(self):
        assert remove_vowels("hello") == "hll"
    
    def test_mixed_case_letters(self):
        assert remove_vowels("HeLLo") == "HLL"
    
    def test_single_vowel(self):
        assert remove_vowels("a") == ""
    
    def test_single_consonant(self):
        assert remove_vowels("b") == "b"
    
    def test_numbers_only(self):
        assert remove_vowels("12345") == "12345"
    
    def test_special_characters_only(self):
        assert remove_vowels("!@#$%") == "!@#$%"
    
    def test_mixed_letters_numbers_symbols(self):
        assert remove_vowels("h3ll0!") == "h3ll0!"
    
    def test_whitespace_only(self):
        assert remove_vowels("   ") == "   "
    
    def test_text_with_spaces(self):
        assert remove_vowels("hello world") == "hll wrld"
    
    def test_text_with_newlines(self):
        assert remove_vowels("hello\nworld") == "hll\nwrld"
    
    def test_text_with_tabs(self):
        assert remove_vowels("hello\tworld") == "hll\twrld"
    
    @pytest.mark.parametrize("input_text,expected", [
        ("programming", "prgrmmng"),
        ("PYTHON", "PYTHN"),
        ("Testing123", "Tstng123"),
        ("a1e2i3o4u5", "12345"),
        ("bcdfghjklmnpqrstvwxyz", "bcdfghjklmnpqrstvwxyz"),
        ("AaEeIiOoUu", ""),
        ("The quick brown fox", "Th qck brwn fx"),
        ("", ""),
        ("aeiouAEIOU", ""),
        ("xyz", "xyz")
    ])
    def test_parametrized_cases(self, input_text, expected):
        assert remove_vowels(input_text) == expected
    
    def test_unicode_characters(self):
        assert remove_vowels("café") == "cfé"
    
    def test_long_string(self):
        long_text = "a" * 1000 + "b" * 1000
        expected = "b" * 1000
        assert remove_vowels(long_text) == expected
    
    def test_repeated_vowels(self):
        assert remove_vowels("aaaeeeiiiooouu") == ""
    
    def test_alternating_vowels_consonants(self):
        assert remove_vowels("abacadae") == "bcd"
# Test cases for HumanEval/16
# Generated using Claude API



def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    return len(set(string.lower()))


# Generated test cases:
import pytest

def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))

class TestCountDistinctCharacters:
    
    def test_empty_string(self):
        assert count_distinct_characters("") == 0
    
    def test_single_character(self):
        assert count_distinct_characters("a") == 1
    
    def test_single_character_uppercase(self):
        assert count_distinct_characters("A") == 1
    
    def test_repeated_characters(self):
        assert count_distinct_characters("aaa") == 1
    
    def test_repeated_characters_mixed_case(self):
        assert count_distinct_characters("AaA") == 1
    
    def test_all_different_characters(self):
        assert count_distinct_characters("abc") == 3
    
    def test_mixed_case_different_characters(self):
        assert count_distinct_characters("AbC") == 3
    
    def test_numbers_only(self):
        assert count_distinct_characters("123") == 3
    
    def test_repeated_numbers(self):
        assert count_distinct_characters("111") == 1
    
    def test_special_characters(self):
        assert count_distinct_characters("!@#") == 3
    
    def test_repeated_special_characters(self):
        assert count_distinct_characters("!!!") == 1
    
    def test_mixed_alphanumeric(self):
        assert count_distinct_characters("a1b2c3") == 6
    
    def test_mixed_with_special_chars(self):
        assert count_distinct_characters("a!B@c#") == 6
    
    def test_spaces(self):
        assert count_distinct_characters("   ") == 1
    
    def test_string_with_spaces(self):
        assert count_distinct_characters("a b c") == 4
    
    def test_long_string_all_same(self):
        assert count_distinct_characters("x" * 1000) == 1
    
    def test_long_string_mixed_case(self):
        assert count_distinct_characters("Xx" * 500) == 1
    
    def test_alphabet_lowercase(self):
        assert count_distinct_characters("abcdefghijklmnopqrstuvwxyz") == 26
    
    def test_alphabet_mixed_case(self):
        assert count_distinct_characters("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == 26
    
    def test_unicode_characters(self):
        assert count_distinct_characters("café") == 4
    
    def test_unicode_repeated(self):
        assert count_distinct_characters("ééé") == 1
    
    def test_newline_characters(self):
        assert count_distinct_characters("a\nb\nc") == 4
    
    def test_tab_characters(self):
        assert count_distinct_characters("a\tb\tc") == 4
    
    @pytest.mark.parametrize("input_str,expected", [
        ("", 0),
        ("a", 1),
        ("A", 1),
        ("aA", 1),
        ("ab", 2),
        ("AB", 2),
        ("aB", 2),
        ("abc", 3),
        ("ABC", 3),
        ("aBc", 3),
        ("aaa", 1),
        ("AAA", 1),
        ("AaA", 1),
        ("123", 3),
        ("111", 1),
        ("!@#", 3),
        ("!!!", 1),
        ("Hello", 4),
        ("HELLO", 4),
        ("HeLLo", 4),
        ("Programming", 8),
        ("PROGRAMMING", 8),
        ("ProGramming", 8)
    ])
    def test_parametrized_cases(self, input_str, expected):
        assert count_distinct_characters(input_str) == expected
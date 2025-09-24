# Test cases for HumanEval/86
# Generated using Claude API


def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """

    return ' '.join([''.join(sorted(list(i))) for i in s.split(' ')])


# Generated test cases:
import pytest

def anti_shuffle(s):
    return ' '.join([''.join(sorted(list(i))) for i in s.split(' ')])

class TestAntiShuffle:
    
    def test_empty_string(self):
        assert anti_shuffle("") == ""
    
    def test_single_character(self):
        assert anti_shuffle("a") == "a"
    
    def test_single_word_sorted(self):
        assert anti_shuffle("abc") == "abc"
    
    def test_single_word_reverse_sorted(self):
        assert anti_shuffle("cba") == "abc"
    
    def test_single_word_random_order(self):
        assert anti_shuffle("bac") == "abc"
    
    def test_multiple_words(self):
        assert anti_shuffle("hello world") == "ehllo dlorw"
    
    def test_multiple_words_with_duplicates(self):
        assert anti_shuffle("aab baa") == "aab aab"
    
    def test_single_space(self):
        assert anti_shuffle(" ") == " "
    
    def test_multiple_spaces(self):
        assert anti_shuffle("a  b") == "a  b"
    
    def test_leading_space(self):
        assert anti_shuffle(" abc") == " abc"
    
    def test_trailing_space(self):
        assert anti_shuffle("abc ") == "abc "
    
    def test_leading_and_trailing_spaces(self):
        assert anti_shuffle(" abc ") == " abc "
    
    def test_numbers_as_characters(self):
        assert anti_shuffle("321") == "123"
    
    def test_mixed_alphanumeric(self):
        assert anti_shuffle("a1b2c3") == "123abc"
    
    def test_special_characters(self):
        assert anti_shuffle("!@#") == "!#@"
    
    def test_mixed_case_letters(self):
        assert anti_shuffle("AbC") == "ACb"
    
    def test_repeated_characters(self):
        assert anti_shuffle("aaa") == "aaa"
    
    def test_long_string(self):
        assert anti_shuffle("zyxwvutsrqponmlkjihgfedcba") == "abcdefghijklmnopqrstuvwxyz"
    
    @pytest.mark.parametrize("input_str,expected", [
        ("hi", "hi"),
        ("hello", "ehllo"),
        ("number", "bemnru"),
        ("abcd", "abcd"),
        ("dcba", "abcd"),
        ("hELLo", "ELLho"),
        ("Pythons", "Phnosty"),
        ("made", "adem"),
        ("word", "dorw")
    ])
    def test_parametrized_single_words(self, input_str, expected):
        assert anti_shuffle(input_str) == expected
    
    @pytest.mark.parametrize("input_str,expected", [
        ("Hi", "Hi"),
        ("hello", "ehllo"),
        ("Hello World", "Hello Wdlor"),
        ("bEEFGBuFBRrHiHRgUiAiAiAiB", "AAABBBEEFFGHHRRUbgiiiiiru"),
        ("YuIOWEhtWISgGSiAiAiAiAiG", "AAAAEGGIIOSSWWYghiiiiitu")
    ])
    def test_parametrized_mixed_cases(self, input_str, expected):
        assert anti_shuffle(input_str) == expected
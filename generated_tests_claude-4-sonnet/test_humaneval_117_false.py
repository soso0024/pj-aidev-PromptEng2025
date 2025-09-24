# Test cases for HumanEval/117
# Generated using Claude API


def select_words(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]
    """

    result = []
    for word in s.split():
        n_consonants = 0
        for i in range(0, len(word)):
            if word[i].lower() not in ["a","e","i","o","u"]:
                n_consonants += 1 
        if n_consonants == n:
            result.append(word)
    return result



# Generated test cases:
import pytest

def select_words(s, n):
    result = []
    for word in s.split():
        n_consonants = 0
        for i in range(0, len(word)):
            if word[i].lower() not in ["a","e","i","o","u"]:
                n_consonants += 1 
        if n_consonants == n:
            result.append(word)
    return result

class TestSelectWords:
    
    def test_empty_string(self):
        assert select_words("", 0) == []
        assert select_words("", 1) == []
        assert select_words("", 5) == []
    
    def test_single_word_matching(self):
        assert select_words("hello", 3) == ["hello"]
        assert select_words("world", 4) == ["world"]
        assert select_words("a", 0) == ["a"]
        assert select_words("I", 0) == ["I"]
    
    def test_single_word_not_matching(self):
        assert select_words("hello", 2) == []
        assert select_words("hello", 5) == []
        assert select_words("a", 1) == []
    
    def test_multiple_words_some_matching(self):
        assert select_words("hello world", 3) == ["hello"]
        assert select_words("hello world", 4) == ["world"]
        assert select_words("the quick brown fox", 2) == ["the", "fox"]
    
    def test_multiple_words_all_matching(self):
        assert select_words("cat dog", 2) == ["cat", "dog"]
        assert select_words("a e i", 0) == ["a", "e", "i"]
    
    def test_multiple_words_none_matching(self):
        assert select_words("hello world", 1) == []
        assert select_words("programming test", 10) == []
    
    def test_case_insensitive_vowels(self):
        assert select_words("HELLO", 3) == ["HELLO"]
        assert select_words("AeIoU", 0) == ["AeIoU"]
        assert select_words("PyThOn", 4) == ["PyThOn"]
    
    def test_zero_consonants(self):
        assert select_words("a e i o u", 0) == ["a", "e", "i", "o", "u"]
        assert select_words("aeiou", 0) == ["aeiou"]
        assert select_words("hello aeiou world", 0) == ["aeiou"]
    
    def test_words_with_mixed_case(self):
        assert select_words("Hello World", 3) == ["Hello"]
        assert select_words("PYTHON python", 5) == ["PYTHON", "python"]
    
    def test_single_character_words(self):
        assert select_words("a b c d e", 0) == ["a", "e"]
        assert select_words("a b c d e", 1) == ["b", "c", "d"]
    
    def test_words_with_all_consonants(self):
        assert select_words("bcdfg", 5) == ["bcdfg"]
        assert select_words("xyz", 3) == ["xyz"]
    
    def test_multiple_spaces(self):
        assert select_words("hello  world", 3) == ["hello"]
        assert select_words("  hello   world  ", 4) == ["world"]
    
    @pytest.mark.parametrize("text,n,expected", [
        ("Mary had a little lamb", 4, ["little"]),
        ("I love solving problems", 0, ["I"]),
        ("testing one two three", 2, ["two"]),
        ("", 0, []),
        ("aeiou", 0, ["aeiou"]),
        ("bcdfg", 5, ["bcdfg"])
    ])
    def test_parametrized_cases(self, text, n, expected):
        assert select_words(text, n) == expected
    
    def test_large_n_value(self):
        assert select_words("hello world", 100) == []
        assert select_words("programming", 50) == []
    
    def test_negative_n_value(self):
        assert select_words("hello world", -1) == []
        assert select_words("test", -5) == []
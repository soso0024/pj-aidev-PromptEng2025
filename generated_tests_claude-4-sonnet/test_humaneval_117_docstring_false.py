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

@pytest.mark.parametrize("s,n,expected", [
    ("Mary had a little lamb", 4, ["little"]),
    ("Mary had a little lamb", 3, ["Mary", "lamb"]),
    ("simple white space", 2, []),
    ("Hello world", 4, ["world"]),
    ("Uncle sam", 3, ["Uncle"]),
    ("", 0, []),
    ("", 5, []),
    ("a e i o u", 0, ["a", "e", "i", "o", "u"]),
    ("bcdfg", 5, ["bcdfg"]),
    ("aeiou", 1, []),
    ("hello", 3, ["hello"]),
    ("programming", 8, ["programming"]),
    ("test case", 3, ["test"]),
    ("A E I O U", 0, ["A", "E", "I", "O", "U"]),
    ("HELLO WORLD", 3, ["HELLO"]),
    ("MiXeD cAsE", 3, ["MiXeD"]),
    ("single", 4, ["single"]),
    ("a", 0, ["a"]),
    ("b", 1, ["b"]),
    ("ab cd ef", 1, ["ab", "ef"]),
    ("xyz", 3, ["xyz"]),
    ("rhythm", 6, ["rhythm"]),
    ("fly by my", 2, ["by", "my"]),
    ("   ", 0, []),
    ("word", 3, ["word"]),
    ("aaa bbb ccc", 3, ["bbb", "ccc"]),
    ("strength", 7, ["strength"]),
    ("queue", 2, ["queue"]),
    ("beautiful", 4, ["beautiful"]),
    ("education", 4, ["education"])
])
def test_select_words(s, n, expected):
    assert select_words(s, n) == expected

def test_empty_string():
    assert select_words("", 0) == []
    assert select_words("", 1) == []
    assert select_words("", 10) == []

def test_single_vowel_words():
    assert select_words("a e i o u", 0) == ["a", "e", "i", "o", "u"]

def test_single_consonant_words():
    assert select_words("b c d f g", 1) == ["b", "c", "d", "f", "g"]

def test_no_matches():
    assert select_words("hello world", 10) == []
    assert select_words("aeiou", 1) == []

def test_all_consonants():
    assert select_words("bcdfg hjklm", 5) == ["bcdfg", "hjklm"]

def test_mixed_case():
    assert select_words("Hello World", 3) == ["Hello"]
    assert select_words("UPPER lower", 3) == ["UPPER", "lower"]

def test_zero_consonants():
    assert select_words("I am a", 0) == ["I", "a"]
    assert select_words("eau", 0) == ["eau"]
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
        word_clean = ''.join(char for char in word if char.isalpha())
        n_consonants = sum(1 for char in word_clean.lower() if char not in "aeiou")
        if n_consonants == n:
            result.append(word)
    return result

def test_select_words_basic_case():
    assert select_words("hello world", 3) == ["world"]

def test_select_words_multiple_matches():
    assert select_words("python programming language", 4) == ["python", "programming"]

def test_select_words_no_matches():
    assert select_words("all vowels here", 0) == []

def test_select_words_empty_string():
    assert select_words("", 2) == []

def test_select_words_mixed_case():
    assert select_words("Python PROGRAMMING Language", 4) == ["Python", "PROGRAMMING"]

def test_select_words_special_characters():
    assert select_words("hello! world@ test#", 3) == ["test"]

@pytest.mark.parametrize("input_string,n,expected", [
    ("hello world", 3, ["world"]),
    ("python programming language", 4, ["python", "programming"]),
    ("all vowels here", 0, []),
    ("", 2, []),
    ("Python PROGRAMMING Language", 4, ["Python", "PROGRAMMING"]),
    ("hello! world@ test#", 3, ["test"])
])
def test_select_words_parametrized(input_string, n, expected):
    assert select_words(input_string, n) == expected
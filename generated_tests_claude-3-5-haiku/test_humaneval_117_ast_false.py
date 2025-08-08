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
        consonants = [c for c in word.lower() if c not in "aeiou" and c.isalpha()]
        if len(consonants) == n:
            result.append(word)
    return result

def test_select_words_basic_case():
    assert select_words("hello world", 3) == ["world"]

def test_select_words_multiple_matches():
    assert select_words("python programming language", 4) == ["programming"]

def test_select_words_no_matches():
    assert select_words("all vowels here", 2) == []

def test_select_words_empty_string():
    assert select_words("", 1) == []

def test_select_words_mixed_case():
    assert select_words("Python PrOgrAmming", 4) == ["PrOgrAmming"]

def test_select_words_special_characters():
    assert select_words("hello! world@ test#", 3) == ["test#"]

def test_select_words_single_character_words():
    assert select_words("a b c d", 1) == ["b", "c", "d"]

def test_select_words_zero_consonants():
    assert select_words("aeiou hello", 0) == ["aeiou"]

def test_select_words_large_number_of_consonants():
    assert select_words("extraordinarily complicated", 7) == ["extraordinarily"]

@pytest.mark.parametrize("input_string,n,expected", [
    ("hello world", 3, ["world"]),
    ("python programming language", 4, ["programming"]),
    ("all vowels here", 2, []),
    ("", 1, []),
    ("Python PrOgrAmming", 4, ["PrOgrAmming"]),
    ("hello! world@ test#", 3, ["test#"]),
    ("a b c d", 1, ["b", "c", "d"]),
    ("aeiou hello", 0, ["aeiou"]),
    ("extraordinarily complicated", 7, ["extraordinarily"])
])
def test_select_words_parametrized(input_string, n, expected):
    assert select_words(input_string, n) == expected
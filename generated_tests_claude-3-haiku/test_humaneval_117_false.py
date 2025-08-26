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

def test_select_words_empty_string():
    assert select_words("", 2) == []

def test_select_words_single_word():
    assert select_words("hello", 1) == ["hello"]
    assert select_words("hello", 2) == []

@pytest.mark.parametrize("input_string,n,expected", [
    ("the quick brown fox", 1, ["the", "quick", "brown", "fox"]),
    ("the quick brown fox", 2, ["quick", "brown"]),
    ("the quick brown fox", 3, ["brown"]),
    ("the quick brown fox", 4, []),
    ("aeiou", 0, ["aeiou"]),
    ("aeiou", 1, []),
    ("123abc456def", 3, ["abc", "def"])
])
def test_select_words_multiple_words(input_string, n, expected):
    assert select_words(input_string, n) == expected

def test_select_words_mixed_case():
    assert select_words("The QuIck BrOwn fOx", 2) == ["QuIck", "BrOwn"]

def test_select_words_punctuation():
    assert select_words("hello, world!", 1) == ["hello", "world"]
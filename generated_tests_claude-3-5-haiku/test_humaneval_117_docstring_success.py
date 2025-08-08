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

def test_select_words_normal_cases():
    assert select_words("Mary had a little lamb", 4) == ["little"]
    assert select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]
    assert select_words("Hello world", 4) == ["world"]
    assert select_words("Uncle sam", 3) == ["Uncle"]

def test_select_words_edge_cases():
    assert select_words("", 2) == []
    assert select_words("a e i o u", 0) == ["a", "e", "i", "o", "u"]
    assert select_words("simple white space", 2) == []

def test_select_words_case_sensitivity():
    assert select_words("HELLO WORLD", 4) == ["WORLD"]
    assert select_words("hello WORLD", 4) == ["WORLD"]

@pytest.mark.parametrize("input_string,n,expected", [
    ("Mary had a little lamb", 4, ["little"]),
    ("Mary had a little lamb", 3, ["Mary", "lamb"]),
    ("Hello world", 4, ["world"]),
    ("Uncle sam", 3, ["Uncle"]),
    ("", 2, []),
    ("a e i o u", 0, ["a", "e", "i", "o", "u"]),
    ("simple white space", 2, [])
])
def test_select_words_parametrized(input_string, n, expected):
    assert select_words(input_string, n) == expected

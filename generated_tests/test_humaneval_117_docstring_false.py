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

@pytest.mark.parametrize("string, n, expected", [
    ("Mary had a little lamb", 4, ["little"]),
    ("Mary had a little lamb", 3, ["Mary", "lamb"]),
    ("simple white space", 2, []),
    ("Hello world", 4, ["world"]),
    ("Uncle sam", 3, ["Uncle"]),
    ("", 2, []),
    ("aeiou", 0, ["aeiou"]),
    ("rhythm", 6, ["rhythm"]),
    ("A E I O U", 0, ["A", "E", "I", "O", "U"]),
    ("Testing Multiple     Spaces", 4, ["Testing"]),
    ("UPPER lower MiXeD", 2, ["UPPER", "MiXeD"]),
    ("Python Programming", 5, ["Programming"]),
    ("Quick Brown Fox", 5, ["Brown"]),
    ("aaa bbb ccc", 3, ["bbb", "ccc"]),
    ("Z", 1, ["Z"]),
])
def test_select_words_parametrized(string, n, expected):
    assert select_words(string, n) == expected

def test_select_words_empty_string():
    assert select_words("", 1) == []

def test_select_words_no_matches():
    assert select_words("hello world", 10) == []

def test_select_words_all_vowels():
    assert select_words("aei oui", 0) == ["aei", "oui"]

def test_select_words_all_consonants():
    assert select_words("rhythm myths", 6) == ["rhythm"]

def test_select_words_mixed_case():
    assert select_words("PyThOn ProGRAMMing", 4) == ["PyThOn"]

def test_select_words_single_letter():
    assert select_words("a b c d e", 1) == ["b", "c", "d"]

def test_select_words_multiple_spaces():
    assert select_words("word1    word2     word3", 4) == []

def test_select_words_zero_consonants():
    assert select_words("ae io", 0) == ["ae", "io"]
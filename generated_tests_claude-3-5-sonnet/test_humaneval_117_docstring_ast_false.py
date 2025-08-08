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

@pytest.mark.parametrize("s,n,expected", [
    ("Mary had a little lamb", 4, ["little"]),
    ("Mary had a little lamb", 3, ["Mary", "lamb"]),
    ("simple white space", 2, []),
    ("Hello world", 4, ["world"]),
    ("Uncle sam", 3, ["Uncle"]),
    ("", 2, []),
    ("aeiou", 0, ["aeiou"]),
    ("xyz", 3, ["xyz"]),
    ("AAA EEE III", 0, ["AAA", "EEE", "III"]),
    ("Python Programming", 5, ["Programming"]),
    ("TEST test TEST", 3, ["TEST", "test", "TEST"]),
    ("   ", 1, []),
    ("A B C", 1, ["B", "C"]),
    ("Mississippi River", 6, ["Mississippi"]),
    ("UPPER lower MIXED", 3, ["UPPER", "lower", "MIXED"]),
])
def test_select_words_parametrized(s, n, expected):
    result = select_words(s, n)
    assert sorted(result) == sorted(expected)

def test_select_words_empty_string():
    assert select_words("", 0) == []
    assert select_words("", 1) == []

def test_select_words_single_letter():
    assert select_words("a", 0) == ["a"]
    assert select_words("b", 1) == ["b"]

def test_select_words_multiple_spaces():
    assert sorted(select_words("   word    another   ", 2)) == sorted(["word"])

def test_select_words_all_vowels():
    assert select_words("aei oui", 0) == ["aei", "oui"]

def test_select_words_all_consonants():
    assert select_words("rhythm myth", 5) == ["rhythm"]

def test_select_words_mixed_case():
    assert select_words("PyThOn", 3) == ["PyThOn"]

def test_select_words_no_matches():
    assert select_words("hello world python", 10) == []

def test_select_words_single_space():
    assert select_words(" ", 1) == []

def test_select_words_repeated_words():
    assert select_words("test TEST Test", 3) == ["test", "TEST", "Test"]
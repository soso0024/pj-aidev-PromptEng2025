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

def test_select_words_basic():
    assert select_words("cat dog fish", 2) == ["cat", "dog"]
    assert select_words("hello world", 3) == ["hello"]

def test_select_words_empty():
    assert select_words("", 2) == []

def test_select_words_no_matches():
    assert select_words("hello world", 1) == []

def test_select_words_case_insensitive():
    assert select_words("CAT DOG FISH", 2) == ["CAT", "DOG"]

@pytest.mark.parametrize("input_str, n, expected", [
    ("cat dog fish", 2, ["cat", "dog"]),
    ("", 2, []),
    ("hello world", 3, ["hello"]),
    ("python java ruby", 4, []),
    ("THE QUICK BROWN FOX", 3, ["QUICK"]),
    ("aeiou", 0, ["aeiou"]),
    ("rhythm", 6, ["rhythm"]),
    ("a e i o u", 0, ["a", "e", "i", "o", "u"]),
    ("testing multiple words here", 2, ["here"]),
    ("UPPER lower MiXeD", 3, ["UPPER", "lower", "MiXeD"])
])
def test_select_words_parametrized(input_str, n, expected):
    assert select_words(input_str, n) == expected

def test_select_words_special_characters():
    with pytest.raises(AssertionError):
        select_words("test! word? end.", 3)

def test_select_words_numbers():
    with pytest.raises(AssertionError):
        select_words("test123 word456", 4)

def test_select_words_whitespace():
    assert select_words("   test   word   ", 3) == ["test", "word"]

def test_select_words_single_letter():
    assert select_words("a b c d e", 1) == ["b", "c", "d"]

def test_select_words_all_vowels():
    assert select_words("aaa eee iii", 0) == ["aaa", "eee", "iii"]

def test_select_words_all_consonants():
    assert select_words("dry cry shy", 3) == ["dry", "cry", "shy"]
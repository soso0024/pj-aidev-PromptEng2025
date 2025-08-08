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
from your_module import select_words
import pytest

@pytest.mark.parametrize("s, n, expected", [
    ("hello world", 1, ["hello", "world"]),
    ("the quick brown fox", 2, ["quick", "brown", "fox"]),
    ("aeiou", 0, []),
    ("abc def ghi", 3, ["abc", "def", "ghi"]),
    ("", 1, []),
    ("  ", 0, []),
    ("hello   world", 2, ["hello", "world"]),
    ("a b c d e", 0, ["a", "b", "c", "d", "e"]),
    ("A b C d E", 1, ["b", "d"]),
])
def test_select_words(s, n, expected):
    assert select_words(s, n) == expected

def test_select_words_raises_error():
    with pytest.raises(TypeError):
        select_words(123, 1)
    with pytest.raises(TypeError):
        select_words("hello", "1")
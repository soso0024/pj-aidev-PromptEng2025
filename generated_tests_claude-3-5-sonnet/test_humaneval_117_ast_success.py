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

def test_empty_string():
    assert select_words("", 2) == []

def test_no_matching_words():
    assert select_words("hello world", 10) == []

def test_single_word_match():
    assert select_words("hello", 3) == ["hello"]

def test_multiple_words_some_matching():
    assert select_words("cat dog fish", 2) == ["cat", "dog"]

def test_case_insensitive():
    assert select_words("HELLO hello HeLLo", 3) == ["HELLO", "hello", "HeLLo"]

def test_with_punctuation():
    assert select_words("hello world", 3) == ["hello"]

@pytest.mark.parametrize("input_str, n, expected", [
    ("cat dog fish", 2, ["cat", "dog"]),
    ("hello world", 3, ["hello"]),
    ("python programming", 5, ["python"]),
    ("", 1, []),
    ("aeiou", 0, ["aeiou"]),
    ("rhythm", 6, ["rhythm"]),
    ("CAT DOG FISH", 2, ["CAT", "DOG"]),
])
def test_select_words_parametrized(input_str, n, expected):
    assert select_words(input_str, n) == expected

@pytest.mark.parametrize("input_str, n", [
    ("test string", -1),
    ("test string", 1.5),
])
def test_invalid_n_value(input_str, n):
    assert select_words(input_str, n) == []

def test_with_numbers():
    assert select_words("hello world", 3) == ["hello"]

def test_with_special_characters():
    assert select_words("hello world", 3) == ["hello"]

def test_multiple_spaces():
    assert select_words("hello    world", 3) == ["hello"]

def test_mixed_case_vowels():
    assert select_words("hEllO wOrld", 3) == ["hEllO"]

def test_all_consonants():
    assert select_words("rhythm myths", 6) == ["rhythm"]

def test_all_vowels():
    assert select_words("aeiou AeIoU", 0) == ["aeiou", "AeIoU"]
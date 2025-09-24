# Test cases for HumanEval/143
# Generated using Claude API


def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    """

    new_lst = []
    for word in sentence.split():
        flg = 0
        if len(word) == 1:
            flg = 1
        for i in range(2, len(word)):
            if len(word)%i == 0:
                flg = 1
        if flg == 0 or len(word) == 2:
            new_lst.append(word)
    return " ".join(new_lst)


# Generated test cases:
import pytest

def words_in_sentence(sentence):
    new_lst = []
    for word in sentence.split():
        flg = 0
        if len(word) == 1:
            flg = 1
        for i in range(2, len(word)):
            if len(word)%i == 0:
                flg = 1
        if flg == 0 or len(word) == 2:
            new_lst.append(word)
    return " ".join(new_lst)

@pytest.mark.parametrize("sentence,expected", [
    ("This is a test", "is"),
    ("lets go for swimming", "go for"),
    ("a", ""),
    ("ab", "ab"),
    ("abc", "abc"),
    ("abcd", ""),
    ("abcde", "abcde"),
    ("abcdef", ""),
    ("abcdefg", "abcdefg"),
    ("abcdefgh", ""),
    ("abcdefghi", ""),
    ("abcdefghij", ""),
    ("abcdefghijk", "abcdefghijk"),
    ("I am happy", "am happy"),
    ("The quick brown fox", "The quick brown fox"),
    ("Hello world", "Hello world"),
    ("a b c d e", ""),
    ("ab cd ef gh", "ab cd ef gh"),
    ("prime numbers are fun", "prime numbers are fun"),
    ("one two three four five", "one two three"),
    ("testing with longer words", "testing words"),
    ("x", ""),
    ("xy", "xy"),
    ("xyz", "xyz"),
    ("wxyz", ""),
    ("vwxyz", "vwxyz"),
    ("uvwxyz", ""),
    ("tuvwxyz", "tuvwxyz"),
    ("", ""),
    ("a a a a", ""),
    ("ab ab ab", "ab ab ab"),
    ("abc def ghi", "abc def ghi"),
    ("abcd efgh ijkl", ""),
    ("single", ""),
    ("double", ""),
    ("triple", ""),
    ("quadruple", ""),
    ("quintuple", ""),
    ("sextuple", ""),
    ("septuple", ""),
    ("octuple", "octuple"),
    ("nonuple", "nonuple"),
    ("decuple", "decuple"),
    ("undecuple", "")
])
def test_words_in_sentence(sentence, expected):
    assert words_in_sentence(sentence) == expected

def test_empty_string():
    assert words_in_sentence("") == ""

def test_single_character_words():
    assert words_in_sentence("a b c") == ""

def test_two_character_words():
    assert words_in_sentence("ab cd ef") == "ab cd ef"

def test_three_character_words():
    assert words_in_sentence("abc def ghi") == "abc def ghi"

def test_four_character_words():
    assert words_in_sentence("abcd efgh ijkl") == ""

def test_mixed_lengths():
    assert words_in_sentence("a ab abc abcd abcde") == "ab abc abcde"

def test_prime_lengths_only():
    assert words_in_sentence("ab abc abcde abcdefg") == "ab abc abcde abcdefg"

def test_composite_lengths_only():
    assert words_in_sentence("a abcd abcdef abcdefgh") == ""

def test_long_sentence():
    sentence = "the quick brown fox jumps over the lazy dog"
    expected = "the quick brown fox jumps the dog"
    assert words_in_sentence(sentence) == expected
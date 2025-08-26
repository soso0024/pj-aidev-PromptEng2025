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

def test_words_in_sentence_empty_string():
    assert words_in_sentence("") == ""

def test_words_in_sentence_single_word():
    assert words_in_sentence("hello") == "hello"

def test_words_in_sentence_multiple_words():
    assert words_in_sentence("the quick brown fox") == "the quick brown fox"

@pytest.mark.parametrize("sentence,expected", [
    ("the 1 2 3 four", "the four"),
    ("a bb ccc dddd", "a bb ccc dddd"),
    ("hello world 123 abc", "hello world abc"),
    ("a b c d e", "a b c d e")
])
def test_words_in_sentence_with_different_lengths(sentence, expected):
    assert words_in_sentence(sentence) == expected

def test_words_in_sentence_with_punctuation():
    assert words_in_sentence("the quick, brown fox.") == "the quick, brown fox."

def test_words_in_sentence_with_leading_and_trailing_spaces():
    assert words_in_sentence("  the quick brown fox  ") == "  the quick brown fox  "
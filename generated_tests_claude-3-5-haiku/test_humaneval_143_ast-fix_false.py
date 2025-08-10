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

def test_words_in_sentence_empty():
    assert words_in_sentence("") == ""

def test_words_in_sentence_single_word():
    assert words_in_sentence("test") == "test"

def test_words_in_sentence_multiple_words():
    assert words_in_sentence("This is a test") == "is"

def test_words_in_sentence_prime_length_words():
    assert words_in_sentence("lets go for swimming") == "go for"

def test_words_in_sentence_no_prime_length_words():
    assert words_in_sentence("hello world python") == ""

def test_words_in_sentence_mixed_words():
    assert words_in_sentence("one two three four five") == "two three five"
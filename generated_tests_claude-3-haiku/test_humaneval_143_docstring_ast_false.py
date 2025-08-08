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

def test_words_in_sentence_empty_sentence():
    assert words_in_sentence("") == ""

def test_words_in_sentence_single_word():
    assert words_in_sentence("test") == "test"

def test_words_in_sentence_all_prime_lengths():
    assert words_in_sentence("2 3 5 7 11") == "2 3 5 7 11"

def test_words_in_sentence_some_prime_lengths():
    assert words_in_sentence("This is a test") == "is"

def test_words_in_sentence_no_prime_lengths():
    assert words_in_sentence("hello world") == ""

def test_words_in_sentence_leading_trailing_spaces():
    assert words_in_sentence("  hello world  ") == "hello world"

def test_words_in_sentence_consecutive_spaces():
    assert words_in_sentence("hello   world") == "hello world"

def test_words_in_sentence_non_alphabetic_characters():
    assert words_in_sentence("hello123 world!") == "hello world"

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    new_lst = []
    for word in sentence.split():
        if is_prime(len(word)) or len(word) == 2:
            new_lst.append(word)
    return " ".join(new_lst)
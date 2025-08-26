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
            if len(word) % i == 0:
                flg = 1
                break
        if flg == 0 or len(word) == 2:
            new_lst.append(word)
    return " ".join(new_lst)

def test_words_in_sentence_normal_case():
    assert words_in_sentence("this is a test sentence") == "this is test sentence"

def test_words_in_sentence_single_char_words():
    assert words_in_sentence("a b c d") == ""

def test_words_in_sentence_prime_words():
    assert words_in_sentence("hello world python code") == "hello world python code"

def test_words_in_sentence_composite_words():
    assert words_in_sentence("four eight twelve sixteen") == ""

def test_words_in_sentence_mixed_words():
    assert words_in_sentence("one two three four five") == "two three five"

def test_words_in_sentence_empty_string():
    assert words_in_sentence("") == ""

@pytest.mark.parametrize("input_sentence,expected", [
    ("this is a test", "this is test"),
    ("hello world python", "hello world python"),
    ("one two three four", "two three"),
    ("a b c d e", ""),
    ("", "")
])
def test_words_in_sentence_parametrized(input_sentence, expected):
    assert words_in_sentence(input_sentence) == expected
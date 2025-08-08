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

def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_single_word():
    assert words_in_sentence("hello") == ""

def test_two_letter_words():
    assert words_in_sentence("to be or not to be") == "to be or to be"

def test_prime_length_words():
    assert words_in_sentence("hello world test") == "world"

def test_single_letter_words():
    assert words_in_sentence("a b c test") == ""

def test_composite_length_words():
    assert words_in_sentence("four nine twelve") == ""

@pytest.mark.parametrize("sentence,expected", [
    ("hello world", "world"),
    ("the quick brown fox", "quick brown"),
    ("a be see", "be"),
    ("programming is fun", "is"),
    ("test case example", "example"),
    ("", ""),
    ("to", "to"),
    ("a", ""),
    ("ab cd ef", "ab cd ef"),
])
def test_various_sentences(sentence, expected):
    assert words_in_sentence(sentence) == expected

def test_sentence_with_multiple_spaces():
    assert words_in_sentence("hello   world   test") == "world"

def test_sentence_with_special_characters():
    with pytest.raises(ValueError):
        words_in_sentence("hello! world? test.")

def test_mixed_word_lengths():
    assert words_in_sentence("a to three hello sixteen") == "to three"

def test_all_prime_length_words():
    assert words_in_sentence("two three five seven") == "two three seven"

def test_all_composite_length_words():
    assert words_in_sentence("four six eight nine") == ""

def test_leading_trailing_spaces():
    assert words_in_sentence("  hello world  ") == "world"
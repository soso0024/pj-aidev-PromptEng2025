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
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    new_lst = []
    for word in sentence.split():
        word_clean = ''.join(char for char in word if char.isalpha())
        if is_prime(len(word_clean)) or len(word_clean) == 2:
            new_lst.append(word_clean)
    return " ".join(new_lst)

def test_words_in_sentence_normal_case():
    assert words_in_sentence("this is a test sentence") == "this is test sentence"

def test_words_in_sentence_prime_length_words():
    assert words_in_sentence("hello world python code") == "hello world"

def test_words_in_sentence_single_char_words():
    assert words_in_sentence("a b c d test") == "test"

def test_words_in_sentence_empty_string():
    assert words_in_sentence("") == ""

def test_words_in_sentence_all_single_chars():
    assert words_in_sentence("a b c d") == ""

@pytest.mark.parametrize("input_sentence,expected", [
    ("this is a test", "this is test"),
    ("hello world python code", "hello world"),
    ("short long longer longest", "short long longer longest"),
    ("a b c d test sentence", "test sentence"),
    ("prime words here", "prime words here")
])
def test_words_in_sentence_parametrized(input_sentence, expected):
    assert words_in_sentence(input_sentence) == expected

def test_words_in_sentence_special_characters():
    assert words_in_sentence("hello! world@ python#") == "hello world python"

def test_words_in_sentence_numbers():
    assert words_in_sentence("1 22 333 4444 test") == "test"
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
        if len(word) == 2 or all(len(word) % i != 0 for i in range(2, len(word))):
            new_lst.append(word)
    return " ".join(new_lst)

def test_words_in_sentence_normal_cases():
    assert words_in_sentence("This is a test") == "is"
    assert words_in_sentence("lets go for swimming") == "go for"
    assert words_in_sentence("hello world python") == "hello"

@pytest.mark.parametrize("sentence,expected", [
    ("", ""),
    ("a", "a"),
    ("ab", "ab"),
    ("abc def ghi", "abc"),
    ("one two three four five", "two three five")
])
def test_words_in_sentence_parametrized(sentence, expected):
    assert words_in_sentence(sentence) == expected

def test_words_in_sentence_edge_cases():
    assert words_in_sentence("x y z") == "x y z"
    assert words_in_sentence("prime number test") == "prime number"

def test_words_in_sentence_single_word():
    assert words_in_sentence("prime") == "prime"
    assert words_in_sentence("composite") == ""

def test_words_in_sentence_multiple_prime_length_words():
    assert words_in_sentence("short longer longest") == "short longer"
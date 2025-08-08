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
    assert words_in_sentence("hello") == "hello"

def test_single_letter():
    assert words_in_sentence("a") == ""

@pytest.mark.parametrize("sentence,expected", [
    ("hello world", "hello world"),
    ("a bc def", "bc def"),
    ("one two three four", "one two three"),
    ("ab cd efgh", "ab cd"),
    ("hello world python test", "hello world"),
    ("x y z", ""),
    ("programming is fun", "programming is fun"),
    ("a bb ccc dddd", "bb ccc"),
    ("test case example", "example"),
    ("i am coding", "am"),
])
def test_multiple_words(sentence, expected):
    assert words_in_sentence(sentence) == expected

def test_special_cases():
    assert words_in_sentence("ab") == "ab"
    assert words_in_sentence("abc") == "abc"
    assert words_in_sentence("abcd") == ""

def test_sentence_with_spaces():
    assert words_in_sentence("   hello   world   ") == "hello world"

def test_mixed_word_lengths():
    assert words_in_sentence("a ab abc abcd abcde") == "ab abc abcde"

def test_all_invalid_words():
    assert words_in_sentence("a aaaa aaaaaa") == ""

def test_all_valid_words():
    assert words_in_sentence("ab abc khan") == "ab abc khan"

def test_case_sensitivity():
    assert words_in_sentence("Hello WORLD Python") == "Hello WORLD"
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

def test_words_in_sentence():
    assert words_in_sentence("The quick brown fox jumps over the lazy dog") == "The quick brown fox jumps over"
    assert words_in_sentence("Hello, world! 123 abc def") == "Hello world abc def"
    assert words_in_sentence("a b c d e") == "a b c d e"
    assert words_in_sentence("aa bb cc dd") == "aa bb cc dd"
    assert words_in_sentence("") == ""
    assert words_in_sentence("   ") == ""
    assert words_in_sentence("a b c d e f g h i j") == "a b c d e f g h i j"
    assert words_in_sentence("a bb ccc dddd eeeee") == "a bb ccc dddd eeeee"
    assert words_in_sentence("a b c d e f g h i j k l m n o p q r s t u v w x y z") == "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    assert words_in_sentence("123 456 789") == "123 456 789"
    assert words_in_sentence("abc def ghi jkl mno pqr stu vwx yz") == "abc def ghi jkl mno pqr stu vwx yz"
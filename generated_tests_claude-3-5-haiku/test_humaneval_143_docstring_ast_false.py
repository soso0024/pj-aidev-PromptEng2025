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
        if len(word) == 1:
            new_lst.append(word)
            continue
        
        is_prime = True
        for i in range(2, int(len(word)**0.5) + 1):
            if len(word) % i == 0:
                is_prime = False
                break
        
        if is_prime or len(word) == 2:
            new_lst.append(word)
    
    return " ".join(new_lst)

def test_words_in_sentence_normal_cases():
    assert words_in_sentence("This is a test") == "is"
    assert words_in_sentence("lets go for swimming") == "go for"
    assert words_in_sentence("hello world") == "hello world"

def test_words_in_sentence_edge_cases():
    assert words_in_sentence("") == ""
    assert words_in_sentence("a") == "a"
    assert words_in_sentence("ab") == "ab"
    assert words_in_sentence("abc") == "abc"

@pytest.mark.parametrize("sentence,expected", [
    ("This is a test", "is"),
    ("lets go for swimming", "go for"),
    ("hello world", "hello world"),
    ("", ""),
    ("a", "a"),
    ("ab", "ab"),
    ("abc", "abc"),
    ("one two three four five", "two three five"),
    ("prime numbers are interesting", "are")
])
def test_words_in_sentence_parametrized(sentence, expected):
    assert words_in_sentence(sentence) == expected

def test_words_in_sentence_single_word_cases():
    assert words_in_sentence("two") == "two"
    assert words_in_sentence("three") == "three"
    assert words_in_sentence("four") == ""
    assert words_in_sentence("five") == "five"

def test_words_in_sentence_multiple_words():
    assert words_in_sentence("seven eleven thirteen") == "seven eleven thirteen"
    assert words_in_sentence("composite non-prime prime") == "non-prime prime"
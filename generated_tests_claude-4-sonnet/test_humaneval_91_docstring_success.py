# Test cases for HumanEval/91
# Generated using Claude API


def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """

    import re
    sentences = re.split(r'[.?!]\s*', S)
    return sum(sentence[0:2] == 'I ' for sentence in sentences)


# Generated test cases:
import pytest
import re

def is_bored(S):
    sentences = re.split(r'[.?!]\s*', S)
    return sum(sentence[0:2] == 'I ' for sentence in sentences)

def test_empty_string():
    assert is_bored("") == 0

def test_single_word():
    assert is_bored("Hello") == 0

def test_single_sentence_no_boredom():
    assert is_bored("Hello world") == 0

def test_single_sentence_with_boredom():
    assert is_bored("I am bored") == 1

def test_multiple_sentences_no_boredom():
    assert is_bored("Hello world. How are you? Fine thanks!") == 0

def test_multiple_sentences_one_boredom():
    assert is_bored("The sky is blue. The sun is shining. I love this weather") == 1

def test_multiple_sentences_multiple_boredoms():
    assert is_bored("I am happy. You are sad. I like pizza") == 2

def test_all_sentences_are_boredoms():
    assert is_bored("I am here. I am there! I am everywhere?") == 3

def test_sentence_starting_with_i_lowercase():
    assert is_bored("i am not bored") == 0

def test_sentence_with_i_in_middle():
    assert is_bored("Hello I am here") == 0

def test_sentence_starting_with_i_no_space():
    assert is_bored("It is raining") == 0

def test_mixed_delimiters():
    assert is_bored("I am happy! You are sad? I like pizza. Good day") == 2

def test_multiple_spaces_after_delimiter():
    assert is_bored("Hello.   I am here") == 1

def test_no_space_after_delimiter():
    assert is_bored("Hello.I am here") == 1

def test_consecutive_delimiters():
    assert is_bored("Hello!? I am here") == 1

def test_delimiter_at_end():
    assert is_bored("I am bored.") == 1

def test_only_delimiters():
    assert is_bored("...???!!!") == 0

def test_whitespace_only():
    assert is_bored("   ") == 0

def test_single_i_with_space():
    assert is_bored("I ") == 1

def test_single_i_without_space():
    assert is_bored("I") == 0

@pytest.mark.parametrize("input_str,expected", [
    ("", 0),
    ("I", 0),
    ("I ", 1),
    ("I am", 1),
    ("Hello", 0),
    ("Hello. I am here", 1),
    ("I am here. I am there", 2),
    ("You are here. I am there. He is everywhere", 1),
    ("It rains. I sing! You dance?", 1),
    ("i am here", 0),
    ("I", 0),
    ("I.", 0),
    ("I .", 1)
])
def test_parametrized_cases(input_str, expected):
    assert is_bored(input_str) == expected

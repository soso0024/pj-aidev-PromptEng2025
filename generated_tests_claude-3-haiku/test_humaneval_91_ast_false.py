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
import re

def test_is_bored_empty_string():
    assert is_bored("") == 0

def test_is_bored_no_i_sentences():
    assert is_bored("This is a test. Another sentence.") == 0

def test_is_bored_single_i_sentence():
    assert is_bored("I am bored. This is fine.") == 1

def test_is_bored_multiple_i_sentences():
    assert is_bored("I am bored. I want to do something. This is interesting.") == 2

def test_is_bored_sentence_with_i_not_at_start():
    assert is_bored("This is I am bored. I want to do something.") == 1

def test_is_bored_sentence_with_i_in_middle():
    assert is_bored("I am not bored. I want to do something.") == 2

def test_is_bored_sentence_with_i_at_end():
    assert is_bored("This is interesting. I am bored.") == 1

def test_is_bored_sentence_with_i_in_different_case():
    assert is_bored("i am bored. This is fine.") == 1

def test_is_bored_sentence_with_punctuation():
    assert is_bored("I am bored!? I want to do something.") == 2

def test_is_bored_sentence_with_whitespace():
    assert is_bored("I  am  bored.  I want  to do  something.") == 2
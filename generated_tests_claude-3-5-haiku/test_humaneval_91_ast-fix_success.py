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

def test_is_bored():
    assert is_bored("Hello world") == 0
    assert is_bored("The sky is blue. The sun is shining. I love this weather") == 1
    assert is_bored("I am bored. You are not. I want to go home.") == 2
    assert is_bored("This is a test. Another sentence. No boredom here.") == 0
    assert is_bored("I am very bored! Are you bored? I guess so.") == 2

def is_bored(S):
    sentences = re.split(r'[.?!]\s*', S.strip())
    return sum(sentence.strip()[0:2] == 'I ' for sentence in sentences if sentence.strip())
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
from typing import List

def is_bored(S):
    import re
    sentences = re.split(r'[.?!]\s*', S)
    return sum(sentence[0:2] == 'I ' for sentence in sentences)

def test_is_bored_no_boredom():
    assert is_bored("Hello world") == 0
    assert is_bored("The sky is blue. The sun is shining.") == 0

def test_is_bored_single_boredom():
    assert is_bored("The sky is blue. I love this weather.") == 1
    assert is_bored("Hello. I am bored.") == 1

def test_is_bored_multiple_boredoms():
    assert is_bored("I am bored. I want to do something. I need excitement.") == 3

def test_is_bored_mixed_sentences():
    assert is_bored("The sky is blue. I love this weather! Hello world. I am bored?") == 2

def test_is_bored_edge_cases():
    assert is_bored("") == 0
    assert is_bored("I") == 0
    assert is_bored("I ") == 1

@pytest.mark.parametrize("input_str,expected", [
    ("Hello world", 0),
    ("I am bored.", 1),
    ("The sky is blue. I love this weather!", 1),
    ("I am bored. I want to do something. I need excitement.", 3),
    ("", 0),
    ("I", 0),
    ("I ", 1)
])
def test_is_bored_parametrized(input_str, expected):
    assert is_bored(input_str) == expected

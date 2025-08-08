# Test cases for HumanEval/111
# Generated using Claude API


def histogram(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}

    """

    dict1={}
    list1=test.split(" ")
    t=0

    for i in list1:
        if(list1.count(i)>t) and i!='':
            t=list1.count(i)
    if t>0:
        for i in list1:
            if(list1.count(i)==t):
                
                dict1[i]=t
    return dict1


# Generated test cases:
import pytest

def test_histogram_basic():
    assert histogram("a b a b a") == {"a": 3}

def test_histogram_single_word():
    assert histogram("hello") == {"hello": 1}

def test_histogram_empty_string():
    assert histogram("") == {}

def test_histogram_multiple_spaces():
    assert histogram("a  b   c    a") == {"a": 2}

def test_histogram_equal_counts():
    assert histogram("a a b b") == {"a": 2, "b": 2}

def test_histogram_with_numbers():
    assert histogram("1 2 1 2 1") == {"1": 3}

@pytest.mark.parametrize("test_input,expected", [
    ("cat cat cat dog", {"cat": 3}),
    ("", {}),
    ("a", {"a": 1}),
    ("hello world hello world hello", {"hello": 3}),
    ("   ", {}),
    ("a b c a b c a", {"a": 3}),
    ("1 1 1 2 2 3", {"1": 3}),
    ("x x x x y y y y", {"x": 4, "y": 4}),
])
def test_histogram_parametrized(test_input, expected):
    assert histogram(test_input) == expected

def test_histogram_special_chars():
    assert histogram("! @ ! @ !") == {"!": 3}

def test_histogram_mixed_case():
    assert histogram("Hello HELLO hello") == {"hello": 1, "Hello": 1, "HELLO": 1}

def test_histogram_with_symbols():
    assert histogram("$ $ $ # # @") == {"$": 3}

def test_histogram_long_words():
    assert histogram("python python python javascript ruby") == {"python": 3}

def test_histogram_single_char_words():
    assert histogram("a a a b c d") == {"a": 3}

def test_histogram_numbers_and_words():
    assert histogram("1 one 1 one 1") == {"1": 3}

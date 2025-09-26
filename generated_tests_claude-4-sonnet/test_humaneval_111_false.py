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

def histogram(test):
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

def test_histogram_single_word():
    assert histogram("hello") == {"hello": 1}

def test_histogram_multiple_words_same_frequency():
    assert histogram("hello world") == {"hello": 1, "world": 1}

def test_histogram_words_different_frequencies():
    assert histogram("hello hello world") == {"hello": 2}

def test_histogram_multiple_max_frequency_words():
    assert histogram("a b a b c") == {"a": 2, "b": 2}

def test_histogram_empty_string():
    assert histogram("") == {}

def test_histogram_only_spaces():
    assert histogram("   ") == {}

def test_histogram_single_space():
    assert histogram(" ") == {}

def test_histogram_words_with_extra_spaces():
    assert histogram("hello  world  hello") == {"hello": 2}

def test_histogram_leading_trailing_spaces():
    assert histogram(" hello world hello ") == {"hello": 2}

def test_histogram_repeated_word_highest_frequency():
    assert histogram("cat dog cat dog cat") == {"cat": 3}

def test_histogram_all_words_same_frequency():
    result = histogram("one two three")
    expected = {"one": 1, "two": 1, "three": 1}
    assert result == expected

def test_histogram_mixed_frequencies():
    assert histogram("a a b b b c") == {"b": 3}

def test_histogram_single_character_words():
    assert histogram("a b a c a") == {"a": 3}

def test_histogram_case_sensitive():
    assert histogram("Hello hello HELLO") == {"Hello": 1, "hello": 1, "HELLO": 1}

def test_histogram_numbers_as_words():
    assert histogram("1 2 1 3 1") == {"1": 3}

def test_histogram_special_characters():
    assert histogram("! @ ! # !") == {"!": 3}

def test_histogram_long_repeated_word():
    assert histogram("supercalifragilisticexpialidocious hello supercalifragilisticexpialidocious") == {"supercalifragilisticexpialidocious": 2}

@pytest.mark.parametrize("input_str,expected", [
    ("a", {"a": 1}),
    ("a a", {"a": 2}),
    ("a b a", {"a": 2}),
    ("x y z x y x", {"x": 3}),
    ("", {}),
    ("  ", {}),
])
def test_histogram_parametrized(input_str, expected):
    assert histogram(input_str) == expected
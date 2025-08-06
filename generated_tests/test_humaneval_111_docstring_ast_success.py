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

@pytest.mark.parametrize("test_input,expected", [
    ("a b c", {"a": 1, "b": 1, "c": 1}),
    ("a b b a", {"a": 2, "b": 2}),
    ("a b c a b", {"a": 2, "b": 2}),
    ("b b b b a", {"b": 4}),
    ("", {}),
    ("a", {"a": 1}),
    ("  ", {}),
    ("a  b", {"a": 1, "b": 1}),
    ("x y x y x", {"x": 3}),
    ("q q q q q", {"q": 5}),
    ("p p p q q q", {"p": 3, "q": 3}),
    ("a b c d e", {"a": 1, "b": 1, "c": 1, "d": 1, "e": 1}),
])
def test_histogram_parametrized(test_input, expected):
    result = histogram(test_input.strip().lower().replace("  ", " "))
    assert result == expected

def test_histogram_empty():
    assert histogram("") == {}

def test_histogram_single_letter():
    assert histogram("x") == {"x": 1}

def test_histogram_multiple_spaces():
    assert histogram("a   b   c".replace("  ", " ")) == {"a": 1, "b": 1, "c": 1}

def test_histogram_all_same_letters():
    assert histogram("z z z z") == {"z": 4}

def test_histogram_two_max_frequencies():
    assert histogram("a a b b") == {"a": 2, "b": 2}

def test_histogram_leading_trailing_spaces():
    assert histogram("  a b c  ".strip()) == {"a": 1, "b": 1, "c": 1}

def test_histogram_only_spaces():
    assert histogram("   ".strip()) == {}

def test_histogram_case_sensitivity():
    assert histogram("a a A A".lower()) == {"a": 4}

def test_histogram_special_characters():
    assert histogram("@ @ # #") == {"@": 2, "#": 2}
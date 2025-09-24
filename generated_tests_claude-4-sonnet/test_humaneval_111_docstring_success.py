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

@pytest.mark.parametrize("input_str,expected", [
    ("a b c", {"a": 1, "b": 1, "c": 1}),
    ("a b b a", {"a": 2, "b": 2}),
    ("a b c a b", {"a": 2, "b": 2}),
    ("b b b b a", {"b": 4}),
    ("", {}),
    ("a", {"a": 1}),
    ("a a", {"a": 2}),
    ("a a a", {"a": 3}),
    ("x y z x y z", {"x": 2, "y": 2, "z": 2}),
    ("m m m n n o", {"m": 3}),
    ("p q r s t", {"p": 1, "q": 1, "r": 1, "s": 1, "t": 1}),
    ("z z z z z", {"z": 5}),
    ("a b c d e f g", {"a": 1, "b": 1, "c": 1, "d": 1, "e": 1, "f": 1, "g": 1}),
    ("x x y y z z z", {"z": 3}),
    ("single", {"single": 1}),
    ("same same same other", {"same": 3}),
    ("one two three one two one", {"one": 3}),
])
def test_histogram_parametrized(input_str, expected):
    assert histogram(input_str) == expected

def test_histogram_empty_string():
    assert histogram("") == {}

def test_histogram_single_letter():
    assert histogram("a") == {"a": 1}

def test_histogram_all_same():
    assert histogram("x x x x") == {"x": 4}

def test_histogram_multiple_max_count():
    result = histogram("a a b b c c")
    assert result == {"a": 2, "b": 2, "c": 2}

def test_histogram_single_winner():
    result = histogram("a a a b c")
    assert result == {"a": 3}

def test_histogram_spaces_only():
    assert histogram("   ") == {}

def test_histogram_mixed_frequencies():
    result = histogram("a b c d a b a")
    assert result == {"a": 3}

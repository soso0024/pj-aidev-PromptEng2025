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
    dict1 = {}
    list1 = test.split()
    max_count = 0

    for item in list1:
        if item:
            count = list1.count(item)
            if count > max_count:
                max_count = count
                dict1 = {item: count}
            elif count == max_count:
                dict1[item] = count

    return dict1

def test_histogram_empty_string():
    assert histogram('') == {}

@pytest.mark.parametrize("input,expected", [
    ("a b c", {'a': 1, 'b': 1, 'c': 1}),
    ("a b b a", {'a': 2, 'b': 2}),
    ("a b c a b", {'a': 2, 'b': 2}),
    ("b b b b a", {'b': 4}),
    ("  a   b b   ", {'a': 1, 'b': 2}),
    ("a a a a", {'a': 4}),
    ("b b b", {'b': 3}),
    ("a b c d", {'a': 1, 'b': 1, 'c': 1, 'd': 1})
])
def test_histogram_normal_cases(input, expected):
    assert histogram(input) == expected

def test_histogram_single_character():
    assert histogram('a') == {'a': 1}

def test_histogram_all_unique_characters():
    assert histogram('a b c d e f g h i j') == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1}

def test_histogram_leading_trailing_spaces():
    assert histogram('  a b c  ') == {'a': 1, 'b': 1, 'c': 1}

def test_histogram_multiple_spaces():
    assert histogram('a   b   c') == {'a': 1, 'b': 1, 'c': 1}
# Test cases for HumanEval/152
# Generated using Claude API


def compare(game,guess):
    """I think we all remember that feeling when the result of some long-awaited
    event is finally known. The feelings and thoughts you have at that moment are
    definitely worth noting down and comparing.
    Your task is to determine if a person correctly guessed the results of a number of matches.
    You are given two arrays of scores and guesses of equal length, where each index shows a match. 
    Return an array of the same length denoting how far off each guess was. If they have guessed correctly,
    the value is 0, and if not, the value is the absolute difference between the guess and the score.
    
    
    example:

    compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) -> [0,0,0,0,3,3]
    compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) -> [4,4,1,0,0,6]
    """

    return [abs(x-y) for x,y in zip(game,guess)]


# Generated test cases:
import pytest

def test_compare_equal_lists():
    assert compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

def test_compare_different_lists():
    assert compare([5, 10, 15], [3, 8, 12]) == [2, 2, 3]

def test_compare_negative_numbers():
    assert compare([-1, -5, -10], [-3, -2, -7]) == [2, 3, 3]

def test_compare_mixed_numbers():
    assert compare([1, -2, 3], [4, -5, 6]) == [3, 3, 3]

def test_compare_single_element_lists():
    assert compare([5], [8]) == [3]

def test_compare_zero_lists():
    assert compare([0, 0, 0], [0, 0, 0]) == [0, 0, 0]

@pytest.mark.parametrize("game,guess,expected", [
    ([1, 2, 3], [1, 2, 3], [0, 0, 0]),
    ([5, 10, 15], [3, 8, 12], [2, 2, 3]),
    ([-1, -5, -10], [-3, -2, -7], [2, 3, 3]),
    ([1, -2, 3], [4, -5, 6], [3, 3, 3])
])
def test_compare_parametrized(game, guess, expected):
    assert compare(game, guess) == expected

def test_compare_empty_lists():
    assert compare([], []) == []

def test_compare_unequal_length_lists():
    with pytest.raises(ValueError):
        compare([1, 2], [1, 2, 3])
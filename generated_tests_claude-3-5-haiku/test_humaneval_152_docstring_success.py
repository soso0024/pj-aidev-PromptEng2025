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

def compare(game, guess):
    if len(game) != len(guess):
        raise ValueError("Input lists must have equal length")
    return [abs(x-y) for x,y in zip(game,guess)]

def test_compare_normal_case():
    assert compare([1,2,3,4,5,1], [1,2,3,4,2,-2]) == [0,0,0,0,3,3]
    assert compare([0,5,0,0,0,4], [4,1,1,0,0,-2]) == [4,4,1,0,0,6]

def test_compare_all_zeros():
    assert compare([0,0,0], [0,0,0]) == [0,0,0]

def test_compare_negative_numbers():
    assert compare([-1,-2,-3], [-1,-5,-3]) == [0,3,0]

def test_compare_mixed_numbers():
    assert compare([10,20,30,40], [5,25,35,45]) == [5,5,5,5]

def test_compare_single_element():
    assert compare([5], [5]) == [0]
    assert compare([5], [10]) == [5]

def test_compare_empty_list():
    assert compare([], []) == []

@pytest.mark.parametrize("game,guess,expected", [
    ([1,2,3], [1,2,3], [0,0,0]),
    ([0,0,0], [1,1,1], [1,1,1]),
    ([-5,5,0], [-5,5,1], [0,0,1])
])
def test_compare_parametrized(game, guess, expected):
    assert compare(game, guess) == expected

def test_compare_unequal_lengths():
    with pytest.raises(ValueError):
        compare([1,2,3], [1,2])
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

@pytest.mark.parametrize("game,guess,expected", [
    ([1, 2, 3], [1, 2, 3], [0, 0, 0]),
    ([1, 2, 3], [4, 5, 6], [3, 3, 3]),
    ([1, 2, 3], [1, 3, 2], [0, 1, 1]),
    ([1, 2, 3], [3, 2, 1], [2, 0, 2]),
    ([0, 0, 0], [0, 0, 0], [0, 0, 0]),
    ([0, 0, 0], [1, 1, 1], [1, 1, 1]),
    ([10, 20, 30], [20, 30, 10], [10, 10, 20]),
    ([100, 200, 300], [300, 200, 100], [200, 0, 200]),
    ([], [], []),
    ([1], [1], [0]),
    ([1], [2], [1]),
    ([1, 2], [2, 1], [1, 1]),
    ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [4, 2, 0, 2, 4]),
])
def test_compare(game, guess, expected):
    assert compare(game, guess) == expected

def compare(game, guess):
    return [abs(x-y) for x, y in zip(game, guess)]

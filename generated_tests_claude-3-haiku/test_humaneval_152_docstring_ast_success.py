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

def test_compare_equal_lengths():
    game = [1, 2, 3, 4, 5, 1]
    guess = [1, 2, 3, 4, 2, -2]
    assert compare(game, guess) == [0, 0, 0, 0, 3, 3]

def test_compare_different_lengths():
    game = [0, 5, 0, 0, 0, 4]
    guess = [4, 1, 1, 0, 0]
    with pytest.raises(ValueError):
        compare(game, guess)

@pytest.mark.parametrize("game,guess,expected", [
    ([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2], [4, 4, 1, 0, 0, 6]),
    ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]),
    ([0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]),
    ([10, 20, 30, 40, 50], [9, 19, 29, 39, 51], [1, 1, 1, 1, 1]),
    ([100, 200, 300, 400, 500], [100, 200, 300, 400, 500], [0, 0, 0, 0, 0])
])
def test_compare_various_cases(game, guess, expected):
    assert compare(game, guess) == expected

def compare(game, guess):
    if len(game) != len(guess):
        raise ValueError("Game and guess arrays must be of equal length")
    return [abs(x - y) for x, y in zip(game, guess)]

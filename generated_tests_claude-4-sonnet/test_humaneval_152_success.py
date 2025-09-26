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

def compare(game,guess):
    return [abs(x-y) for x,y in zip(game,guess)]

def test_compare_equal_lists():
    assert compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

def test_compare_different_lists():
    assert compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

def test_compare_mixed_differences():
    assert compare([1, 5, 3], [2, 3, 7]) == [1, 2, 4]

def test_compare_negative_numbers():
    assert compare([-1, -2, -3], [1, 2, 3]) == [2, 4, 6]

def test_compare_negative_and_positive():
    assert compare([-5, 0, 5], [5, 0, -5]) == [10, 0, 10]

def test_compare_single_element():
    assert compare([5], [3]) == [2]

def test_compare_empty_lists():
    assert compare([], []) == []

def test_compare_floats():
    result = compare([1.5, 2.7], [1.2, 3.1])
    assert abs(result[0] - 0.3) < 1e-10
    assert abs(result[1] - 0.4) < 1e-10

def test_compare_zero_values():
    assert compare([0, 0, 0], [1, -1, 0]) == [1, 1, 0]

def test_compare_large_numbers():
    assert compare([1000, 2000], [1500, 1800]) == [500, 200]

@pytest.mark.parametrize("game,guess,expected", [
    ([1, 2], [3, 4], [2, 2]),
    ([10, 20, 30], [15, 25, 35], [5, 5, 5]),
    ([0], [10], [10]),
    ([-10, -20], [-5, -25], [5, 5])
])
def test_compare_parametrized(game, guess, expected):
    assert compare(game, guess) == expected

def test_compare_different_lengths_shorter_game():
    assert compare([1, 2], [1, 2, 3]) == [0, 0]

def test_compare_different_lengths_shorter_guess():
    assert compare([1, 2, 3], [1, 2]) == [0, 0]

def test_compare_with_type_error():
    with pytest.raises(TypeError):
        compare("abc", [1, 2, 3])

def test_compare_with_none_values():
    with pytest.raises(TypeError):
        compare([None, 1], [1, 2])
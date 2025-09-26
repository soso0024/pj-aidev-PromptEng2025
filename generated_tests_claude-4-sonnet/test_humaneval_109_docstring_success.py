# Test cases for HumanEval/109
# Generated using Claude API


def move_one_ball(arr):
    """We have an array 'arr' of N integers arr[1], arr[2], ..., arr[N].The
    numbers in the array will be randomly ordered. Your task is to determine if
    it is possible to get an array sorted in non-decreasing order by performing 
    the following operation on the given array:
        You are allowed to perform right shift operation any number of times.
    
    One right shift operation means shifting all elements of the array by one
    position in the right direction. The last element of the array will be moved to
    the starting position in the array i.e. 0th index. 

    If it is possible to obtain the sorted array by performing the above operation
    then return True else return False.
    If the given array is empty then return True.

    Note: The given list is guaranteed to have unique elements.

    For Example:
    
    move_one_ball([3, 4, 5, 1, 2])==>True
    Explanation: By performin 2 right shift operations, non-decreasing order can
                 be achieved for the given array.
    move_one_ball([3, 5, 4, 1, 2])==>False
    Explanation:It is not possible to get non-decreasing order for the given
                array by performing any number of right shift operations.
                
    """

    if len(arr)==0:
      return True
    sorted_array=sorted(arr)
    my_arr=[]
    
    min_value=min(arr)
    min_index=arr.index(min_value)
    my_arr=arr[min_index:]+arr[0:min_index]
    for i in range(len(arr)):
      if my_arr[i]!=sorted_array[i]:
        return False
    return True


# Generated test cases:
import pytest

def move_one_ball(arr):
    if len(arr)==0:
      return True
    sorted_array=sorted(arr)
    my_arr=[]
    
    min_value=min(arr)
    min_index=arr.index(min_value)
    my_arr=arr[min_index:]+arr[0:min_index]
    for i in range(len(arr)):
      if my_arr[i]!=sorted_array[i]:
        return False
    return True

@pytest.mark.parametrize("arr,expected", [
    ([], True),
    ([1], True),
    ([1, 2], True),
    ([2, 1], True),
    ([3, 4, 5, 1, 2], True),
    ([3, 5, 4, 1, 2], False),
    ([1, 2, 3, 4, 5], True),
    ([5, 1, 2, 3, 4], True),
    ([4, 5, 1, 2, 3], True),
    ([3, 4, 5, 1, 2], True),
    ([2, 3, 4, 5, 1], True),
    ([1, 3, 2, 4, 5], False),
    ([5, 4, 3, 2, 1], False),
    ([2, 1, 4, 3, 5], False),
    ([1, 2, 3, 5, 4], False),
    ([10, 20, 30, 5], True),
    ([10, 30, 20, 5], False),
    ([100], True),
    ([50, 100], True),
    ([100, 50], True),
    ([-1, 0, 1], True),
    ([0, 1, -1], True),
    ([1, -1, 0], True),
    ([-1, 1, 0], False),
    ([0, -1, 1], False),
    ([1, 0, -1], False),
    ([7, 8, 9, 1, 2, 3, 4, 5, 6], True),
    ([7, 8, 9, 1, 2, 3, 5, 4, 6], False),
    ([2, 3, 1], True),
    ([3, 1, 2], True),
    ([1, 3, 2], False)
])
def test_move_one_ball(arr, expected):
    assert move_one_ball(arr) == expected

def test_move_one_ball_empty_array():
    assert move_one_ball([]) == True

def test_move_one_ball_single_element():
    assert move_one_ball([42]) == True

def test_move_one_ball_already_sorted():
    assert move_one_ball([1, 2, 3, 4, 5]) == True

def test_move_one_ball_reverse_sorted():
    assert move_one_ball([5, 4, 3, 2, 1]) == False

def test_move_one_ball_rotated_sorted():
    assert move_one_ball([4, 5, 1, 2, 3]) == True

def test_move_one_ball_not_rotatable():
    assert move_one_ball([1, 3, 2, 4, 5]) == False

def test_move_one_ball_negative_numbers():
    assert move_one_ball([-3, -2, -1, -5, -4]) == True

def test_move_one_ball_mixed_numbers():
    assert move_one_ball([0, 1, 2, -2, -1]) == True

def test_move_one_ball_large_numbers():
    assert move_one_ball([1000, 2000, 3000, 100, 200, 300]) == True

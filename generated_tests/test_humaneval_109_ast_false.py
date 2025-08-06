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

def test_empty_array():
    assert move_one_ball([]) == True

def test_single_element():
    assert move_one_ball([1]) == True

def test_already_sorted():
    assert move_one_ball([1, 2, 3, 4]) == True

def test_can_be_sorted_with_one_move():
    assert move_one_ball([3, 4, 5, 1, 2]) == True

def test_cannot_be_sorted():
    assert move_one_ball([1, 2, 4, 3]) == False

@pytest.mark.parametrize("input_arr,expected", [
    ([1, 2, 3], True),
    ([2, 3, 1], True),
    ([3, 1, 2], True),
    ([4, 1, 2, 3], True),
    ([2, 3, 4, 1], True),
    ([3, 4, 1, 2], True),
    ([1, 3, 2, 4], False),
    ([2, 1, 4, 3], False),
    ([1], True),
    ([], True),
    ([5, 4, 3, 2, 1], False),
    ([2, 1], True)
])
def test_various_arrays(input_arr, expected):
    assert move_one_ball(input_arr) == expected

def test_duplicate_elements():
    result = move_one_ball([2, 2, 1, 1])
    assert result == False

def test_negative_numbers():
    assert move_one_ball([-3, -2, -1]) == True
    assert move_one_ball([-1, -3, -2]) == True
    assert move_one_ball([-2, -3, -1]) == False

def test_large_numbers():
    assert move_one_ball([1000, 1001, 999]) == True
    assert move_one_ball([999, 1001, 1000]) == False

def test_mixed_numbers():
    assert move_one_ball([-1, 0, 1]) == True
    assert move_one_ball([0, 1, -1]) == True
    assert move_one_ball([1, -1, 0]) == True
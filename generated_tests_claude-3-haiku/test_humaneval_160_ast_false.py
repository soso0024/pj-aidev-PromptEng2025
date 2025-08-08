# Test cases for HumanEval/160
# Generated using Claude API


def do_algebra(operator, operand):
    """
    Given two lists operator, and operand. The first list has basic algebra operations, and 
    the second list is a list of integers. Use the two given lists to build the algebric 
    expression and return the evaluation of this expression.

    The basic algebra operations:
    Addition ( + ) 
    Subtraction ( - ) 
    Multiplication ( * ) 
    Floor division ( // ) 
    Exponentiation ( ** ) 

    Example:
    operator['+', '*', '-']
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9

    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.

    """

    expression = str(operand[0])
    for oprt, oprn in zip(operator, operand[1:]):
        expression+= oprt + str(oprn)
    return eval(expression)


# Generated test cases:
import pytest

def test_do_algebra_addition():
    assert do_algebra(['+'], [2, 3]) == 5
    assert do_algebra(['+'], [10, 5, 2]) == 17

def test_do_algebra_subtraction():
    assert do_algebra(['-'], [10, 3]) == 7
    assert do_algebra(['-'], [20, 5, 2]) == 13

def test_do_algebra_multiplication():
    assert do_algebra(['*'], [2, 3]) == 6
    assert do_algebra(['*'], [4, 5, 2]) == 40

def test_do_algebra_division():
    assert do_algebra(['//'], [100, 5, 2]) == 10
    assert do_algebra(['//'], [50, 5, 2]) == 5

def test_do_algebra_mixed_operations():
    assert do_algebra(['+', '-', '*'], [10, 3, 4, 2]) == 16
    assert do_algebra(['-', '*', '//'], [20, 5, 4, 2]) == 2

def test_do_algebra_empty_input():
    with pytest.raises(IndexError):
        do_algebra([], [])

def test_do_algebra_mismatched_input():
    with pytest.raises(IndexError):
        do_algebra(['+', '-'], [10])

def test_do_algebra_invalid_operator():
    with pytest.raises(SyntaxError):
        do_algebra(['%'], [10, 3])
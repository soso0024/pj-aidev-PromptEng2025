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

def do_algebra(operator, operand):
    expression = str(operand[0])
    for oprt, oprn in zip(operator, operand[1:]):
        expression += oprt + str(oprn)
    return eval(expression)

def test_do_algebra_basic():
    operator = ['+', '*', '-']
    operand = [2, 3, 4, 5]
    assert do_algebra(operator, operand) == 9

def test_do_algebra_empty_operator():
    operator = []
    operand = [2, 3, 4, 5]
    with pytest.raises(IndexError):
        do_algebra(operator, operand)

def test_do_algebra_empty_operand():
    operator = ['+', '*', '-']
    operand = []
    with pytest.raises(IndexError):
        do_algebra(operator, operand)

def test_do_algebra_single_operand():
    operator = ['+']
    operand = [5]
    assert do_algebra(operator, operand) == 5

def test_do_algebra_negative_operands():
    operator = ['-', '*']
    operand = [-2, 3, -4]
    assert do_algebra(operator, operand) == -6

def test_do_algebra_zero_operands():
    operator = ['+', '//', '**']
    operand = [0, 2, 3]
    assert do_algebra(operator, operand) == 0

def test_do_algebra_division_by_zero():
    operator = ['//', '+']
    operand = [2, 0]
    with pytest.raises(ZeroDivisionError):
        do_algebra(operator, operand)

def test_do_algebra_invalid_operator():
    operator = ['+', '%', '-']
    operand = [2, 3, 4, 5]
    with pytest.raises(SyntaxError):
        do_algebra(operator, operand)

def test_do_algebra_different_lengths():
    operator = ['+', '*', '-', '/']
    operand = [2, 3, 4]
    with pytest.raises(IndexError):
        do_algebra(operator, operand)
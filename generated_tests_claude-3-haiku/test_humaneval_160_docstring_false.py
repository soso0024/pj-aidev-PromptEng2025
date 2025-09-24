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
    operator = ['-', '*', '//', '//']
    operand = [-2, 3, -4, 2]
    assert do_algebra(operator, operand) == -8

def test_do_algebra_zero_division():
    operator = ['//', '**']
    operand = [4, 0]
    with pytest.raises(ZeroDivisionError):
        do_algebra(operator, operand)

def test_do_algebra_float_operands():
    operator = ['+', '*', '-']
    operand = [2.5, 3.2, 4.1, 5.0]
    assert round(do_algebra(operator, operand), 1) == 9.8

def test_do_algebra_large_numbers():
    operator = ['+', '**', '-']
    operand = [1000000, 2, 1000000]
    assert do_algebra(operator, operand) == 1000002

def test_do_algebra_operator_mismatch():
    operator = ['+', '*', '-']
    operand = [2, 3, 4, 5]
    with pytest.raises(IndexError):
        do_algebra(operator, operand)
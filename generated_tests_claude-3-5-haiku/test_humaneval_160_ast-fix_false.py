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
from typing import List, Union

def do_algebra(operator: List[str], operand: List[Union[int, float]]):
    if not operator:
        return operand[0]
    
    result = operand[0]
    for oprt, oprn in zip(operator, operand[1:]):
        if oprt == '+':
            result += oprn
        elif oprt == '-':
            result -= oprn
        elif oprt == '*':
            result *= oprn
        elif oprt == '//':
            result //= oprn
        elif oprt == '**':
            result **= oprn
    
    return result

def test_do_algebra_basic():
    assert do_algebra(['+'], [1, 2]) == 3
    assert do_algebra(['-'], [5, 3]) == 2
    assert do_algebra(['*'], [3, 4]) == 12
    assert do_algebra(['//'], [10, 3]) == 3
    assert do_algebra(['**'], [2, 3]) == 8

def test_do_algebra_multiple_operations():
    assert do_algebra(['+', '*'], [1, 2, 3]) == 7
    assert do_algebra(['-', '+'], [10, 3, 2]) == 11
    assert do_algebra(['*', '//'], [4, 3, 2]) == 2
    assert do_algebra(['+', '**'], [2, 3, 2]) == 11

def test_do_algebra_edge_cases():
    assert do_algebra(['+'], [5]) == 5
    assert do_algebra(['**', '+'], [2, 3, 1]) == 10
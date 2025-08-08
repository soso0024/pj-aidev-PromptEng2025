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
    for i, oprt in enumerate(operator):
        if oprt == '+':
            result += operand[i+1]
        elif oprt == '-':
            result -= operand[i+1]
        elif oprt == '*':
            result *= operand[i+1]
        elif oprt == '/':
            result /= operand[i+1]
        elif oprt == '//':
            result //= operand[i+1]
        elif oprt == '**':
            result **= operand[i+1]
    
    return result

def test_do_algebra_basic_addition():
    assert do_algebra(['+'], [1, 2]) == 3
    assert do_algebra(['+'], [5, 3]) == 8

def test_do_algebra_multiple_operations():
    assert do_algebra(['+', '*'], [1, 2, 3]) == 7
    assert do_algebra(['-', '+'], [10, 5, 3]) == 12

def test_do_algebra_complex_operations():
    assert do_algebra(['+', '*', '-'], [1, 2, 3, 4]) == -5
    assert do_algebra(['*', '+', '-'], [2, 3, 4, 5]) == 11

def test_do_algebra_floating_point():
    assert do_algebra(['+'], [1.5, 2.5]) == 4.0
    assert do_algebra(['*'], [2.5, 3.0]) == 7.5

def test_do_algebra_negative_numbers():
    assert do_algebra(['+'], [-1, 2]) == 1
    assert do_algebra(['-'], [10, -5]) == 15

@pytest.mark.parametrize("operators,operands,expected", [
    (['+'], [0, 0], 0),
    (['-'], [100, 50], 50),
    (['*'], [5, 0], 0),
    (['*'], [0, 5], 0),
    (['**'], [2, 3], 8),
    (['//'], [10, 3], 3)
])
def test_do_algebra_parametrized(operators, operands, expected):
    assert do_algebra(operators, operands) == expected

def test_do_algebra_single_operand():
    assert do_algebra([], [42]) == 42

def test_do_algebra_division():
    assert do_algebra(['/'], [10, 2]) == 5.0
    assert do_algebra(['/'], [15, 3]) == 5.0

def test_do_algebra_mixed_operations():
    assert do_algebra(['+', '*', '/'], [10, 2, 3, 2]) == 7.0
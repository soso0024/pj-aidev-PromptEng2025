# Test cases for HumanEval/81
# Generated using Claude API


def numerical_letter_grade(grades):
    """It is the last week of the semester and the teacher has to give the grades
    to students. The teacher has been making her own algorithm for grading.
    The only problem is, she has lost the code she used for grading.
    She has given you a list of GPAs for some students and you have to write 
    a function that can output a list of letter grades using the following table:
             GPA       |    Letter grade
              4.0                A+
            > 3.7                A 
            > 3.3                A- 
            > 3.0                B+
            > 2.7                B 
            > 2.3                B-
            > 2.0                C+
            > 1.7                C
            > 1.3                C-
            > 1.0                D+ 
            > 0.7                D 
            > 0.0                D-
              0.0                E
    

    Example:
    grade_equation([4.0, 3, 1.7, 2, 3.5]) ==> ['A+', 'B', 'C-', 'C', 'A-']
    """


   
    letter_grade = []
    for gpa in grades:
        if gpa == 4.0:
            letter_grade.append("A+")
        elif gpa > 3.7:
            letter_grade.append("A")
        elif gpa > 3.3:
            letter_grade.append("A-")
        elif gpa > 3.0:
            letter_grade.append("B+")
        elif gpa > 2.7:
            letter_grade.append("B")
        elif gpa > 2.3:
            letter_grade.append("B-")
        elif gpa > 2.0:
            letter_grade.append("C+")
        elif gpa > 1.7:
            letter_grade.append("C")
        elif gpa > 1.3:
            letter_grade.append("C-")
        elif gpa > 1.0:
            letter_grade.append("D+")
        elif gpa > 0.7:
            letter_grade.append("D")
        elif gpa > 0.0:
            letter_grade.append("D-")
        else:
            letter_grade.append("E")
    return letter_grade


# Generated test cases:
import pytest

def numerical_letter_grade(grades):
    letter_grade = []
    for gpa in grades:
        if gpa == 4.0:
            letter_grade.append("A+")
        elif gpa > 3.7:
            letter_grade.append("A")
        elif gpa > 3.3:
            letter_grade.append("A-")
        elif gpa > 3.0:
            letter_grade.append("B+")
        elif gpa > 2.7:
            letter_grade.append("B")
        elif gpa > 2.3:
            letter_grade.append("B-")
        elif gpa > 2.0:
            letter_grade.append("C+")
        elif gpa > 1.7:
            letter_grade.append("C")
        elif gpa > 1.3:
            letter_grade.append("C-")
        elif gpa > 1.0:
            letter_grade.append("D+")
        elif gpa > 0.7:
            letter_grade.append("D")
        elif gpa > 0.0:
            letter_grade.append("D-")
        else:
            letter_grade.append("E")
    return letter_grade

def test_numerical_letter_grade_all_a_plus():
    assert numerical_letter_grade([4.0, 4.0, 4.0]) == ['A+', 'A+', 'A+']

def test_numerical_letter_grade_all_a():
    assert numerical_letter_grade([3.8, 3.9, 4.0]) == ['A', 'A', 'A+']

def test_numerical_letter_grade_all_a_minus():
    assert numerical_letter_grade([3.4, 3.5, 3.6]) == ['A-', 'A-', 'A-']

def test_numerical_letter_grade_all_b_plus():
    assert numerical_letter_grade([3.1, 3.2, 3.3]) == ['B+', 'B+', 'B+']

def test_numerical_letter_grade_all_b():
    assert numerical_letter_grade([2.8, 2.9, 3.0]) == ['B', 'B', 'B']

def test_numerical_letter_grade_all_b_minus():
    assert numerical_letter_grade([2.4, 2.5, 2.6]) == ['B-', 'B-', 'B-']

def test_numerical_letter_grade_all_c_plus():
    assert numerical_letter_grade([2.1, 2.2, 2.3]) == ['C+', 'C+', 'C+']

def test_numerical_letter_grade_all_c():
    assert numerical_letter_grade([1.8, 1.9, 2.0]) == ['C', 'C', 'C']

def test_numerical_letter_grade_all_c_minus():
    assert numerical_letter_grade([1.4, 1.5, 1.6]) == ['C-', 'C-', 'C-']

def test_numerical_letter_grade_all_d_plus():
    assert numerical_letter_grade([1.1, 1.2, 1.3]) == ['D+', 'D+', 'D+']

def test_numerical_letter_grade_all_d():
    assert numerical_letter_grade([0.8, 0.9, 1.0]) == ['D', 'D', 'D']

def test_numerical_letter_grade_all_d_minus():
    assert numerical_letter_grade([0.1, 0.4, 0.7]) == ['D-', 'D-', 'D-']

def test_numerical_letter_grade_all_e():
    assert numerical_letter_grade([0.0, 0.0, 0.0]) == ['E', 'E', 'E']

def test_numerical_letter_grade_mixed_grades():
    assert numerical_letter_grade([4.0, 3.0, 1.7, 2.0, 3.5]) == ['A+', 'B', 'C-', 'C', 'A-']
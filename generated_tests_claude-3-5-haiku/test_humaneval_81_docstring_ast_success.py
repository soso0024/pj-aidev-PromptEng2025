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
        elif gpa >= 3.7:
            letter_grade.append("A")
        elif gpa >= 3.3:
            letter_grade.append("A-")
        elif gpa >= 3.0:
            letter_grade.append("B+")
        elif gpa >= 2.7:
            letter_grade.append("B")
        elif gpa >= 2.3:
            letter_grade.append("B-")
        elif gpa >= 2.0:
            letter_grade.append("C+")
        elif gpa >= 1.7:
            letter_grade.append("C")
        elif gpa >= 1.3:
            letter_grade.append("C-")
        elif gpa >= 1.0:
            letter_grade.append("D+")
        elif gpa >= 0.7:
            letter_grade.append("D")
        elif gpa > 0.0:
            letter_grade.append("D-")
        else:
            letter_grade.append("E")
    return letter_grade

def test_numerical_letter_grade_standard_cases():
    assert numerical_letter_grade([4.0, 3.8, 3.5, 3.2, 2.9]) == ['A+', 'A', 'A-', 'B+', 'B']

def test_numerical_letter_grade_edge_cases():
    assert numerical_letter_grade([4.0, 3.7, 3.3, 3.0, 2.7]) == ['A+', 'A', 'A-', 'B+', 'B']

def test_numerical_letter_grade_lower_bounds():
    assert numerical_letter_grade([2.3, 2.0, 1.7, 1.3, 1.0]) == ['B-', 'C+', 'C', 'C-', 'D+']

def test_numerical_letter_grade_zero_cases():
    assert numerical_letter_grade([0.0, 0.1, 0.5]) == ['E', 'D-', 'D-']

@pytest.mark.parametrize("input_grades,expected", [
    ([4.0, 3.8, 1.5, 0.5], ['A+', 'A', 'C-', 'D-']),
    ([3.9, 2.5, 1.2, 0.0], ['A', 'B-', 'D+', 'E'])
])
def test_numerical_letter_grade_mixed_cases(input_grades, expected):
    assert numerical_letter_grade(input_grades) == expected

def test_numerical_letter_grade_empty_list():
    assert numerical_letter_grade([]) == []

def test_numerical_letter_grade_single_values():
    assert numerical_letter_grade([4.0]) == ['A+']
    assert numerical_letter_grade([0.0]) == ['E']
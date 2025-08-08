# Test cases for HumanEval/124
# Generated using Claude API


def valid_date(date):
    """You have to write a function which validates a given date string and
    returns True if the date is valid otherwise False.
    The date is valid if all of the following rules are satisfied:
    1. The date string is not empty.
    2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2.
    3. The months should not be less than 1 or higher than 12.
    4. The date should be in the format: mm-dd-yyyy

    for example: 
    valid_date('03-11-2000') => True

    valid_date('15-01-2012') => False

    valid_date('04-0-2040') => False

    valid_date('06-04-2020') => True

    valid_date('06/04/2020') => False
    """

    try:
        date = date.strip()
        month, day, year = date.split('-')
        month, day, year = int(month), int(day), int(year)
        if month < 1 or month > 12:
            return False
        if month in [1,3,5,7,8,10,12] and day < 1 or day > 31:
            return False
        if month in [4,6,9,11] and day < 1 or day > 30:
            return False
        if month == 2 and day < 1 or day > 29:
            return False
    except:
        return False

    return True


# Generated test cases:
import pytest

def test_valid_date_normal_cases():
    assert valid_date('1-1-2023') == True
    assert valid_date('12-31-2022') == True
    assert valid_date('7-15-2024') == True

def test_valid_date_edge_cases():
    assert valid_date('1-31-2023') == True
    assert valid_date('12-1-2022') == True
    assert valid_date('2-29-2020') == True

def test_valid_date_invalid_months():
    assert valid_date('0-1-2023') == False
    assert valid_date('13-1-2023') == False

def test_valid_date_invalid_days():
    assert valid_date('1-0-2023') == False
    assert valid_date('1-32-2023') == False
    assert valid_date('2-30-2023') == False
    assert valid_date('4-31-2023') == False

def test_valid_date_invalid_formats():
    assert valid_date('1/1/2023') == False
    assert valid_date('2023-1-1') == False
    assert valid_date('abc') == False
    assert valid_date('') == False

@pytest.mark.parametrize("date,expected", [
    ('1-1-2023', True),
    ('12-31-2022', True),
    ('2-29-2020', True),
    ('0-1-2023', False),
    ('1-0-2023', False),
    ('1-32-2023', False),
    ('13-1-2023', False),
    ('1/1/2023', False),
    ('', False)
])
def test_valid_date_parametrized(date, expected):
    assert valid_date(date) == expected
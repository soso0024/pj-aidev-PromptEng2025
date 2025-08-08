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
from valid_date import valid_date
import pytest

@pytest.mark.parametrize("input,expected", [
    ('03-11-2000', True),
    ('15-01-2012', False),
    ('04-0-2040', False),
    ('06-04-2020', True),
    ('06/04/2020', False),
    ('', False),
    ('13-32-2022', False),
    ('02-29-2021', False),
    ('02-29-2020', True),
    ('11-31-2022', False),
    ('04-31-2022', False),
    ('06-31-2022', False),
    ('09-31-2022', False),
    ('12-32-2022', False),
    ('02-30-2022', False),
    ('02-28-2022', True),
    ('02-28-2023', True),
    ('02-29-2024', True),
    ('02-29-2025', False),
    ('00-04-2022', False),
    ('13-04-2022', False),
    ('04-00-2022', False),
    ('04-32-2022', False),
    ('04-04-0000', False),
    ('04-04-10000', False)
])
def test_valid_date(input, expected):
    assert valid_date(input) == expected
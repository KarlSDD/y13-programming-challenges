from task4_day_of_the_week import *


def test_valid_days():
    # Today
    assert day_of_the_week(3, 12, 2020) == "Thursday"

    # Leap day
    assert day_of_the_week(29, 2, 2020) == "Thursday"

    # Mr. Rigby's birthday
    assert day_of_the_week(22, 4, 1991) == "Monday"

    # Ms. O'Rourke's birthday
    assert day_of_the_week(17, 4, 1993) == "Saturday"

    # Last day of school
    assert day_of_the_week(18, 6, 2020) == "Friday"


def test_invalid_days():
    assert day_of_the_week(31, 9, 2020) == "Invalid"
    assert day_of_the_week(29, 2, 2021) == "Invalid"
    assert day_of_the_week(31, 11, 2020) == "Invalid"

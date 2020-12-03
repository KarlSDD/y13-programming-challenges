from task2_number_names import *


# Valid tests
def test_a():
    assert number_name(1) == "one"


def test_b():
    assert number_name(11) == "eleven"


def test_c():
    assert number_name(-77) == "negative seventy seven"


def test_d():
    assert number_name(1088) == "one thousand and eighty eight"


def test_e():
    assert number_name(4608) == "four thousand six hundred and eight"


def test_f():
    assert number_name(-60028) == "negative sixty thousand and twenty eight"


def test_g():
    assert number_name(500000) == "five hundred thousand"


def test_h():
    assert number_name(999999) == "nine hundred and ninety nine thousand nine hundred and ninety nine"


# Invalid tests
def test_i():
    assert number_name(True) == None


def test_j():
    assert number_name("one") == None


def test_k():
    assert number_name() == None

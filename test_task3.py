from task3_triangulate import *


def test_right():
    assert triangulate(5, 3, 4) == "right"


def test_equilateral():
    assert triangulate(4, 4, 4) == "equilateral"


def test_isosceles():
    assert triangulate(6, 3, 6) == "isosceles"


def test_scalene():
    assert triangulate(2, 4, 3) == "scalene"


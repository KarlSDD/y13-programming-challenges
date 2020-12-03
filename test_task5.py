from task5_letters_odd_even import *


def test_numbers_only():
    assert letters_odd_even([4, 2, 7, 6, 3]) == [3, 7, 2, 4, 6]


def test_letters_only():
    assert letters_odd_even(['e', 'c', 'd', 'b', 'a']) == ['a', 'b', 'c', 'd', 'e']


def test_letters_and_numbers():
    assert letters_odd_even([12, 17, 'a', 'h', 4, 1, 5, 'f', 8, 'z']) == ['a', 'f', 'h', 'z', 1, 5, 17, 4, 8, 12]

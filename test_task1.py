from task1_hacking_pin_number import *


# Valid data tests
def test_1_number():
    test_pin = "0000"
    hacking_attempts = len(pin_sequence_finder(test_pin))
    assert hacking_attempts == 1


def test_2_number_v1():
    test_pin = "1114"
    hacking_attempts = len(pin_sequence_finder(test_pin))
    assert hacking_attempts == 4


def test_2_number_v2():
    test_pin = "2332"
    hacking_attempts = len(pin_sequence_finder(test_pin))
    assert hacking_attempts == 6


def test_3_number():
    test_pin = "4540"
    hacking_attempts = len(pin_sequence_finder(test_pin))
    assert hacking_attempts == 12


def test_4_number():
    test_pin = "8594"
    hacking_attempts = len(pin_sequence_finder(test_pin))
    assert hacking_attempts == 24


# Invalid data tests
def test_0_number():
    test_pin = ""
    hacking_attempts = pin_sequence_finder(test_pin)
    assert hacking_attempts == -1


def test_letters():
    test_pin = "abcd"
    hacking_attempts = pin_sequence_finder(test_pin)
    assert hacking_attempts == -1

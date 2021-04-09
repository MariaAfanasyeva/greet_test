import pytest
from greet import greet


@pytest.mark.parametrize("test_input, expected", [("Vasya", "Hello, Vasya"), (54, "Wrong input"), (3.5, "Wrong input")])
def test_greet(test_input, expected):
    assert greet(test_input) == expected


def test_empty_greet():
    assert greet() == "Hello, my friend"


def test_isupper():
    assert greet("HARRY") == "HELLO, HARRY"


@pytest.mark.parametrize("expected, test_input1, test_input2", [("Hello, John and Any", "John", "Any"), ("Wrong input",
                                                                                                         "John", 4)])
def test_two_names(expected, test_input1, test_input2):
    assert greet(test_input1, test_input2) == expected

import pytest
from greet import greet


@pytest.mark.parametrize("test_input, expected", [("Vasya", "Hello, Vasya"), (54, "Wrong input"), (3.5, "Wrong input")])
def test_greet(test_input, expected):
    assert greet(test_input) == expected


def test_empty_greet():
    assert greet() == "Hello, my friend"


def test_isupper():
    assert greet("HARRY") == "HELLO, HARRY"


import pytest
from greet import greet


def test_greet():
    assert greet("Vasya") == "Hello, Vasya"
    assert greet(54) == "Wrong input"
    assert greet(3.5) == "Wrong input"


def test_empty_greet():
    assert greet() == "Hello, my friend"


def test_isupper():
    assert greet("HARRY") == "HELLO, HARRY"


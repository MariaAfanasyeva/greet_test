import pytest
from greet import greet


def test_greet():
    assert greet("Vasya") == "Hello, Vasya"


def test_empty_greet():
    assert greet() == "Hello, my friend"


def test_isupper():
    assert greet("HARRY") == "HELLO, HARRY"


def test_two_names():
    assert greet('John', 'Any') == "Hello, John and Any"
    assert greet('John', 4) == "Wrong input"
    assert greet(5) == "Wrong input"


import pytest
from req1 import greet


def test_greet():
    assert greet("Vasya") == "Hello, Vasya"



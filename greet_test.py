import pytest
from greet import greet


def test_greet():
    assert greet("Vasya") == "Hello, Vasya."


@pytest.mark.parametrize("inp1, inp2, exception", [("John", 4, ValueError), (4, 5, ValueError)])
def test_wrong_input(inp1, inp2, exception):
    with pytest.raises(exception):
        greet(inp1, inp2)


def test_empty_greet():
    assert greet() == "Hello, my friend"


def test_isupper():
    assert greet("HARRY") == "HELLO, HARRY!"


def test_two_names():
    assert greet('John', 'Any') == "Hello, John and Any."


@pytest.mark.parametrize("inp1, inp2, inp3, expected", [("John", "Mary", "James", "Hello, John, Mary and James."),
                                                        ("JOHN", "Mary", "James", "Hello, Mary and James.AND HELLO, JOHN!"),
                                                        ("JOHN", "MARY", "James", "Hello, James.AND HELLO, JOHN AND MARY!"),
                                                        ("John", "Mary", "James", "Hello, John, Mary and James.")])
def test_three_names(inp1, inp2, inp3, expected):
    assert greet(inp1, inp2, inp3) == expected


@pytest.mark.parametrize("inp1, inp2, inp3, inp4, expected", [("John", "Mary", "Rudolf", "Greg",
                                                               "Hello, John, Mary, Rudolf and Greg.")])
def test_four_names(inp1, inp2, inp3, inp4, expected):
    assert greet(inp1, inp2, inp3, inp4) == expected




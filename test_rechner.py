import pytest
from rechner import addiere, subtrahiere, multipliziere, dividiere


def test_addiere():
    assert addiere(2, 3) == 5
    assert addiere(-1, 1) == 0
    assert addiere(0, 0) == 0


def test_subtrahiere():
    assert subtrahiere(5, 3) == 2
    assert subtrahiere(0, 5) == -5


def test_multipliziere():
    assert multipliziere(3, 4) == 12
    assert multipliziere(-2, 5) == -10
    assert multipliziere(0, 100) == 0


def test_dividiere():
    assert dividiere(10, 2) == 5.0
    assert dividiere(7, 2) == 3.5


def test_dividiere_durch_null():
    with pytest.raises(ValueError, match="Division durch Null ist nicht erlaubt"):
        dividiere(5, 0)

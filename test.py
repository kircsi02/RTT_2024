import pytest
from haromszog import HaromszogSzamitasok

def test_jo_haromszog():
    assert HaromszogSzamitasok(3, 4, 5) == 6

def test_nem_jo_haromszog():
    with pytest.raises(ValueError):
        HaromszogSzamitasok(1, 2, 10)
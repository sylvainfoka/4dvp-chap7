# ./tests/test_temperature.py
from temperature import __version__, celsius_to_farenheit, farenheit_to_celsius


def test_version():
    assert __version__ == "0.1.0"


def test_celsius_to_farenheit():
    assert celsius_to_farenheit(10) == 50


def test_farenheit_to_celius():
    assert farenheit_to_celsius(100) == 37.78

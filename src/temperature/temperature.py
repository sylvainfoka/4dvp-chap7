# ./src/temperature/temperature.py


def celsius_to_farenheit(celsius: float) -> float:
    return round(celsius * 1.8 + 32, 2)


def farenheit_to_celsius(farenheit: float) -> float:
    return round((farenheit - 32) / 1.8, 2)

import pandas as pd

df = pd.read_csv("data/weather.csv")


def test_columns_exist():
    expected = [
        "Time",
        "Temperature",
        "Humidity",
        "WindSpeed"
    ]
    assert list(df.columns) == expected


def test_temperature_not_null():
    assert df["Temperature"].notnull().all()


def test_humidity_range():
    assert df["Humidity"].between(0, 100).all()
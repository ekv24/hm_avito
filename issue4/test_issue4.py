from one_hot_encoder import fit_transform
import pytest


def test_common():
    cities = ["Moscow", "New York", "Moscow", "London"]
    exp_transformed_cities = [
        ("Moscow", [0, 0, 1]),
        ("New York", [0, 1, 0]),
        ("Moscow", [0, 0, 1]),
        ("London", [1, 0, 0]),
    ]
    transformed_cities = fit_transform(cities)
    assert exp_transformed_cities == transformed_cities


def test_many():
    cities = [
        "New York",
        "London",
        "Paris",
        "Tokyo",
        "Sydney",
        "Los Angeles",
        "Rome",
        "Berlin",
        "Moscow",
        "Beijing",
    ]
    exp_transformed_cities = [
        ("New York", [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]),
        ("London", [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]),
        ("Paris", [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]),
        ("Tokyo", [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]),
        ("Sydney", [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]),
        ("Los Angeles", [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]),
        ("Rome", [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]),
        ("Berlin", [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]),
        ("Moscow", [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]),
        ("Beijing", [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    ]
    transformed_cities = fit_transform(cities)
    assert exp_transformed_cities == transformed_cities


def test_empty():
    with pytest.raises(TypeError):
        fit_transform()


def test_two_city():
    cities = ["Moscow", "Moscow"]
    exp_transformed_cities = [("Moscow", [1]), ("Moscow", [1])]
    transformed_cities = fit_transform(cities)
    assert exp_transformed_cities == transformed_cities

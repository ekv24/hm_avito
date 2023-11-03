from one_hot_encoder import fit_transform
import unittest


class TestOHE(unittest.TestCase):
    def test_common(self):
        cities = ["Moscow", "New York", "Moscow", "London"]
        exp_transformed_cities = [
            ("Moscow", [0, 0, 1]),
            ("New York", [0, 1, 0]),
            ("Moscow", [0, 0, 1]),
            ("London", [1, 0, 0]),
        ]
        transformed_cities = fit_transform(cities)
        self.assertEqual(exp_transformed_cities, transformed_cities)

    def test_many(self):
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
        exp_element = ("Sydney", [0, 0, 0, 0, 0, 1, 0, 0, 0, 0])
        transformed_cities = fit_transform(cities)
        self.assertIn(exp_element, transformed_cities)

    def test_empty(self):
        with self.assertRaises(TypeError):
            fit_transform()

    def test_two_city(self):
        cities = ["Moscow", "Moscow"]
        exp_transformed_cities = [("Moscow", [1]), ("Moscow", [1])]
        transformed_cities = fit_transform(cities)
        self.assertEqual(exp_transformed_cities, transformed_cities)

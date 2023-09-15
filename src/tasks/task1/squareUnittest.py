import unittest
from .squareCounter import _countCircle, _countTriangle, countSquare


class TestGeometryFunctions(unittest.TestCase):

    def test_circle_area(self):
        # Проверяем вычисление площади круга
        radius = 5.0
        expected_area = 78.53981633974483
        self.assertAlmostEqual(_countCircle(radius), expected_area, places=5)

    def test_triangle_area(self):
        # Проверяем вычисление площади треугольника
        sides = (3, 4, 5)
        expected_area = 6.0
        self.assertAlmostEqual(_countTriangle(*sides), expected_area, places=5)

    def test_no_arguments(self):
        # Проверяем на ошибку без аргументов
        with self.assertRaises(ValueError):
            countSquare()

    def test_six_arguments(self):
        # Проверяем на ошибку с большим количеством аргументов
        with self.assertRaises(ValueError):
            countSquare(1, 2, 3, 4, 5, 6)

    def test_invalid_triangle(self):
        # Проверяем на ошибку с невалидным треугольником
        sides = (1, 2, 3)
        with self.assertRaises(ValueError):
            _countTriangle(*sides)
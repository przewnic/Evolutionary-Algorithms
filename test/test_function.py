"""
Project: Evolutionary Algorithm + Island Model
Authors: przewnic
Date: 12.2020
"""
import unittest
from Function_eval import Function_eval


class TestFunction(unittest.TestCase):
    def test_get_params(self):
        fun = Function_eval((0, 1), 2, "x", "f")
        self.assertEqual(fun.get_params(), (0, 1, 2))

    def test_get_y_value(self):
        fun = Function_eval((0, 1), 2, "x+x", "f")
        self.assertEqual(fun.get_y_value(2), 4)

        fun = Function_eval((0, 1), 2, "x[0]+x[1]", "f")
        self.assertEqual(fun.get_y_value([2, 3]), 5)

        fun = Function_eval((0, 1), 2, "x[0]**2 + x[1]", "f")
        self.assertEqual(fun.get_y_value([1, 2]), 3)

    def test_get_function(self):
        fun = Function_eval((0, 1), 2, "x+x", "f")
        self.assertEqual(fun.get_function(), fun.get_y_value)

    def test_replace_function(self):
        fun = Function_eval((0, 1), 2, "x+x", "f")
        new_function = "x**2"
        fun.replace_function(new_function)
        self.assertEqual(fun.function, "x**2", "f")
        self.assertEqual(fun.y(3), 9)
        self.assertEqual(fun.y(4), 16)


if __name__ == '__main__':
    unittest.main()

"""
Project: Evolutionary Algorithm + Island Model
Authors: przewnic
Date: 12.2020
"""
import unittest
from Individual import Individual


class TestIndvidual(unittest.TestCase):
    def test_set_values(self):
        individual = Individual(values=[1, 2, 3])
        individual.set_values([1, 1, 1])
        self.assertEqual(individual.values, [1, 1, 1])

    def test_get_values(self):
        individual = Individual(values=[1, 2, 3])
        self.assertEqual(individual.values, [1, 2, 3])


if __name__ == '__main__':
    unittest.main()

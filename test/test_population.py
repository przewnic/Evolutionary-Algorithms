"""
Project: Evolutionary Algorithm + Island Model
Authors: przewnic
Date: 12.2020
"""
import unittest
from Population import Population


class TestPopulation(unittest.TestCase):
    def test_get_random_individual(self):
        population = Population(individuals=[1])
        self.assertEqual(population.get_random_individual(), 1)

    def test_replace(self):
        population = Population(individuals=[1])
        population.replace([1, 2, 3])
        self.assertEqual(population.individuals, [1, 2, 3])

    def test_get_population_size(self):
        population = Population(individuals=[1])
        self.assertEqual(population.get_population_size(), 1)


if __name__ == '__main__':
    unittest.main()

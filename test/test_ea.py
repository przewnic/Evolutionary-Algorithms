"""
Project: Evolutionary Algorithm + Island Model
Authors: przewnic
Date: 12.2020
"""
import unittest
from Function_eval import Function_eval
from Population import Population
from Individual import Individual
from EA import EA


class TestEA(unittest.TestCase):
    def test_set_nr_of_steps(self):
        fun = Function_eval((0, 1), 2, "x", "f")
        ea = EA(fun)
        ea.set_nr_of_steps(13)
        self.assertEqual(ea.nr_of_steps, 13)

    def test_initialize_population(self):
        fun = Function_eval((0, 1), 2, "x", "f")
        ea = EA(fun)
        ea.initialize_population(population_size=10)
        self.assertIsInstance(ea.population, Population)
        self.assertEqual(len(ea.population.individuals), 10)

    def test_count_fitness(self):
        fun = Function_eval((0, 1), 2, "x", "f")
        ea = EA(fun)
        ea.initialize_population(population_size=5)
        ea.count_fitness(ea.population)
        for individual in ea.population.individuals:
            self.assertIsNotNone(individual.fitness)

    def test_sort_by_fitness(self):
        # Test designed to check if sorted in ascending order
        fun = Function_eval((0, 100), 1, "x", "f")
        i1 = Individual([5])
        i2 = Individual([10])
        i3 = Individual([15])
        p1 = Population(individuals=[i1, i2, i3])
        ea = EA(fun, p1)
        ea.count_fitness(ea.population)
        ea.sort_by_fitness(ea.population)
        self.assertEqual(ea.population.individuals, [i1, i2, i3])

    def test_check_better_individual_index(self):
        fun = Function_eval((0, 100), 1, "x", "f")
        i1 = Individual([15])
        i2 = Individual([10])
        i3 = Individual([5])
        p1 = Population(individuals=[i1, i2, i3])
        ea = EA(fun, p1)
        ea.count_fitness(ea.population)
        self.assertFalse(ea.check_better_individual_index(0, 1, ea.population))
        self.assertFalse(ea.check_better_individual_index(0, 2, ea.population))
        self.assertFalse(ea.check_better_individual_index(1, 2, ea.population))
        self.assertTrue(ea.check_better_individual_index(1, 0, ea.population))

    def test_selection(self):
        fun = Function_eval((0, 100), 1, "x", "f")
        i1 = Individual([5])
        i2 = Individual([10])
        i3 = Individual([15])
        p1 = Population(individuals=[i1, i2, i3])
        ea = EA(fun, p1)
        ea.count_fitness(ea.population)

        ea.selection()
        self.assertTrue(len(ea.offsprings.individuals) > 0)
        self.assertIn(ea.offsprings.individuals[0].values[0], [5, 10, 15])

    def test_crossover(self):
        fun = Function_eval((0, 100), 1, "x", "f")
        i1 = Individual([5])
        i1.set_sigmas([0.5])
        i2 = Individual([10])
        i2.set_sigmas([0.5])
        p1 = Population(individuals=[i1, i2])
        ea = EA(fun, p1)
        ea.crossover_probability = 1
        ea.count_fitness(ea.population)

        i4 = ea.crossover(i1, i2, a=0.5)
        self.assertEqual(i4.values[0], 7.5)

        i5 = ea.crossover(i1, i2, 0.2)
        self.assertEqual(i5.values[0], 5*0.2+10*0.8)

    def test_mutate(self):
        pass


if __name__ == '__main__':
    unittest.main()

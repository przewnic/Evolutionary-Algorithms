"""
Project: Evolutionary Algorithm + Island Model
Authors: przewnic
Date: 12.2020
"""
# Population Class Implementation
from Individual import Individual
from numpy import random


class Population():
    def __init__(self, individuals=None, population_size=None, params=None):
        """ Two ways of creating a population:
            1. giving individuals as a argument
            2. giving population size and params,
               then individuals will be created randomly
        """
        if individuals is not None:
            self.individuals = individuals
        else:
            self.individuals = [Individual(params=params)
                                for i in range(population_size)]

    def get_random_individual(self):
        random_index = random.randint(0, self.get_population_size())
        return self.individuals[random_index]

    def replace(self, new_population):
        """ Replace existing population with a new one """
        self.individuals = new_population

    def get_population_size(self):
        return len(self.individuals)

    def add_individual(self, new_individual):
        self.individuals.append(new_individual)

    def trim_size(self, size):
        """ Trims population size to given as a argument """
        if len(self.individuals) > size:
            self.individuals = self.individuals[:size]
            return True
        return False

    def __str__(self):
        info = f"Population consists of {self.get_population_size()} individuals." + \
                f"List of values of individuals:\n"
        for counter, individual in enumerate(self.individuals):
            info += f"{counter+1}. "+individual.__str__() 
            if individual.fitness is not None:
                info += f" Fitness:{individual.fitness}"
            info += "\n"
        return info

"""
Project: Evolutionary Algorithm + Island Model
Authors: przewnic
Date: 12.2020
"""
# Individual Class Implementation
import numpy as np


class Individual():
    def __init__(self, values=None, params=None, sigmas=None):
        """
            values: A List of values of Individual
            params: lower_bound, upper_bound, dimentions
            Params used to select random Values if initial values not specified
        """
        if values is not None:
            self.values = values
        else:
            self.values = self.init_random(params)
        self.sigmas = sigmas
        self.fitness = None

    def set_sigmas(self, new_sigmas):
        self.sigmas = new_sigmas

    def set_fitness(self, new_fitness):
        self.fitness = new_fitness

    def get_fitness(self):
        return self.fitness

    def set_values(self, new_values):
        self.values = new_values

    def get_values(self):
        return self.values

    def init_random(self, params):
        """ params: lower_bound, upper_bound, dimentions
        """
        return list(np.random.uniform(params[0], params[1], params[2]))

    def __str__(self):
        return f"Individual: {self.values}"

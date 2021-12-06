"""
Project: Evolutionary Algorithm + Island Model
Authors: przewnic
Date: 12.2020
"""
from CsvReader import CsvReader, CsvWriter
from EA import EA
from Island_ea import IslandEA, Island
import matplotlib.pyplot as plt


class Simulation:
    """ Class used to simulate evolution"""
    def __init__(self, function, number_of_isles, migration_number,
                 migration_epoch, topology, nr_of_steps):
        """
        Args:
            function: function which is optimized
            number_of_isles: how many isles to create
            migration_number: how many individuals migrate
            migration_epoch: number of steps to the next migration
            topology: chosen topology of connections between islands
            nr_of_steps: how many steps to do
        """
        self.nr_of_steps = nr_of_steps
        if number_of_isles <= 0:
            number_of_isles = 1
        isles = []
        for _ in range(number_of_isles):
            isles.append(Island(function))
        self.basic_model = EA(function, population=isles[0].population,
                              nr_of_steps=nr_of_steps)
        self.island_model = IslandEA(isles, migration_number,
                                     migration_epoch, topology, nr_of_steps)

    def simulate(self, print_populations=False):
        best_fitnesses = []
        best_fitnesses_island = []
        for _ in range(self.nr_of_steps):
            self.basic_model.step()
            self.island_model.step()
            if print_populations:
                print(f"Basic model Population:\nStep:{_}", self.basic_model.population)
                print(f"Island model Population:\nStep:{_}", self.island_model.get_results())
            best_fitnesses.append(self.basic_model.population.individuals[0].fitness)
            best_fitnesses_island.append(self.island_model.get_results().individuals[0].fitness)
        fig, ax = plt.subplots()
        ax.plot(range(1, self.nr_of_steps+1), best_fitnesses, 'ro', label="Basic Model")
        ax.plot(range(1, self.nr_of_steps+1), best_fitnesses_island, 'bo', label="Island Model")
        ax.set(xlabel="step number", ylabel="fitness",
               title="Plot of fitness values during evolution")
        ax.grid()
        plt.legend()
        plt.show()
        result_basic = self.basic_model.get_best_result()
        result_island = self.island_model.get_best_result()
        return result_basic, result_island

    def solve(self):
        for _ in range(self.nr_of_steps):
            self.basic_model.step()
            self.island_model.step()
        result_basic = self.basic_model.get_best_result()
        result_island = self.island_model.get_best_result()
        return result_basic, result_island

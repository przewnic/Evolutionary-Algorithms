"""
Project: Evolutionary Algorithm + Island Model
Authors: przewnic
Date: 12.2020
"""
# Evolutionary Alghoritm
from EA import EA
from Population import Population
import concurrent.futures as cf
import copy


class Island(EA):
    def __init__(self, function, population=None, nr_of_steps=30,
                 mutation_width_of_distribution=1,
                 mutation_probability=1,
                 crossover_probability=0.9):
        super().__init__(function,
                         population, nr_of_steps,
                         mutation_width_of_distribution,
                         mutation_probability,
                         crossover_probability)

    def check_stop_condition(self):
        """ No need to check condition if an island,
            migration could change individuals
        """
        pass


class IslandEA():
    """ Implementation of Island Model """
    def __init__(self, islands, migration_number,
                 migration_epoch, topology, nr_of_steps):
        """
        Args:
            islands: which islads belog to archipelago
            migration_number: how many individuals migrate
            migration_epoch: number of steps to the next migration
            topology: chosen topology of connections between islands
            nr_of_steps: how many steps to do
        """
        self.islands = islands
        self.nr_of_islands = len(islands)
        self.migration_number = migration_number  # Number of individuals, that migrate between islands
        self.migration_epoch = migration_epoch  # Number of generations elapsed before individuals are received or sent from/to others
        self.topology = topology

        self.nr_of_steps = nr_of_steps
        self.current_step = 0
        self.threads = []

    def migrate(self):
        if self.topology == "ring":
            for next_island_index, island in enumerate(self.islands):
                if island is self.islands[-1]:
                    next_island_index = 0
                migration = island.population.individuals[:self.migration_number]
                migration = copy.deepcopy(migration)
                self.islands[next_island_index].population.individuals[-self.migration_number:] = migration

        elif self.topology == "star":
            """ A specialized processor or bridge
                is used in order to receive the information from all the islands, process it and
                return the result to all of them. In this model, the islands send individuals to
                the bridge, and it generates a pool with the union of all the received individuals.
                Afterward, the bridge selects (by fitness) the best subset from the pool and
                sends it to every island. """
            migration = self.get_results().individuals[:self.migration_number]
            for island in self.islands:
                island.population.individuals[-self.migration_number:] = copy.deepcopy(migration)

    def step(self):
        for island in self.islands:
            island.step()
        self.current_step += 1
        if self.current_step % self.migration_epoch == 0:
            self.migrate()

    def threads_step(self):
        with cf.ThreadPoolExecutor(max_workers=self.nr_of_islands) as isle:
            isle.map(self.thread_function, self.islands)
        self.current_step += 1
        if self.current_step % self.migration_epoch == 0:
            self.migrate()

    def thread_function(self, island):
        island.step()

    def get_results(self, result_size=10):
        # Combine results from all islands, take the best ones
        best_individuals = []
        for island in self.islands:
            best_individuals += island.population.individuals
        if result_size < len(best_individuals):
            best_individuals = best_individuals[:result_size]
        best_population = Population(best_individuals)
        best_population.individuals.sort(key=lambda x: x.get_fitness(), reverse=False)
        return best_population

    def get_best_result(self):
        return self.get_results(result_size=1).individuals[0].fitness

    def solve(self):
        # In loop till max number of steps
        for step in range(self.nr_of_steps):
            step()

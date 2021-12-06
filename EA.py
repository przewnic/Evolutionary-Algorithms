"""
Project: Evolutionary Algorithm + Island Model
Authors: przewnic
Date: 12.2020
"""

# Evolutionary Alghoritm
from Population import Population
from Individual import Individual
from numpy import random, average, exp
import copy
POPULATION_SIZE = 3  # if population not specified in EA constructor


class EA():
    """ Implementation of Evolutionary Alghoritm mu+lambda """
    def __init__(self, function, population=None, nr_of_steps=30,
                 mutation_width_of_distribution=1,
                 mutation_probability=1,
                 crossover_probability=0.9):
        self.function = function
        if population is not None:
            self.population = population
        else:
            self.initialize_population(POPULATION_SIZE)
        self.mu_size = self.population.get_population_size()
        self.offsprings = Population(individuals=[])
        self.nr_of_steps = nr_of_steps
        self.current_step = 0
        self.mutation_width_of_distribution = mutation_width_of_distribution
        self.mutation_probability = mutation_probability
        self.crossover_probability = crossover_probability
        self.lambda_size = self.mu_size*7
        self.set_sigma_values()
        self.set_tau_values()
        self.count_fitness(self.population)

    def set_tau_values(self):
        """ Sets tau values for the problem """
        d = self.function.dimentions
        self.tau = (2*d)**-0.5
        self.tau_prime = (2*(d**0.5))**-0.5

    def set_sigma_values(self):
        """ Used by creating first population """
        for individual in self.population.individuals:
            individual.sigmas = list(random.normal(
                    0,
                    self.mutation_width_of_distribution,
                    self.function.dimentions))

    def set_lambda_size(self, new_size):
        self.lambda_size = new_size

    def set_nr_of_steps(self, new_nr):
        self.nr_of_steps = new_nr

    def initialize_population(self, population_size):
        """
        Args:
            population_size: how many initial individuals
        """
        self.population = Population(population_size=population_size,
                                     params=self.function.get_params())

    def count_fitness(self, population):
        """ Calculation of a fitness of all individuals """
        for individual in population.individuals:
            individual.set_fitness(self.function.get_y_value(individual.get_values()))

    def sort_by_fitness(self, population):
        population.individuals.sort(key=lambda x: x.get_fitness(),
                                    reverse=False)

    def selection(self):
        """ Implements tournament strategy: takes two
            parents and selects the fittest, till there is place for new individuals.
        """
        self.offsprings.individuals.clear()
        """
        for _ in range(self.lambda_size):
            index_1, index_2 = random.randint(0, self.mu_size), random.randint(0, self.mu_size)
            if self.check_better_individual_index(index_1, index_2, self.population):
                self.offsprings.individuals.append(self.population.individuals[index_1])
            else:
                self.offsprings.individuals.append(self.population.individuals[index_2])
        """
        for _ in range(self.lambda_size):
            index_1 = random.randint(0, self.mu_size)
            selected = self.population.individuals[index_1]
            new_individual = copy.deepcopy(selected)
            self.offsprings.individuals.append(new_individual)

    def check_better_individual_index(self, index_1, index_2, in_population):
        """ Returns True if fitness of first index in chosen population is better
            Lesser value better - Minimization
        """
        if in_population.individuals[index_1].fitness < in_population.individuals[index_2].fitness:
            return True
        return False

    def check_better_individual(self, individual_1, individual_2):
        """ Returns True if fitness of first individual is better
            Lesser value better - Minimization
        """
        if individual_1.fitness < individual_2.fitness:
            return True
        return False

    def crossover_population(self):
        """
            Every selected individual may become a parent,
            new offspring replaces worse parent
        """
        for counter, individual in enumerate(self.offsprings.individuals):
            if random.rand() < self.crossover_probability:
                index_second_parent = random.randint(0, self.lambda_size)
                if self.offsprings.individuals[index_second_parent] is individual:
                    continue
                second_parent = self.offsprings.individuals[index_second_parent]
                new_individual = copy.deepcopy(self.crossover(individual,
                                                              second_parent))
                if self.check_better_individual(second_parent, individual):
                    individual = new_individual
                else:
                    second_parent = new_individual
                if counter == self.lambda_size:
                    break

    def crossover(self, parent_1, parent_2, a=None):
        """
            Interpolation of two parents
            Returns new Individual
        """
        values = []
        sigmas = []
        if a is None:
            a = random.uniform(0, 1)
        for v1, v2, s1, s2 in zip(parent_1.values, parent_2.values,
                                  parent_1.sigmas, parent_2.sigmas):
            values.append(a*v1 + (1-a)*v2)
            sigmas.append(a*s1 + (1-a)*s2)
        new_offspring = Individual(values)
        new_offspring.set_sigmas(sigmas)
        new_offspring.set_fitness(self.function.get_y_value(new_offspring.get_values()))
        return new_offspring

    def mutate_population(self):
        for individual in self.offsprings.individuals:
            if random.rand() <= self.mutation_probability:
                individual = self.mutate(individual)

    def mutate(self, individual):
        # Add random value from normal distribution
        ksi = float(random.normal(0, 1, 1))
        for sigma in individual.sigmas:
            ksi_sigma = float(random.normal(0, 1, 1))
            sigma = sigma*float(exp(self.tau*ksi + self.tau_prime*ksi_sigma))

        for i in range(self.function.dimentions):
            individual.values[i] += individual.sigmas[i]*float(random.normal(0, 1, 1))
            # Check lower and upper bounds for every gene
            individual.values[i] = max(individual.values[i],
                                       self.function.bounds[0])
            individual.values[i] = min(individual.values[i],
                                       self.function.bounds[1])
        return individual

    def succession(self):
        self.count_fitness(self.offsprings)
        succesion_list = self.population.individuals + \
            self.offsprings.individuals
        new_population = Population(succesion_list)
        self.sort_by_fitness(new_population)
        new_population.trim_size(self.mu_size)
        return new_population

    def step(self):
        self.count_fitness(self.population)
        self.current_step += 1
        self.selection()
        self.mutate_population()
        self.crossover_population()
        self.population = self.succession()

    def check_stop_condition(self):
        # TODO Is it necessary to implement additional condition ?
        if self.current_step >= self.nr_of_steps:
            return True

    def solve(self):
        # In loop till max number of steps or stop condition True
        for _ in range(self.nr_of_steps):
            if self.check_stop_condition() is True:
                break
            self.step()
        return self.population

    def get_best_result(self):
        if self.population is not None:
            self.sort_by_fitness(self.population)
            return self.population.individuals[0].fitness
        return None

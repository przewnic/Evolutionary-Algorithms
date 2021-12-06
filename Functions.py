"""
Project: Evolutionary Algorithm + Island Model
Authors: przewnic
Date: 12.2020
"""

# Script contains:
#    Function: Base class  for all functions used in EA alghoritms
#    Other classes: implement some chosen functions
import math


class Function():
    """ Base class for implementation of diffrent kinds of functions """
    def __init__(self, bounds, dimentions, name):
        """
        Args:
        bounds: tuple of acceptable values of x
        dimentions: number of dimentions
        name: name of the function
        """
        self.bounds = bounds
        self.dimentions = dimentions
        self.name = name

    def get_params(self):
        """ Returns tuples of function parameters """
        return self.bounds + (self.dimentions,)

    def get_y_value(self, x):
        """ Implemented in subclasses """
        pass

    def get_function(self):
        """ Returns implemented function """
        return self.get_y_value

    def __str__(self):
        return f"Function: X bounds: {self.bounds}, dim: {self.dimentions} \
                 \n {self.name} Function"


class RidgesFunction(Function):
    def __init__(self, bounds, dimentions, name="Ridge's"):
        super().__init__(bounds, dimentions, name)

    def get_y_value(self, x):
        sum = 0
        for i in range(self.dimentions):
            i_sum = 0
            for j in range(i+1):
                i_sum += x[j]
            sum += i_sum**2
        return sum


class ModifiedDoubleSum(Function):
    def __init__(self, bounds, dimentions, name="Modified Double Sum"):
        super().__init__(bounds, dimentions, name)

    def get_y_value(self, x):
        sum_y = 0
        for i in range(self.dimentions):
            i_sum = 0
            for j in range(i+1):
                i_sum += (x[j] - j - 1)**2
            sum_y += i_sum
        return sum_y


class Rastrings(Function):
    def __init__(self, bounds, dimentions, name="Rastring's"):
        super().__init__(bounds, dimentions, name)

    def get_y_value(self, x):
        sum_y = 10*self.dimentions
        for i in range(self.dimentions):
            sum_y += x[i]**2 - 10*math.cos(2*math.pi*x[i])
        return sum_y


class Griewanks(Function):
    def __init__(self, bounds, dimentions, name="Griewank's"):
        super().__init__(bounds, dimentions, name)

    def get_y_value(self, x):
        sum_y = 0
        multiple_y = 1
        for i in range(self.dimentions):
            sum_y += x[i]**2
            multiple_y *= math.cos(x[i]/((i+1)**0.5))
        sum_y = 1 + (1/4000)*sum_y - multiple_y
        return sum_y


class Schwefels(Function):
    def __init__(self, bounds, dimentions, name="Schwefel's"):
        super().__init__(bounds, dimentions, name)

    def get_y_value(self, x):
        sum_y = 0
        for i in range(self.dimentions):
            sum_y += -x[i]*math.sin(abs(x[i])**0.5)
        return sum_y + 418.982887*self.dimentions


class Rosenbrock(Function):
    def __init__(self, bounds, dimentions, name="Rosenbrock's"):
        super().__init__(bounds, dimentions, name)

    def get_y_value(self, x):
        sum_y = 0
        for i in range(self.dimentions-1):
            sum_y += (100*(x[i]**2 - x[i+1])**2 + (1-x[i])**2)
        return sum_y
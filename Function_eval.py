"""
Project: Evolutionary Algorithm + Island Model
Authors: przewnic
Date: 12.2020
"""

# Script contains:
# 1. a class used to create self-implementations
#   of chosen functions for testing purposes
from Functions import Function
import math


class Function_eval(Function):
    def __init__(self, bounds, dimentions, function, name):
        super().__init__(bounds, dimentions, name)
        """
        Args:
        function: combination of x[i] as a string
        """
        self.function = function  # eg. "-x[0] * (x[0] - 1) * (x[0] - 2) * (x[0] - 3) * (x[0] - 4)"
        self.y = eval("lambda x: "+self.function)

    def get_y_value(self, x):
        return self.y(x)

    def replace_function(self, new_function):
        self.function = new_function
        self.y = eval("lambda x: "+new_function)

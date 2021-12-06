"""
Project: Evolutionary Algorithm + Island Model
Authors: przewnic
Date: 12.2020
"""

# Script contains:
# 1. a class used as a wrapper for cec2017 functions
from Functions import Function
import math
import numpy as np


class Function_cec2017(Function):
    """ Wrapper  for cec2017 functions to use in EA alghoritms"""
    def __init__(self, bounds, dimentions, function, name):
        super().__init__(bounds, dimentions, name)
        self.function = function

    def get_y_value(self, x):
        return self.function(np.array(x))

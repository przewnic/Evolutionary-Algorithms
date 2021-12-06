"""
Project: Evolutionary Algorithm + Island Model
Authors: przewnic
Date: 12.2020
"""
# File contains a set of self-implemented functions to
# check the functionality of EA alghoritms

from Function_eval import Function_eval
from EA import EA
from Functions import RidgesFunction, ModifiedDoubleSum, Rastrings, \
                      Griewanks, Schwefels, Rosenbrock
from Simulation import Simulation


# Sphere Model F(X) = sum(x_i**2)
fun_1 = Function_eval((-5.12, 5.12), 5, "x[0]**2 + x[1]**2 + x[2]**2 + x[3]**2 + x[4]**2", "Sphere")

# Ridge's function = sum(sum(x_i**2))
fun_2 = RidgesFunction((-64, 64), 25)

# Exponential function
fun_3  = Function_eval((-5.12, 5.12), 5, "math.e**(x[0]*1) + math.e**(x[1]*2)+ math.e**(x[2]*3)+ math.e**(x[3]*4)+ math.e**(x[4]*5) +"+
                    "math.e**(-5.12*1) + math.e**(-5.12*2) + math.e**(-5.12*3) + math.e**(-5.12*4) + math.e**(-5.12*5)", "Exponential")

# ModifiedDoubleSum
fun_4 = ModifiedDoubleSum((-10.24, 10.24), 5)

# Rastring's Function
fun_5 = Rastrings((-5.12, 5.12), 5)

# Griewank's Function
fun_6 = Griewanks((-512, 512), 5)

# Schwefel's Function
fun_7 = Schwefels((-512, 512), 5)

# Rosenbrock Funtion
fun_8 = Rosenbrock((-2.048, 2.048), 5)




# Simulation
#######################
CHOSEN_FUNCTION = fun_2
#######################
nr_of_ilands = 5
nr_of_epochs = 5

sim = Simulation(CHOSEN_FUNCTION, 5, 5, 3, "ring", 300)
x = sim.simulate()
print(f"{x[0]:.5}  {x[1]:.5}")


# Evolutionary Alghoritm

ea = EA(fun_2)

"""
print(ea.population)
for _ in range(40):
    print(_)
    ea.step()
    print(ea.population)
"""
"""
# Evolutionary Alghoritm with Islands
isles = []
number_of_isles = 5
for _ in range(number_of_isles):
    isles.append(Island(fun_8))

iea = IslandEA(isles, 5, 3, "ring", 30)
for step in range(40):
    iea.threads_step()
    print(step)
    print(iea.get_results())
"""
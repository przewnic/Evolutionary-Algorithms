"""
Project: Evolutionary Algorithm + Island Model
Authors: przewnic
Date: 12.2020
"""
from cec2017.functions import *
# cec2017-py from github
from Function import Function_cec2017
from Simulation import Simulation


bounds = (-100, 100)
dims = 10
cec_f1 = Function_cec2017(bounds, dims, f1, 'f1')
cec_f2 = Function_cec2017(bounds, dims, f2, 'f2')
cec_f3 = Function_cec2017(bounds, dims, f3, 'f3')
cec_f4 = Function_cec2017(bounds, dims, f4, 'f4')
cec_f5 = Function_cec2017(bounds, dims, f5, 'f5')
cec_f6 = Function_cec2017(bounds, dims, f6, 'f6')
cec_f7 = Function_cec2017(bounds, dims, f7, 'f7')
cec_f8 = Function_cec2017(bounds, dims, f8, 'f8')
cec_f9 = Function_cec2017(bounds, dims, f9, 'f9')
cec_f10 = Function_cec2017(bounds, dims, f10, 'f10')
cec_f11 = Function_cec2017(bounds, dims, f11, 'f11')
cec_f12 = Function_cec2017(bounds, dims, f12, 'f12')
cec_f13 = Function_cec2017(bounds, dims, f13, 'f13')
cec_f14 = Function_cec2017(bounds, dims, f14, 'f14')
cec_f15 = Function_cec2017(bounds, dims, f15, 'f15')
cec_f16 = Function_cec2017(bounds, dims, f16, 'f16')
cec_f17 = Function_cec2017(bounds, dims, f17, 'f17')
cec_f18 = Function_cec2017(bounds, dims, f18, 'f18')
cec_f19 = Function_cec2017(bounds, dims, f19, 'f19')
cec_f20 = Function_cec2017(bounds, dims, f20, 'f20')
cec_f21 = Function_cec2017(bounds, dims, f21, 'f21')
cec_f22 = Function_cec2017(bounds, dims, f22, 'f22')
cec_f23 = Function_cec2017(bounds, dims, f23, 'f23')
cec_f24 = Function_cec2017(bounds, dims, f24, 'f24')
cec_f25 = Function_cec2017(bounds, dims, f25, 'f25')
cec_f26 = Function_cec2017(bounds, dims, f26, 'f26')
cec_f27 = Function_cec2017(bounds, dims, f27, 'f27')
cec_f28 = Function_cec2017(bounds, dims, f28, 'f28')
cec_f29 = Function_cec2017(bounds, dims, f29, 'f29')
cec_f30 = Function_cec2017(bounds, dims, f30, 'f30')


# Simulation
sim = Simulation(cec_f3, 5, 5, 10, "ring", 200)
#x = sim.simulate()
x = sim.solve()
print(f"{x[0]:.5}  {x[1]:.5}")


"""
from EA import EA
ea = EA(cec_f3)
print(ea.population)
for _ in range(100):
    print(_)
    ea.step()
    print(ea.population)
"""
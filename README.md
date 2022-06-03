# Basics of Artificial Intelligence
Project nr 1 - Maybe on an island?

---

### Description of important design decisions
Project was created using Python language (Recommended version at least 3.7). 

### Comparison of standard Evolutionary algorithm and version with an Island Model.

### Island Model description:
In this model population is divided into subgroups. 
Each of them is evolving on its owm, and every few generations there is a migration of individuals to the other island/(s). 

There are specified two ways of migrating:
1. Ring Topology - there are chosen best individuals from every island and they migrate to the adjacent island
2. Star Topology - there are chosen best individuals from all islands and copies of them go to every island in topology

### Goals and thesis of conducted study
Goal of this project was to test if use of modified evolutionary algorithm, in which there will be used subgrups of populations i.e. in which such subgroups develop independetly, will result in better outcomes comparing to standard version of this algorithm. There can be assumed that thanks to higher count of individuals, the exploration space of optimum could be better. Populations develop independently form each other, thus it may be assuemed also that better exploatation of optimums will occur for every of the island, if their initial values are different.

CEC F1 Function
Changes of fitness values during evolution for F1 functiion for standard model and Island model with Ring topology | Changes of fitness values during evolution for F1 functiion for standard model and Island model with Star topology
:-------------------------:|:-------------------------:
![cec_f1_1000](https://user-images.githubusercontent.com/24957921/171777561-5c60af98-2db2-4350-a455-9e94442f226d.svg) | ![cec_f1_1000_star](https://user-images.githubusercontent.com/24957921/171777553-d7b7b4c1-b6d6-4e58-b036-2626166a8b19.svg)

CEC F3 Function
Changes of fitness values during evolution for F3 functiion for standard model and Island model with Ring topology | Changes of fitness values during evolution for F3 functiion for standard model and Island model with Star topology
:-------------------------:|:-------------------------:
![cec_f3](https://user-images.githubusercontent.com/24957921/171777590-c2493ded-895d-448c-904b-2201c6ce03d3.svg) | ![cec_f3_1000_star](https://user-images.githubusercontent.com/24957921/171777574-28602a6a-52f0-42a4-b1a8-dbb6a95c3b34.svg)

### Conducted experiments
For testing were used functions defined in CEC2017, with search constrains $[-100, 100]^{\mathrm{D}}$. (During the experiments the value of $D$ equaled to $D=10$) The operation is started with initialisation of values of individuals randomly selected from uniform distribution form given range. The end of the evaluations occurs when the chosen number of generations is achieved. Because of the resources and time constrains as well as based on initial tests chosen number of generations for the test was equal to 100. The optimum for each of the test function was searched for 25 times. Results show the statistical values based upon those experiments. For each function will be calculated the following measures: 

- min
- max
- median
- mean
- std

Fitness values based on 25 test for F1 function for standard algorithm, Island Ring and Island Star | Fitness values based on 25 test for F3 function for standard algorithm, Island Ring and Island Star
:-------------------------:|:-------------------------:
![F1_box_crs](https://user-images.githubusercontent.com/24957921/171779951-7dc554c1-a385-4527-9cb7-afb3328e2f3d.svg) | ![F3_box_crs](https://user-images.githubusercontent.com/24957921/171779964-5d2519a9-4ce9-4986-bf6a-8a62f6babb6d.svg)


Used libraries:
1. numpy 
```
pip install numpy
```
2. cec2017-py - benchmark functions for testing of algorithms
```
git clone https://github.com/tilleyd/cec2017-py
cd cec2017-py
python3 setup.py install
```
3. math
4. matplotlib
```
pip install matplotlib
 ```

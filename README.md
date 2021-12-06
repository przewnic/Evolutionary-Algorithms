# BoAI
Project nr 1 - Basics of Artificial Intelligence

Comparison of standard Evolutionary algorithm and version with an Island Model.

In this model population is divided into subgroups. 
Everyone of them is evolving on its owm, and every few generations there is a migration of individuals to the other island. 
There are specified two ways of migrating:
1. Ring Topology - there are chosen best individuals from every island and they migrate to the adjacent island
2. Star Topology - there are chosen best individuals from all islands and copies of them go to every island in topology


Used libraries:
1. numpy 
pip install numpy

2. cec2017-py
git clone https://github.com/tilleyd/cec2017-py
cd cec2017-py
python3 setup.py install

3. math

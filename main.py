import networkx as nx
import matplotlib.pyplot as plt
from metropolis import independent_set
from utils import draw

n = m = 16
p = 0.5
mtemp = 0.1
miter = 100

G = nx.bipartite.random_graph(n, m, p)
IS = independent_set(G, miter, mtemp)
# draw(G, IS)

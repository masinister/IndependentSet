import networkx as nx
import matplotlib.pyplot as plt
from metropolis import independent_set
from utils import draw

n = m = 1024
p = 0.5

G = nx.bipartite.random_graph(n, m, p)

temps = [0.01, 0.05, 0.1, 0.5]
iters = [512,1024,2048,4096,8192]


for temp in temps:
    sizes = []
    for iter in iters:
        t = []
        for i in range(32):
            IS = independent_set(G, iter, temp)
            t.append(len(list(IS)))
        sizes.append(sum(t) / len(t))
    plt.plot(iters, sizes)

plt.legend(temps, title = "Temperatures")
plt.xlabel("Stopping Time")
plt.ylabel("Mean IS Size")
plt.title("Mean IS Size vs. Stopping Time")
plt.show()

# draw(G,IS)

import networkx as nx
import matplotlib.pyplot as plt
from metropolis import independent_set
from utils import draw

n = m = 800
d = 11
p = d / n

G = nx.bipartite.random_graph(n, m, p)
bottom_nodes, top_nodes = set(range(0,n)), set(range(n,n+m)),

temps = [0.01, 0.05, 0.1, 0.5]
iters = [n*2, n*2**2, n*2**3, n*2**4,n*2**5, n*2**6,n*2**7, n*2**8,]
# iters = [100,200,300]

fig, (ax1, ax2) = plt.subplots(1,2)

for temp in temps:
    sizes = []
    adiffs = []
    for iter in iters:
        t = []
        ad = []
        for i in range(32):
            IS = independent_set(G, iter, temp)
            t.append(len(list(IS)))
            bottom_IS = bottom_nodes.intersection(IS)
            top_IS = top_nodes.intersection(IS)
            ad.append(abs(len(list(bottom_IS)) - len(list(top_IS))))
        sizes.append(sum(t) / len(t))
        adiffs.append(sum(ad) / len(ad))
    ax1.plot(iters, sizes)
    ax2.plot(iters, adiffs)

fig.suptitle("n = {}, d = {}".format(n,d))
fig.legend(temps, title = "Temperatures")
plt.xlabel("Stopping Time")

ax1.set_ylabel("Mean IS Size (32 runs)")

ax2.set_ylabel("Mean IS Size Abs. Diff. |L-R| (32 runs)")
plt.show()

# draw(G,IS)

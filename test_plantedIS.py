import networkx as nx
import matplotlib.pyplot as plt
from metropolis import independent_set
from graphs import planted_IS
from utils import draw

n = 1000
p = 1/2.
k = n**(1/10) # Planted IS size

G = planted_IS(n, p, k)
temps = [0.01, 0.05, 0.1, 0.5]
iters = [n*2, n*2**2, n*2**3, n*2**4,n*2**5, n*2**6,n*2**7,]
# iters = [100,200,300]

for temp in temps:
    sizes = []
    for iter in iters:
        t = []
        for i in range(32):
            IS = independent_set(G, iter, temp)
            t.append(len(list(IS)))
        sizes.append(sum(t) / len(t))
    plt.plot(iters, sizes)

plt.title("n = {}, p = {}, k = {}".format(n,p,int(k)))
plt.xlabel("Stopping Time")
plt.ylabel("Mean IS Size (32 runs)")
plt.legend(temps, title = "Temperatures")
plt.show()

# draw(G,IS)

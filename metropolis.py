from random import choice, random

def independent_set(G, iter, temp):
    IS = set()
    for _ in range(iter):
        node = choice(list(G))
        neighbors = set().union(*[set(G.adj[v]) for v in IS])
        if node in neighbors:
            continue
        if node not in IS:
            IS.add(node)
            continue
        if random() < temp:
            IS.remove(node)
    return IS

if __name__ == '__main__':
    import networkx as nx
    import matplotlib.pyplot as plt
    from utils import draw

    n = 16
    p = 0.5
    G = nx.bipartite.random_graph(n,n,p)
    IS = independent_set(G, 100, 0.1)

    draw(G,IS)

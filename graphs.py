import networkx as nx
import matplotlib.pyplot as plt

def reichman_graph(k,m,c):
    "A collection of k (disjoint) pairs of \
    independent sets of size m \
    connected by complete bipartite graph to \
    Cliques of size Cm."
    G = nx.Graph()
    for i in range(k):
        IS = nx.Graph()
        IS.add_nodes_from(range(m))
        C = nx.complete_graph(c * m)
        T = nx.full_join(IS,C, rename = ("IS{}".format(i), "C{}".format(i)))
        G = nx.disjoint_union(G, T)
    return G

if __name__ == '__main__':
    nx.draw(reichman_graph(3,3,1))
    plt.show()

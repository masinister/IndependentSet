import networkx as nx
import matplotlib.pyplot as plt

def draw(G, IS):
    color_map = []
    for node in G:
        if node in IS:
            color_map.append('green')
        else:
            color_map.append('gray')
    nx.draw(G, node_color = color_map, with_labels = True)
    plt.show()

def draw_bipartite(G, IS):
    color_map = []
    for node in G:
        if node in IS:
            color_map.append('green')
        else:
            color_map.append('gray')
    top = nx.bipartite.sets(G)[0]
    pos = nx.bipartite_layout(G, top)
    nx.draw(G, node_color = color_map, with_labels = True, pos = pos)
    plt.show()

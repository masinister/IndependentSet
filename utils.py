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

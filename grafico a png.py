import networkx as nx
from networkx.algorithms.link_analysis.pagerank_alg import pagerank
from src.utils.utils import init_graph
import numpy as np
from src.PageRank import PageRank
from numpy import array
import matplotlib.pyplot as plt


filename = './dataset/node.txt'

def pagerank_calculation(iteration, graph, damping_factor):
    PageRank(graph, damping_factor, iteration)
    pagerank_list = graph.get_pagerank_list()
    return pagerank_list

graph = init_graph(filename)
graph.display()
pesos = pagerank_calculation(500,graph,0.15)

G = nx.DiGraph()

for node in graph.nodes:
    for child in node.children:
        node_name = str(node.name) + "\n" + str(round(node.pagerank,3))
        child_name = str(child.name) + "\n" + str(round(child.pagerank,3))
        G.add_edge(node_name,child_name, weight=(node.pagerank)**2)

print(pesos)


nx.draw(G, with_labels=True, node_size=1000, edge_color='#eb4034', width=1, font_size=8, font_weight=50, arrowsize=15, alpha=1)
plt.savefig("grafico.png")


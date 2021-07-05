from src.utils.utils import init_graph
from src.PageRank import PageRank_one_iter
import matplotlib.pyplot as plt

damping_factor = 0.1
iteration = 10
file_path = 'dataset/node.txt'

graph = init_graph(file_path)

length = len(graph.nodes)
all_pagerank = [[] for i in range(length)]


for i in range(iteration):
    PageRank_one_iter(graph, damping_factor)
    pagerank_list = graph.get_pagerank_list()
    for idx, auth in enumerate(pagerank_list):
        all_pagerank[idx].append(auth)

for pagerank_list in all_pagerank:
    plt.plot(pagerank_list)

plt.title('PageRank on iteration')
plt.legend([node.name for node in graph.nodes])
plt.xlabel('Iteration')
plt.ylabel('Value')

plt.show()

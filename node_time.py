from src.utils.utils import init_graph
from src.PageRank import PageRank
import itertools
import random
import time
import matplotlib.pyplot as plt


def create_graph(node_num):
    edges = []
    node_list = [i+1 for i in range(node_num)]
    edge_num = node_num * 2
    edge_pool = list(itertools.permutations(node_list, 2))
    for i in range(edge_num):
        edge = random.choice(edge_pool)
        edges.append(edge)

    with open('dataset/prueba.txt', 'w') as f:
        for edge in edges:
            f.write(f'{edge[0]},{edge[1]}\n')

time_list = []

for i in range(0, 500, 10):
    print(i)
    create_graph(i)
    graph = init_graph('dataset/prueba.txt')

    prev_time = time.time()
    PageRank(graph, 0.15)
    time_list.append(time.time() - prev_time)

x = [2*i for i in range(0, 500, 10)]

plt.plot(x, time_list)
plt.title('Tiempo de computo de Pagerank en base al numero de conexiones')
plt.xlabel('Conexiones')
plt.ylabel('Tiempo (sec)')
plt.show()

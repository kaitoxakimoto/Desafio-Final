from src.utils.utils import init_graph
from src.PageRank import PageRank_one_iter
import matplotlib.pyplot as plt
from optparse import OptionParser

optparser = OptionParser()
optparser.add_option('-f', '--input_file',
                        dest='input_file',
                        help='CSV filename',
                        default='dataset/node.txt')

(options, args) = optparser.parse_args()
file_path = options.input_file

damping_factor = 0.15
iteration = 10


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

plt.title('Pagerank segun iteracion')
plt.legend([node.name for node in graph.nodes])
plt.xlabel('Iteracion')
plt.ylabel('Valor')

plt.show()

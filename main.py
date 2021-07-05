from src.utils.utils import init_graph
from src.PageRank import PageRank
from optparse import OptionParser

def output_PageRank(iteration, graph, damping_factor):
    PageRank(graph, damping_factor, iteration)
    pagerank_list = graph.get_pagerank_list()
    print('PageRank:')
    print(pagerank_list)


if __name__ == '__main__':


    file_path = 'dataset/node.txt'
    iteration = 500
    damping_factor = 0.15
 #   decay_factor = options.decay_factor

    graph = init_graph(file_path)

    output_PageRank(iteration, graph, damping_factor)

from src.utils.utils import init_graph
from src.PageRank import PageRank
from optparse import OptionParser

def output_PageRank(iteration, graph, damping_factor):
    PageRank(graph, damping_factor, iteration)
    pagerank_list = graph.get_pagerank_list()
    print('PageRank:')
    print(pagerank_list)


if __name__ == '__main__':

    optparser = OptionParser()
    optparser.add_option('-f', '--input_file',
                         dest='input_file',
                         help='CSV filename',
                         default='dataset/node.txt')

    (options, args) = optparser.parse_args()

    file_path = options.input_file
    iteration = 500
    damping_factor = 0.15

    graph = init_graph(file_path)

    output_PageRank(iteration, graph, damping_factor)

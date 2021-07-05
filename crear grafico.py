import itertools
import random
from optparse import OptionParser

optparser = OptionParser()
optparser.add_option('-f', '--input_file',
                        dest='input_file',
                        help='CSV filename',
                        default='dataset/node.txt')

(options, args) = optparser.parse_args()

file_path = options.input_file
node_num = 14


edges = []
node_list = [i+1 for i in range(node_num)]
edge_num = node_num * 2
edge_pool = list(itertools.permutations(node_list, 2))
for i in range(edge_num):
    edge = random.choice(edge_pool)
    edges.append(edge)
with open(file_path, 'w') as f:
    for edge in edges:
        f.write(f'{edge[0]},{edge[1]}\n')


from graph import Graph
from tqdm import tqdm


def parse_file(filename: str):
    with open(filename, 'r') as afile:
        num_nodes, num_edges = afile.readline().split(' ')
        num_nodes = int(num_nodes)
        num_edges = int(num_edges)

        edges = []

        for i in range(num_edges):
            v1, v2, weight = afile.readline().split(' ')
            v1 = int(v1) - 1
            v2 = int(v2) - 1
            weight = int(weight)
            edges.append((v1, v2, weight))

        return Graph(num_nodes, edges)

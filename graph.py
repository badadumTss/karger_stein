import numpy as np
import copy
from random import randrange


class Graph:
    # n_vertices builds the adjency matrix. `edges` are tuples in the
    # shape (a,b,w) where (a < b) and w in R
    def __init__(self, n_vertices, edges):
        # Assumption: there are no zero-valued edges. otherwise the
        # adj matrix initialised as such would be not valid
        self.adj_matrix = np.zeros((n_vertices, n_vertices))
        self.n_vertices = n_vertices
        self.edges = []
        self.vertices = [i for i in range(self.n_vertices)]

        self.degrees = np.zeros(n_vertices)
        for (a, b, w) in edges:
            self.adj_matrix[a][b] = self.adj_matrix[b][a] = w
            self.degrees[a] += 1
            self.degrees[b] += 1
            self.edges.append((a, b, w))
        print("initialized graph: {} {}".format(self.n_vertices, self.edges))

    @property
    def n_edges(self):
        return len(self.edges)

    def __repr__(self):
        return "{}".format(self.adj_matrix)

    def weight(self, u, v):
        return self.adj_matrix[u][v]

    def set_weight(self, u, v, n_w):
        self.adj_matrix[u][v] = self.adj_matrix[v][u] = n_w

    def merge_vertices(self, edge_index):
        u, v, w = self.edges[edge_index]
        del self.edges[edge_index]
        self.n_vertices -= 1
        self.degrees[u] = self.degrees[u] + \
            self.degrees[v] - (2 * self.weight(u, v))
        self.degrees[v] = 0
        self.set_weight(u, v, 0)
        # generator for all the nodes except u and v
        gen = (w for w in range(self.n_vertices) if w != u and w != v)
        for w in gen:
            self.set_weight(u, w, self.weight(u, w) + self.weight(v, w))
            self.set_weight(v, w, 0)
        print(self.edges)


def contract(graph, n_v=2):
    g = copy.deepcopy(graph)
    while g.n_vertices > n_v:
        r = randrange(0, g.n_edges)
        g.merge_vertices(r)
    return g


def karger_stein(graph):
    if graph.n_edges <= 6:
        g1 = contract(graph, 2)
        u, v, w = g1.edges[0]
        return w
    t = int(np.ceil(graph.n_vertices / np.sqrt(2)) + 1)
    w1 = karger_stein(contract(copy.deepcopy(graph), t))
    w2 = karger_stein(contract(copy.deepcopy(graph), t))
    return min(w1, w2)

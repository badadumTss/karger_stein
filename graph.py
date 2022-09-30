import numpy as np
import copy
from random import randrange
from time import perf_counter_ns
from queue import PriorityQueue
from queue_entries import PEntry


class Graph:
    # n_vertices builds the adjency matrix. `edges` are tuples in the
    # shape (a,b,w) where (a < b) and w in R
    def __init__(self, n_vertices, edges):
        # Assumption: there are no zero-valued edges. otherwise the
        # adj matrix initialised as such would be not valid
        self.adj_matrix = np.zeros((n_vertices, n_vertices))
        self.n_vertices = n_vertices
        self.edges = []
        self.vertices = set([i for i in range(self.n_vertices)])

        self.degrees = np.zeros(n_vertices)
        for (a, b, w) in edges:
            self.adj_matrix[a][b] = self.adj_matrix[b][a] = w
            self.degrees[a] += 1
            self.degrees[b] += 1
            self.edges.append((a, b, w))

    @property
    def n_edges(self):
        return len(self.edges)

    def __repr__(self):
        return "{}".format(self.adj_matrix)

    def weight(self, u, v):
        return self.adj_matrix[u][v]

    def set_weight(self, u, v, n_w):
        self.adj_matrix[u][v] = self.adj_matrix[v][u] = n_w

    def adj_list(self, v):
        to_ret = []
        for i, u in enumerate(self.adj_matrix[v]):
            if u != 0:
                to_ret += [i]
        return to_ret

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

    def remove(self, n):
        self.n_vertices -= 1
        self.adj_matrix[n, :] = 0
        self.adj_matrix[:, n] = 0
        self.vertices.remove(n)
        for i, (u,v,w) in enumerate(self.edges):
            if u == n or v == n:
                del self.edges[i]


def contract(graph, n_v=2):
    g = copy.deepcopy(graph)
    while g.n_vertices > n_v:
        r = randrange(0, g.n_edges)
        g.merge_vertices(r)
    return g


def karger_stein(graph):
    if graph.n_vertices <= 6:
        g1 = contract(graph, 2)
        u, v, w = g1.edges[0]
        return w, perf_counter_ns()
    t = int(np.ceil(graph.n_vertices / np.sqrt(2)) + 1)
    w1, t1 = karger_stein(contract(graph, t))
    w2, t2 = karger_stein(contract(graph, t))
    if w2 < w1:
        return w2, t2
    else:
        return w1, t1


def stMinCut(graph):
    q = PriorityQueue()
    # Priority queue init
    for u in graph.vertices:
        q.put((0, u))
    s = t = None
    while not q.empty():
        (k, u) = q.get()
        s, t = t, u
        # Probably sbagliato
        for v in graph.adj_list(u):
            for e in q.queue:
                k, n = e
                if n == v:
                    k -= graph.weight(u, v)
    return sum(graph.adj_matrix[t]), s, t, perf_counter_ns()


def stoer_wagner(graph):
    if graph.n_vertices == 2:
        vertices = list(v for v in graph.vertices)
        return graph.weight(vertices[0], vertices[1]), perf_counter_ns()
    else:
        c1, s, t, d_t1= stMinCut(graph)
        # G\{s,t}
        g = copy.deepcopy(graph)
        g.remove(s)
        g.remove(t)
        c2, d_t2 = stoer_wagner(g)
        if c1 <= c2:
            return int(c1), d_t1
        else:
            return int(c2), d_t2

from custom_queue import PriorityQueue
from time import perf_counter_ns
import copy
import numpy as np
from tqdm import tqdm


def stMinCut(graph):
    q = PriorityQueue()
    keys = {}
    # Priority queue init
    for u in graph.vertices:
        q.put((0, u))
        keys[u] = 0
    s = t = None
    while not q.empty():
        (k, u) = q.pop()
        s = t
        t = u
        for v in graph.adj_list(u):
            if v in q:
                keys[v] = keys[v] + graph.weight(u, v)
                q.update_elem(v, (keys[v], v))
    return sum(graph.adj_matrix[t,:] + graph.adj_matrix[:,t]), s, t, perf_counter_ns()


def stoer_wagner(graph):
    if graph.n_vertices == 2:
        vertices = list(v for v in graph.vertices)
        c = perf_counter_ns()
        # QUI, deve tornare il taglio perchè poi ne deve misurare il
        # peso, usare solo il peso dell'arco tra i due non restituisce
        # una visione completa
        return graph.weight(vertices[0], vertices[1]), graph.n_vertices, graph.n_edges, c, c
    else:
        # G\{s,t}
        g = copy.deepcopy(graph)
        c1, s, t, d_t1= stMinCut(graph)
        # do not consider s and t anymore, but do not remove the
        # edges, in order to consider them for future cuts
        g.remove(s,False)
        g.remove(t,False)
        c2, n, m, d_t2, junk = stoer_wagner(g)
        if c1 <= c2:
            return c1, graph.n_vertices, graph.n_edges, d_t1, perf_counter_ns()
        else:
            return c2, graph.n_vertices, graph.n_edges, d_t2, perf_counter_ns()

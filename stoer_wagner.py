from custom_queue import PriorityQueue
from time import perf_counter_ns
import copy
import numpy as np

def stMinCut(graph):
    q = PriorityQueue()
    # Priority queue init
    for u in graph.vertices:
        q.put((0, u))
    s = t = None
    while not q.empty():
        (k, u) = q.pop()
        s = t
        t = u
        # tqdm.write("{}".format(q))
        for v in graph.adj_list(u):
            if v in q:
                k += graph.weight(u, v)
                q.update_elem(v, (k,v))
    return sum(graph.adj_matrix[t,:] + graph.adj_matrix[:,t]), s, t, perf_counter_ns()


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
            return c1, d_t1
        else:
            return c2, d_t2

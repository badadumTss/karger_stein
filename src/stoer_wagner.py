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
    
    Vmt = set(graph.vertices)
    Vmt.remove(t)
    return ((Vmt, {t}),
            s,
            t,
            perf_counter_ns())


def stoer_wagner(graph):
    
    if graph.n_vertices == 2:
        vs = list(v for v in graph.vertices)
        return ({vs[0]}, {vs[1]}), perf_counter_ns()
    
    else:
        g = copy.deepcopy(graph)
        c1, s, t, d_t1 = stMinCut(graph)

        # G\{s,t}
        g.remove(s)
        g.remove(t)
        
        # (X2, Y2)
        (X2, Y2), d_t2 = stoer_wagner(g)

        s1 = X2.union({s,t})
        s2 = Y2.union({s,t})
        cuts = [(s1, Y2), (X2, s2)]
        
        c2 = None
        if graph.cut_weight(cuts[0]) <= graph.cut_weight(cuts[1]):
            c2 = cuts[0]
        else:
            c2 = cuts[1]

        if graph.cut_weight(c1) <= graph.cut_weight(c2):
            return c1, d_t1
        else:
            return c2, d_t2

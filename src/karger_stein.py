import copy
import numpy as np
from time import perf_counter_ns
import random

def contract(graph, n_v=2):
    g = copy.deepcopy(graph)
    while g.n_vertices > n_v:
        # Build the cumulative weights list
        ws = list(map(lambda e: g.weight(e[0],e[1]), g.edges))
        cum_ws = [sum(ws[:i+1]) for i in range(len(ws))]
        # give it to random.choices, as it already has the
        # random_select procedura incorporated
        res = random.choices(g.edges, cum_weights=cum_ws)
        u, v = res[0]
        g.merge_vertices(u, v)
    return g


def rec_contract(graph):
    if graph.n_vertices <= 6:
        g = contract(graph)
        u,v = g.edges[0]
        return g.weight(u,v), perf_counter_ns()
    
    t = int(np.ceil(graph.n_vertices / np.sqrt(2)) + 1)
    w1, t1 = rec_contract(contract(graph, t))
    w2, t2 = rec_contract(contract(graph, t))
    
    if w2 < w1:
        return w2, t2
    else:
        return w1, t1


def karger_stein(graph):
    amin = np.Inf
    full_d_time = 0
    n = graph.n_vertices
    graph.n_edges
    k = int(np.ceil(n * np.log(n) / (n-1)))
    for i in range(k):
        t, d_time = rec_contract(graph)
        if t < amin:
            amin = t
            full_d_time = d_time
    return amin, full_d_time

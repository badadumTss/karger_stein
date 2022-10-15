from time import perf_counter_ns
import numpy as np
from karger_stein import contract
from stoer_wagner import stoer_wagner

def hybrid_iteration(graph):
    t = np.ceil(graph.n_vertices / np.sqrt(2) + 1)
    g = contract(graph, t)
    # Gets better for the last iterations, the graph given to
    # stoer_wagner has t vertices
    return stoer_wagner(g)
    
def hybrid(graph):
    n = graph.n_vertices
    t = int(np.ceil((n * np.log(n)/ (n-1)))) # The same bound as for
                                             # Karger and Stein
                                             # applies
    amin = np.Inf
    d_time = 0
    for i in range(t):
        cut, d_time = hybrid_iteration(graph)
        if cut < amin:
            amin = cut
            d_time = perf_counter_ns()
    return amin, d_time

from custom_queue import PriorityQueue
from time import perf_counter_ns
import copy


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
    return (graph.cut_weight((Vmt, {t})),
            s,
            t,
            perf_counter_ns())


def stoer_wagner(graph):
    
    if graph.n_vertices == 2:
        vs = list(v for v in graph.vertices)
        return graph.weight(vs[0], vs[1]), perf_counter_ns()
    
    else:
        g = copy.deepcopy(graph)
        c1, s, t, d_t1 = stMinCut(graph)

        g.merge_vertices(s, t)
        
        c2, d_t2 = stoer_wagner(g)

        if c1 <= c2:
            return c1, d_t1
        else:
            return c2, d_t2

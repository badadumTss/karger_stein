import numpy as np


class Graph:
    # n_vertices builds the adjency matrix. `edges` are tuples in the
    # shape (a,b) where (a < b) and w in R
    def __init__(self, n_vertices, edges):
        # Assumption: there are no zero-valued edges. otherwise the
        # adj matrix initialised as such would be not valid
        self.adj_matrix = np.zeros((n_vertices, n_vertices))
        self.vertices = [i for i in range(n_vertices)]
        # self.edges = [(a,b) for a,b,w in edges]
        self.degrees = np.zeros(n_vertices)
        for (a, b, w) in edges:
            self.adj_matrix[a][b] = self.adj_matrix[b][a] = w
        self.normalize_adj()

    def normalize_adj(self):
        self.adj_matrix = np.triu(self.adj_matrix)

    @property
    def n_edges(self):
        return int(len(np.nonzero(self.adj_matrix)[0]))

    @property
    def edges(self):
        gen = np.nonzero(self.adj_matrix)
        l = zip(gen[0], gen[1])
        return list(l)
    
    @property
    def n_vertices(self):
        return len(self.vertices)

    def __repr__(self):
        return "graph with {} vertices and {} edges".format(self.n_vertices, self.n_edges)

    def weight(self, u, v):
        if v > u:
            return self.adj_matrix[u][v]
        else:
            return self.adj_matrix[v][u]

    def set_weight(self, u, v, n_w):
        self.adj_matrix[u][v] = self.adj_matrix[v][u] = n_w
        self.normalize_adj()

    def adj_list(self, v):
        row = self.adj_matrix[v,:]
        col = self.adj_matrix[:,v]
        return [i for i,u in enumerate(row+col) if u != 0]

    # Merges two vertices together. Does so by adding to the first
    # node all the edges the second one was attached to , except for
    # those between them; finally removes the second edge from the set
    # of edges
    def merge_vertices(self, u, v):
        self.adj_matrix[u][v]

        # generator for all the nodes except u and v
        gen = (x for x in self.vertices if x != u and x != v)
        
        for x in gen:
            self.set_weight(u, x, self.weight(u, x) + self.weight(v, x))
            
        self.remove(v)

    # removes a node from the set of vertices, if remove_edges=True
    # removes also all the edges attached to that node
    def remove(self, n, remove_edges=True):
        if remove_edges:
            self.adj_matrix[n, :] = 0
            self.adj_matrix[:, n] = 0
        self.vertices.remove(n)

    # returns the weight of a given cut, rapresented as a tuple of
    # exactly 2 sets of vertices
    def cut_weight(self, cut):
        c1, c2 = cut
        w = 0
        for u in c1:
            for v in c2:
                w += self.weight(u,v)
        return w

class GraphAdjMatrix:
    def __init__(self):
        self.index = {}
        self.mat = []

    def add_vertex(self, v):
        if v in self.index:
            return

        idx = len(self.index)
        self.index[v] = idx

        for row in self.mat:
            row.append(0)

        self.mat.append([0] * (idx + 1))

    def add_edge(self, u, v, directed=False):
        self.add_vertex(u)
        self.add_vertex(v)

        i = self.index[u]
        j = self.index[v]

        self.mat[i][j] = 1

        if not directed:
            self.mat[j][i] = 1

    def has_edge(self, u, v):
        if u not in self.index or v not in self.index:
            return False

        i = self.index[u]
        j = self.index[v]

        return self.mat[i][j] == 1